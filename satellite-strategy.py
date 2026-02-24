import pandas as pd
import requests
import argparse
import os
import calendar
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv

# ==============================================================================
# CONFIGURATION & STRATEGY PARAMETERS
# ==============================================================================

CASH_TICKER = "VCAA.XETRA"  
CASH_NAME   = "CASH (Vanguard EUR Cash)"
CASH_ISIN   = "IE000SOORXS0" 

WEIGHTS = {'1M': 4, '3M': 5, '6M': 3, '10M': 2}
SMA_WINDOW_DAYS = 200
BASE_URL = "https://eodhd.com/api/eod/"

# ==============================================================================
# DATA RETRIEVAL & PROCESSING
# ==============================================================================

def fetch_history(ticker, api_key, max_retries=3):
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    url = f"{BASE_URL}{ticker}"
    params = {'api_token': api_key, 'from': start_date, 'fmt': 'json'}
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            
            # Handling Rate Limits (429) and Server Errors (500, 502, 503, 504)
            if response.status_code == 429 or response.status_code >= 500:
                wait_time = 2 ** attempt
                print(f"      [API HTTP {response.status_code}] Delaying execution for {ticker}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
                continue
                
            response.raise_for_status()
            data = response.json()
            
            # Verify if API returned a valid list structure
            if not isinstance(data, list):
                print(f"      [ERROR] Unexpected JSON structure for {ticker}.")
                return None

            df = pd.DataFrame(data)
            
            if df.empty:
                print(f"      [WARNING] No historical data returned for {ticker}.")
                return None
            
            if 'adjusted_close' in df.columns:
                df = df[['date', 'adjusted_close']].rename(columns={'adjusted_close': 'close'})
            elif 'close' in df.columns:
                df = df[['date', 'close']]
            else:
                print(f"      [ERROR] Required price columns missing for {ticker}.")
                return None
                
            df['date'] = pd.to_datetime(df['date'])
            df.set_index('date', inplace=True)
            df.sort_index(inplace=True)
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"      [ERROR] Network/API request failed for {ticker}: {e}")
            break
        except Exception as e:
            print(f"      [ERROR] Data processing failed for {ticker}: {e}")
            break
            
    return None

def get_monthly_data(df):
    df = df.copy()
    df['period'] = df.index.to_period('M')
    monthly_df = df.groupby('period').last()
    monthly_df.index = df.groupby('period')['close'].apply(lambda x: x.index[-1])
    return monthly_df

def calculate_metrics(df_daily):
    if len(df_daily) < 200: 
        print(f"      -> Excluded: Insufficient historical data ({len(df_daily)} days < 200)")
        return None

    df_monthly = get_monthly_data(df_daily)
    last_available_date = df_monthly.index[-1]
    now = datetime.now()
    
    _, last_day_of_month = calendar.monthrange(now.year, now.month)
    
    if (last_available_date.month == now.month) and (last_available_date.year == now.year):
        cutoff_day = last_day_of_month - 2
        if now.day < cutoff_day:
            if len(df_monthly) < 2: return None 
            df_monthly = df_monthly.iloc[:-1]
    
    if len(df_monthly) < 11: 
        print(f"      -> Excluded: Insufficient monthly historical data.")
        return None 
    
    p0_row = df_monthly.iloc[-1]
    p0_date = p0_row.name
    p0_price = p0_row['close']
    
    try:
        p_1m  = df_monthly.iloc[-2]['close']
        p_3m  = df_monthly.iloc[-4]['close']
        p_6m  = df_monthly.iloc[-7]['close']
        p_10m = df_monthly.iloc[-11]['close']
    except IndexError:
        return None

    r_1m  = (p0_price / p_1m) - 1
    r_3m  = (p0_price / p_3m) - 1
    r_6m  = (p0_price / p_6m) - 1
    r_10m = (p0_price / p_10m) - 1

    total_weight = sum(WEIGHTS.values())
    score = ((WEIGHTS['1M'] * r_1m) + (WEIGHTS['3M'] * r_3m) + (WEIGHTS['6M'] * r_6m) + (WEIGHTS['10M'] * r_10m)) / float(total_weight)
    
    df_daily_sliced = df_daily.loc[:p0_date]
    sma200 = df_daily_sliced['close'].rolling(window=SMA_WINDOW_DAYS).mean().iloc[-1]
    
    is_uptrend = (p0_price > sma200) and (score > 0)

    return {
        'price': p0_price, 'sma200': sma200, 'score': score, 'is_uptrend': is_uptrend, 'ref_date': p0_date.strftime('%Y-%m-%d'),
        'p1m': p_1m, 'p3m': p_3m, 'p6m': p_6m, 'p10m': p_10m, 'r1m': r_1m, 'r3m': r_3m, 'r6m': r_6m, 'r10m': r_10m
    }

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

def main():
    load_dotenv()

    print("\n" + "="*60)
    print(" SATELLITE STRATEGY ALGORITHM")
    print(" Strategy: GTAA Agg 3 Dual Momentum")
    print("="*60 + "\n")

    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', type=str, default=None)
    parser.add_argument('--file', type=str, default='ticker.csv')
    parser.add_argument('--current', type=str, default='', help='Comma-separated list of currently held tickers')
    args = parser.parse_args()

    if args.api_key: api_key = args.api_key
    elif os.getenv('EODHD_API_KEY'): api_key = os.getenv('EODHD_API_KEY')
    else: api_key = 'demo'

    current_holdings = [t.strip() for t in args.current.split(',')] if args.current else []

    if not os.path.exists(args.file):
        print(f"[ERROR] Required input file '{args.file}' not found.")
        return

    tickers_df = pd.read_csv(args.file)
    tickers_df.columns = [c.strip().lower() for c in tickers_df.columns]
    tickers_df['ticker'] = tickers_df['ticker'].astype(str).str.strip()
    
    if 'name' not in tickers_df.columns: 
        tickers_df['name'] = tickers_df['ticker']
    if 'isin' not in tickers_df.columns:
        tickers_df['isin'] = ''
    else:
        tickers_df['isin'] = tickers_df['isin'].astype(str).str.strip()

    results = []
    print(f"Initiating analysis for {len(tickers_df)} assets...\n")

    for index, row in tickers_df.iterrows():
        ticker = row['ticker']
        print(f"   ... processing data for: {ticker}")
        df = fetch_history(ticker, api_key)
        
        if df is not None:
            metrics = calculate_metrics(df)
            if metrics:
                results.append({
                    'Ticker': ticker,
                    'Name': row['name'],
                    'ISIN': row['isin'],
                    'constraint_group': row.get('constraint_group', None),
                    'Close': metrics['price'],
                    'RefDate': metrics['ref_date'],
                    'Score': metrics['score'],
                    'Is_Uptrend': metrics['is_uptrend'],
                    'SMA200': metrics['sma200'],
                    'P1M': metrics['p1m'], 'P3M': metrics['p3m'],
                    'P6M': metrics['p6m'], 'P10M': metrics['p10m'],
                    'R1M': metrics['r1m'], 'R3M': metrics['r3m'],
                    'R6M': metrics['r6m'], 'R10M': metrics['r10m']
                })
        
        # Proactive rate limiting to respect EODHD 10 req/sec limit
        time.sleep(0.2)

    if not results: return

    df_results = pd.DataFrame(results).sort_values(by='Score', ascending=False)
    
    # ---------------------------------------------------------
    # APPLY RANK STABILITY RULE (Top 7 Buffer) & CONSTRAINT CHECK
    # ---------------------------------------------------------
    
    if 'constraint_group' not in df_results.columns:
        df_results['constraint_group'] = None
    
    buffer_df = df_results.head(7)
    
    final_allocation = []
    group_usage = {}

    def add_to_allocation(row_dict):
        final_allocation.append(row_dict)
        grp = row_dict.get('constraint_group')
        if pd.notna(grp) and str(grp).strip():
            grp_str = str(grp).strip()
            group_usage[grp_str] = group_usage.get(grp_str, 0) + 1

    # --- Step 1: Retain current holdings (Rank Stability Buffer) ---
    if current_holdings:
        for ticker in current_holdings:
            match = buffer_df[(buffer_df['Ticker'] == ticker) & (buffer_df['Is_Uptrend'] == True)]
            if not match.empty:
                row_dict = match.iloc[0].to_dict()
                grp = row_dict.get('constraint_group')
                grp_str = str(grp).strip() if pd.notna(grp) and str(grp).strip() else None
                
                if grp_str and group_usage.get(grp_str, 0) >= 1:
                    continue
                
                if len(final_allocation) < 3:
                    add_to_allocation(row_dict)

    # --- Step 2: Allocate remaining capital from the primary ranking ---
    for _, row in df_results.iterrows():
        if len(final_allocation) >= 3:
            break
            
        ticker = row['Ticker']
        
        if ticker in [a['Ticker'] for a in final_allocation]:
            continue
            
        if not row['Is_Uptrend']:
            continue
            
        grp = row.get('constraint_group')
        grp_str = str(grp).strip() if pd.notna(grp) and str(grp).strip() else None
        
        if grp_str and group_usage.get(grp_str, 0) >= 1:
            print(f"      -> Skipped {ticker} (Constraint limit reached for: {grp_str})")
            continue
            
        add_to_allocation(row.to_dict())

    final_allocation = sorted(final_allocation, key=lambda x: x['Score'], reverse=True)
    
    # ---------------------------------------------------------
    # HANDLE DEFENSIVE MODE (Dynamic Cash Padding)
    # ---------------------------------------------------------
    
    valid_positions = len(final_allocation)
    cash_slots_needed = 3 - valid_positions
    
    if cash_slots_needed == 3:
        print("\n[WARNING] Zero assets passed momentum constraints. Activating Full Defensive Mode (100 % Cash/Money Market).")
    elif cash_slots_needed > 0:
        print(f"\n[WARNING] Only {valid_positions} assets in confirmed uptrend. Padding remaining {cash_slots_needed} slot(s) with Cash/Money Market.")
        
    while len(final_allocation) < 3:
        final_allocation.append({
            'Ticker': CASH_TICKER, 
            'ISIN': CASH_ISIN,
            'Name': CASH_NAME, 
            'Score': 0.0,
            'Is_Uptrend': True
        })

    # ---------------------------------------------------------
    # OUTPUT GENERATION
    # ---------------------------------------------------------
    print("\n" + "-"*60)
    print(" ALGORITHMIC RANKING (Top 7 - For Rank Stability Rule)")
    print("-" * 60)
    
    cols_to_show = ['Ticker', 'ISIN', 'Name', 'Score', 'Is_Uptrend']
    print(buffer_df[cols_to_show].to_string(index=False, formatters={'Score': lambda x: f"{x:.2%}".replace('.', ',').replace('%', ' %')}))

    print("\n" + "-"*60)
    print(" FINAL ALLOCATION DIRECTIVE (Post-Filter Assessment)")
    print("-" * 60)
    
    display_alloc = []
    for i, item in enumerate(final_allocation):
        action = 'HOLD' if item['Ticker'] in current_holdings else 'BUY'
        if item['Ticker'] == CASH_TICKER: action = 'FALLBACK'
        
        display_alloc.append({
            'Pos': i+1, 
            'Action': action, 
            'Ticker': item['Ticker'], 
            'ISIN': item.get('ISIN', ''),
            'Name': item['Name']
        })
    
    print(pd.DataFrame(display_alloc).to_string(index=False))

    if current_holdings:
        new_tickers = [a['Ticker'] for a in final_allocation if a['Ticker'] != CASH_TICKER]
        sells = [t for t in current_holdings if t not in new_tickers and t != CASH_TICKER]
        buys  = [t for t in new_tickers if t not in current_holdings]
        
        print("\nTURNOVER LOGIC:")
        print(f"   Current Holdings: {current_holdings}")
        print(f"   Target Target:    {new_tickers}")
        print(f"   Required Sales:   {sells}")
        print(f"   Required Buys:    {buys}")

    timestamp = datetime.now().strftime('%Y-%m-%d')
    filename = f"satellite_signals_{timestamp}.csv"
    df_results.to_csv(filename, index=False, sep=';', decimal=',')
    print(f"\n[SYSTEM] Detailed analytical report exported to: {filename}")

if __name__ == "__main__":
    main()