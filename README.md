# GOIL PLC — Annual Report & KPI Analysis (2021–2025)
> Portfolio analysis repository. Findings are based on publicly available company materials and clearly identified assumptions; this is not commissioned client work or an official company report.

**Author:** Caleb Agyemang  
**Portfolio:** [calebagyemang.vercel.app](https://calebagyemang.vercel.app)

## Overview

A multi-year comparative analysis of Ghana Oil Company Limited (GOIL PLC, GHSE: GOIL) annual reports, tracking 8 financial KPIs and scoring disclosure clarity across 6 dimensions from 2021 to 2025.

## Data Sources

| Source | Type | Coverage |
|--------|------|----------|
| GOIL PLC Annual Reports (2021–2025) | Corporate Filing | Full financial statements |
| Ghana Stock Exchange (GHSE) | Regulatory | Listed company filings |
| B&FT Ghana | Financial Media | Investor analysis |
| GOIL Investor Presentations | Corporate | Strategic priorities |

## Key Findings

| Metric | 2021 | 2025 | Change |
|--------|------|------|--------|
| Gross Revenue (GHS B) | 19.20 | 18.55 | -3.4% |
| Profit After Tax (GHS M) | 45.0 | 90.67 | **+101.5%** |
| EPS (GHS) | 0.12 | 0.23 | **+91.7%** |
| Dividend/Share (GHS) | 0.025 | 0.060 | **+140%** |
| Total Assets (GHS B) | 3.85 | 4.95 | +28.6% |

- **Revenue declined** 14.6% from peak (2023) but **PAT grew 66%** — strong cost optimization
- **Dividend policy increasingly shareholder-friendly** — +140% over 5 years
- **Disclosure clarity improved** from 53.3 (2023) to 68.7 (2025)
- **ESG reporting remains weakest** dimension (40/100 in 2025)

## Technical Stack

- Python 3.11
- Pandas, NumPy
- Matplotlib (custom Editorial Precision styling)

## How to Run

```bash
pip install -r requirements.txt
python scripts/analyze_goil_annual.py
```

## Outputs

- `output/goil_revenue_profit.png` — Revenue vs. PAT trend
- `output/goil_dividend_eps.png` — Dividend & EPS growth
- `output/goil_disclosure_clarity.png` — Report quality comparison
- `output/goil_executive_summary.json` — Structured findings

## Methodology

Comparative analysis of GOIL PLC annual reports across 5 years. Financial KPIs extracted from audited statements. Disclosure clarity scored using a rubric assessing completeness, readability, and investor accessibility across 6 dimensions.

## License

MIT
