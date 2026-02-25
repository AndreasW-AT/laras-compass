# Lara’s Compass – Systematic Market Navigation

### Framework for Structured Wealth Accumulation and Risk Governance

---

**Status:** February 2026  
**Perspective:** Private Retail Investor (Austria / Flatex)  
**Objective:** Long-term capital growth with minimized drawdown exposure.

---

## Table of Contents

1. [Prologue](#1-prologue)
2. [Investment Philosophy & Principles](#2-investment-philosophy--principles)
3. [Portfolio Architecture](#3-portfolio-architecture)
4. [The Core Portfolio](#4-the-core-portfolio)
5. [The Satellite Portfolio](#5-the-satellite-portfolio)
6. [Historical Context & Expected Behavior](#6-historical-context--expected-behavior)
7. [Jurisdictional Framework (Austria)](#7-jurisdictional-framework-austria)
8. [Technical Implementation](#8-technical-implementation)
9. [Operational Protocol](#9-operational-protocol)
10. [References & Data Sources](#10-references--data-sources)
11. [Financial & Legal Disclaimer](#11-financial--legal-disclaimer)

---

## 1. Prologue

> *This work is dedicated to my daughter, Lara.*
> 
> *May this strategy, rooted in deep research, serve as a financial foundation for your life. It is designed to let you sleep soundly when the world goes crazy, and to let you participate in growth when the economy flourishes. This is not a casino. It is an instrument for your future.*

---

## 2. Investment Philosophy & Principles

The foundation relies on a strict **Core-Satellite Architecture**, functionally separating market breadth and stabilization (the Core) from active, trend-following excess return generation (the Satellite).

### Fundamental Tenets

1. **Tax Hygiene & Structural Efficiency**
   
   * The primary detractor of compound interest is fiscal friction — both direct (Capital Gains Tax) and indirect (Withholding Tax Leakage).
   * **Core Allocation:** Maximizes tax deferral. Assets are held long-term to leverage the compounding effect on unrealized gains.
   * **Satellite Allocation:** Accepts capital gains taxes as operational friction, strictly contingent on the generated Alpha mathematically compensating for the tax drag.
   * **Asset Selection:** Prioritizes the most efficient legal structure available over mere index tracking.

2. **Diversification & Systematic Risk**
   
   * The strategy mitigates idiosyncratic risk by excluding single equities. 
   * All utilized instruments must track an index, a predefined basket, or a macro-economic factor, ensuring exposure remains systematic.

3. **Algorithmic Governance & Execution Discipline**
   
   * The approach is entirely systematic: Rules are defined ex-ante, and quantitative signals dictate execution.
   * The quantitative model measures and quantifies established trends rather than attempting predictive forecasting. Market entry, rotation, and cash allocation are executed strictly according to the mathematical output.

---

## 3. Portfolio Architecture

**Target Allocation:** 80 % Core / 20 % Satellite.

Capital management and rebalancing are primarily executed via continuous monthly capital inflows. To preserve the mathematical edge of the trend-following component, the portfolio utilizes **Dynamic Trend-Conditioned Bands** rather than static tolerance thresholds:

1. **Upper Bound Scenario (Satellite > 25 %):**
   
   * *Trigger:* Disproportionate Satellite growth driven by persistent macro trends.
   * *Action:* Assess the technical integrity of the Top 3 Satellite constituents. Are at least 2 constituents maintaining a confirmed uptrend (Price > SMA200)?
     * **Yes (Trend Intact + Satellite 25 - 32 %):** Maintain exposure with controlled capital allocation (70 % of new inflows allocate to the Core, 30 % to the Satellite).
     * **Yes (Trend Intact + Satellite > 32 %):** Cease Satellite capital inflows entirely (100 % of new inflows allocate to the Core) to cap aggressive strategy concentration at roughly one-third of the total portfolio.
     * **No (Trend Weakening):** Sell Satellite assets to revert to the 20 % baseline target. Realized net gains are subsequently injected into the Core.

2. **Lower Bound Scenario (Satellite < 15 %):**
   
   * *Trigger:* Significant Satellite drawdown.
   * *Action:* No assets are liquidated from the Core (preserving the tax shield). Priority Rebalancing applies: 70 % of new capital inflows are allocated directly to the Satellite until the threshold of ≥ 18 % is re-established.

---

## 4. The Core Portfolio

*Objective: Broad market capitalization with controlled volatility exposure.* \
*Profile: Growth-oriented, structurally stabilized, low-maintenance.*

* **Methodology:** A hybrid framework adapting John C. Bogle's principles and Tyler's *Golden Butterfly Portfolio* to a simplified, low-friction macro-index approach. The original fragmentation (e.g., Small vs. Large Cap, Short vs. Long Term Bonds) is deliberately consolidated into single broad market tickers to minimize rebalancing friction and operational complexity.

* **The Growth Tilt:** The allocation implements a heavy 70 % equity weighting to maximize long-term generational compounding. Volatility is counterbalanced by typically uncorrelated stabilizers (Bonds and Gold) and a systematic accelerated accumulation protocol.

| Weight   | Asset Class     | Instrument (Example)                            | Function                                                         |
|:-------- |:--------------- |:----------------------------------------------- |:---------------------------------------------------------------- |
| **70 %** | Global Equities | Vanguard FTSE All-World Acc (VWCE)              | Primary compounding engine.                                      |
| **20 %** | Gov. Bonds      | Vanguard Global Gov. Bond EUR Hedged Acc (VGGF) | Structural stabilization, crisis correlation and interest yield. |
| **10 %** | Gold            | EUWAX Gold II (EWG2)                            | Currency hedge and inflation protection.                         |

### Operational Mechanics & Accelerated Accumulation

1. **Savings Plan Control (Standard):** Under normal market conditions (price > SMA200d/SMA10M), monthly capital inflows are systematically routed into whichever of the three Core positions is most underweight relative to its percentage target.
2. **Annual Rebalancing:** The baseline allocation (70/20/10) is reviewed annually. The primary mechanism for maintaining target weights is the strategic routing of continuous capital inflows. Active rebalancing (liquidating assets) is strictly executed only if positional deviations exceed **5 percentage points** AND the mathematical benefit of realigning the portfolio demonstrably outweighs the resultant fiscal drag (capital gains tax) and transactional friction. This mandate ensures the protocol scales efficiently and remains mathematically viable regardless of the absolute portfolio magnitude.

**Accelerated Accumulation Protocol (The Anti-Cyclical Tilt):**

* *Applicability:* Restricted to the core equity allocation (e.g., `VWCE`).
* *Trigger Mechanism:* The monthly closing price (Ultimo) of the equity asset falls below its 10-month Simple Moving Average (SMA10M).
* *Action (Cost-Basis Reduction):* The standard proportional distribution of inflows is suspended. 100 % of all designated Core capital inflows are aggressively routed into the equity allocation to maximize share accumulation at depressed valuations.
* *Redeployment:* Standard balancing of inflows across all Core assets (Equities, Bonds, Gold) resumes as soon as the monthly closing price recovers above the SMA10M.
* This buy-and-hold protocol functions as the systematic counter-weight to the Satellite’s momentum logic. While the Satellite exits during price declines, the Core utilizes phases below the SMA10M for aggressive cost-basis reduction. This "bet on global recovery" ensures that the portfolio accumulates maximum shares at depressed valuations, which historically serves as the primary driver for outsized returns during the subsequent recovery phase.

---

## 5. The Satellite Portfolio

*Objective: Alpha generation via dynamic trend capture and asset rotation.* \
*Profile: Aggressive, statistically grounded, actively managed.*

* **Methodology:** A composite model expanding on Mebane T. Faber's *Global Tactical Asset Allocation* and Gary Antonacci's *Dual Momentum*. Unlike standard implementations, this strategy applies an adaptive 2-5-4-3 weighting framework. This mathematical engine builds upon the foundational momentum anomaly research by Narasimhan Jegadeesh and Sheridan Titman, incorporates the cross-asset momentum principles of AQR Capital Management (Cliff Asness), and aligns with the core concepts of *Adaptive Asset Allocation (AAA)* formulated by Adam Butler, Michael Philbrick, and Rodrigo Gordillo.

* **Algorithm Constraints:** Relies strictly on End-Of-Month (Ultimo) pricing data. The portfolio allocates evenly to the Top 3 assets selected from a diversified, low-correlation universe (`ticker.csv`). 

### The Universe Selection ("Algorithmic Alpha vs. Beta Asset")

To protect the mathematical edge of the strategy, the selection of instruments must follow a strict "Vanilla Macro" approach. The Python algorithm provides the intelligence. The underlying assets must provide pure, unadulterated market exposure (Beta). 

* **No Active Management:** Avoid actively managed ETFs, "Smart Beta" constructs, or heavily ESG-screened products. The algorithm must measure raw global capital flows, not subjective fund manager opinions.
* **Massive & Ultra-Liquid:** Only heavyweight ETFs with immense Assets Under Management (AUM) are permitted to ensure minimal bid-ask spreads and reduce invisible frictional costs (slippage).
* **Lumping vs. Slicing:** Consolidate broad economic regimes rather than slicing into micro-themes (e.g., favoring a broad `FTSE Developed Europe` over a fragmented `Europe ex-UK`+`UK` setup to capture the clean, overarching macro trend).
* **Zero Redundancy:** Highly correlated assets fulfilling identical roles are excluded to prevent microscopic performance noise from generating useless tax events ("whipsawing").
* **Expansion via Certificates:** Index and Participation Certificates are permitted to reduce transaction costs or cover niches, under strict conditions:
  1. *Delta-1 Only:* Must track the underlying 1:1. Leveraged products and instruments with profit caps (Discount/Bonus Certificates) are strictly forbidden.
  2. *Issuer Quality:* Only systemically relevant major banks (e.g., Morgan Stanley, J.P. Morgan, UBS, Goldman Sachs) to minimize issuer risk.

### The Quantitative Model

**1. Trend Strength Quantification and Endpoint Sensitivity Reduction** \
Standard momentum relies on point-to-point returns, making it highly vulnerable to single historical price outliers. By calculating a weighted average across four distinct segmented periods, the model effectively smooths the data distribution and reduces endpoint sensitivity, prioritizing the "Golden Zone" of trend persistence.

$$
Score = \frac{2 \cdot R_{1M} + 5 \cdot R_{3M} + 4 \cdot R_{6M} + 3 \cdot R_{10M}}{14}
$$

* **$R_{1M}$ (Weight: 2):** Functions as a minimal tie-breaker. The weight is intentionally suppressed to filter out short-term statistical noise and prevent performance erosion caused by mean reversion. 
* **$R_{3M}$ (Weight: 5) & $R_{6M}$ (Weight: 4):** The core anchors of the strategy. Research by Narasimhan Jegadeesh & Sheridan Titman (the pioneers of momentum research) and AQR Capital (Cliff Asness) provides clear evidence: The strongest, most robust momentum signal across asset classes, least vulnerable to mean reversion, resides precisely within the 3 to 6-month window.
* **$R_{10M}$ (Weight: 3):** Long-term trend baseline. The 10-month parameter (equivalent to 200 days) is intentionally selected to align the strategy's maximum historical lookback with the data retrieval limits of the EODHD API Free Tier, ensuring technical operational feasibility.

**Macro-Inertia Calibration and Signal-to-Noise Integrity:** The specific mathematical weighting ($2 \cdot R_{1M} + 5 \cdot R_{3M} + 4 \cdot R_{6M} + 3 \cdot R_{10M}$) is explicitly calibrated to capture the structural inertia of broad macroeconomic sectors and primary asset classes. It is inherently unsuitable for the higher volatility profiles of single equities, narrow thematic ETFs, or isolated smart-beta factors. Applying this specific smoothing model to highly volatile micro-assets would degrade the signal-to-noise ratio, resulting in severe signal lag and delayed execution (whipsawing). Therefore, the strict adherence to the "Lumping vs. Slicing" doctrine is a fundamental mathematical prerequisite for the algorithm's validity, not merely a stylistic preference.

**2. Absolute Momentum (Trend Filter)** \
An asset is only eligible for selection if it exhibits both relative outperformance ($Score > 0$) AND absolute momentum (Current Price > SMA200). 

**3. Cluster Risk Governance** \
Assets are categorized by constraint groups (e.g., Crypto, Real Estate). The algorithm enforces a strict limit (maximum 1 slot per group) within the Top 3 selection to prevent excessive sector concentration. 

**4. Transaction Cost Mitigation (Rank Stability)** \
To prevent mathematical edge erosion through frictional costs (e.g., broker fees, bid-ask spreads, and tax events), a buffer rule is applied: An existing asset is retained as long as it remains within the Top 7 rankings. This threshold provides a structural tolerance band, representing the upper echelon of the dynamic investment universe. Rotation is triggered strictly when an asset falls outside this Top 7 buffer or violates the absolute momentum baseline. This operational suppression of unnecessary churn ensures that the algorithm prioritizes signal stability over marginal ranking shifts, optimizing net compounding.

**Critical Constraint (Minimum Capital):** Given base brokerage fees, the Satellite allocation should only be activated with a minimum designated capital of 5.000 € (corresponding to a total portfolio minimum of 25.000 € at a 20 % weighting) to ensure transactional friction does not negate the generated Alpha. Below this threshold, a static 70/20/10 Core-only portfolio is mandated.

---

## 6. Historical Context & Expected Behavior

* **Normal Market Conditions:** The Core grows steadily, capturing general market returns. The Satellite functions as an accelerator, capitalizing on established, persistent macroeconomic trends.
* **Crisis Scenarios (Market Crashes):**
  * The Core temporarily depreciates but is buffered by the inverse correlation of Government Bonds and the non-correlated Gold allocation. During sustained market downtrends (Price < SMA200d/SMA10M), the core switches into the Accelerated Accumulation Protocol, aggressively funneling all new capital inflows into equities to lower the average cost basis.
  * The Satellite rapidly cuts exposure via its absolute momentum filters, moving completely into money market instruments or cash to preserve capital for re-entry at the systemic bottom.
  
  ---

## 6. Historical Context & Expected Behavior

* **Normal Market Conditions:** The Core grows steadily, capturing general market returns. The Satellite functions as an accelerator, capitalizing on established, persistent macroeconomic trends.
* **Crisis Scenarios (Market Crashes):**
  * The Core temporarily depreciates but is buffered by the inverse correlation of Government Bonds and the non-correlated Gold allocation. During sustained market downtrends (Price < SMA200d/SMA10M), the core switches into the Accelerated Accumulation Protocol, aggressively funneling all new capital inflows into equities to lower the average cost basis.
  * The Satellite rapidly cuts exposure via its absolute momentum filters, moving completely into money market instruments or cash to preserve capital for re-entry at the systemic bottom.
* **Risk-Adjusted Performance (Sortino Ratio):** Theoretically, the synthesis of the Core's structural stability and the Satellite's absolute momentum filter is designed to optimize the portfolio's Sortino Ratio. By systematically clipping the left-tail risk (severe drawdowns) while capturing macro uptrends, the architecture aims for asymmetric compounding. Ultimately, empirical future market data will be the sole validator of this theoretical edge.

---

## 7. Jurisdictional Framework

The asset selection process is structurally optimized for Austrian fiscal regulations to prevent systemic performance degradation.

* **Domicile Optimization ("Ireland-Bias"):** To mitigate the standard 30 % US withholding tax on dividends, funds holding significant US equity exposure must be domiciled in Ireland (ISIN prefix "IE") to benefit from the reduced 15 % rate under the US-Ireland Double Taxation Treaty.
* **Reporting Fund Status ("Meldefonds"):** All utilized instruments must be officially registered as "Meldefonds" with the Oesterreichische Kontrollbank (OeKB) to avoid punitive lump-sum taxation ("Pauschalbesteuerung").
* **Transparency & Replicability ("Opaque AgE Protection"):** Synthetic, swap-based ETFs are strictly excluded. Under Austrian tax law, the deemed distributed income ("ausschüttungsgleiche Erträge") for synthetic funds is calculated based on the fund's actual substitute basket, not the tracked index. This structural mismatch frequently triggers highly unpredictable, inflated tax events. The strategy utilizes physically replicating ETFs exclusively, ensuring that the fiscal drag is strictly tied to the transparent, fundamental yield of the targeted macro-asset.

---

## 8. Technical Implementation

The algorithmic component of the Satellite portfolio is executed via a Python script to ensure emotional detachment and mathematical precision. 

### System Requirements

* Python 3.x
* Required libraries: `pandas`, `requests`, `argparse`, `python-dotenv`
* EODHD API Key (End-Of-Day Historical Data)

### Directory Architecture

The working directory must maintain a flat structure:

```text
Project-Directory/
├── satellite-strategy.py    (Execution Script)
├── .env                     (Configuration/API Key)
└── ticker.csv               (Investment Universe Data)
```

### Configuration

Store the API key securely in the `.env` file to automate authentication:

Plaintext

```
EODHD_API_KEY=YOUR_API_KEY_STRING
```

The `ticker.csv` defines the permissible investment universe according to the strict criteria outlined in section 5.

Code-Snippet

```
ticker,name,isin,constraint_group
XDWT.XETRA,Xtrackers MSCI World Information Technology,IE00BM67HT60,TECH_AND_GROWTH
VWCG.XETRA,Vanguard FTSE Developed Europe,IE00BK5BQX27,
...
```

### Command Line Execution

The script provides a terminal-based output ranking and exports a detailed historical CSV file.

**Standard Execution:**

```
python satellite-strategy.py
```

**Holdings Assessment & Cost Analysis:** To apply the Rank Stability Rule and calculate precise turnover logic, pass the currently held assets via the `--current` argument:

Bash

```
python satellite-strategy.py --current [TICKER1].XETRA,[TICKER2].XETRA,[TICKER3].XETRA
```

---

---

## 9. Operational Protocol

- **Frequency:** The technical assessment is executed once per month.

- **Data Processing:** The script must be run at the end of the month (Ultimo) to capture the complete monthly data candle accurately. The internal calendar module allows execution within the final 2-3 trading days of the current month.

- **Execution Window:** Necessary portfolio adjustments are executed within the first 5 trading days of the subsequent month.

- **Intra-Month Discipline (No Ad-Hoc Interventions):** The strategy strictly ignores intra-month price volatility. If an asset temporarily breaches its SMA200 during the month, no preemptive action is taken. The algorithm relies exclusively on end-of-month closing prices to filter out market noise and prevent whipsaw losses. Don't let yourself be tempted into anything continuous monitoring or emotional overrides.

- **Hard Stop Execution:** If specific technical entry triggers are utilized but remain unmet, market orders are placed on the close of the 5th trading day to ensure adherence to the algorithmic allocation. Performance chasing beyond this window is prohibited.

---

## 10. References & Data Sources

- **EODHD (End-Of-Day Historical Data):** Financial API providing global historical market data. (https://eodhd.com/)

- **Portfolio Visualizer:** Quantitative tools for historical backtesting and correlation analysis. Note: Correlation does not imply causation. (https://www.portfoliovisualizer.com/)

- **Portfolio Charts:** Asset allocation research and performance visualization. (https://portfoliocharts.com/)

- **North Data:** Corporate registry research for analyzing ETF index constituents. (https://www.northdata.com/)

---

## 11. Financial & Legal Disclaimer

**PLEASE READ CAREFULLY**

This repository, including the investment documentation (`README.md`) and the algorithmic software (`satellite-strategy.py`), is provided exclusively for **educational and personal documentation purposes**.

**No Financial Advice:** The provided material does not constitute financial, investment, legal, or tax advice. The strategy reflects the specific objectives and risk tolerance of myself as a private retail investor.

**Jurisdictional Specificity:** This strategy is optimized strictly for the Austrian tax environment (e.g., Flatex.at, Meldefonds/OeKB requirements, avoidance of 'Ausschüttungsgleiche Erträge' traps). Implementation in alternate jurisdictions may result in severe tax inefficiencies or legal complications.

**Data Accuracy & Software Integrity:** The Python script was developed for private use and is provided "as is" without warranties of any kind. Financial data sourced via API may be subject to delays or inaccuracies. Algorithmic outputs are mathematical derivations, not tailored financial recommendations.

**Capital Risk:** Market investments carry inherent risks, including the potential for total capital loss. Past performance is not indicative of future results. Never invest capital you cannot afford to lose.

**Personal Legacy:** The dedication and philosophical framework within these documents represent a private legacy. Respect regarding the personal nature of the dedication is requested.

**Liability Waiver:** Utilizing any part of this repository is done entirely at your own risk. The author assumes no liability for any financial losses, tax penalties, or damages incurred.

---

**License Strategy:** CC BY-NC-SA 4.0 Andreas Willert

**License Code:** MIT License
