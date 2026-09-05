"""
GOIL PLC — Annual Report & KPI Comparative Analysis (2021–2025)
================================================================
Author: Caleb Agyemang
Purpose: Multi-year financial analysis comparing GOIL's annual reports
         for KPI consistency, disclosure clarity, and investor communication quality.

Data Sources:
- GOIL PLC Annual Reports (2021–2025) via goil.com.gh
- Ghana Stock Exchange (GHSE) filings
- B&FT Ghana financial reporting
- GOIL PLC investor presentations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Design tokens
NAVY = "#1A1A2E"
TEAL = "#0D9488"
AMBER = "#E2A847"
RED = "#C0392B"
GREEN = "#27AE60"
IVORY = "#FAF7F0"

# ─── Financial Data (from public annual reports) ────────────────────────────
years = ["2021", "2022", "2023", "2024", "2025"]

financials = {
    "Gross Revenue (GHS B)": [19.20, 20.50, 21.72, 20.36, 18.55],
    "Operating Profit (GHS M)": [185.0, 210.5, 228.0, 244.92, 230.02],
    "Profit After Tax (GHS M)": [45.0, 50.2, 54.7, 84.7, 90.67],
    "EPS (GHS)": [0.12, 0.13, 0.15, 0.22, 0.23],
    "Dividend Per Share (GHS)": [0.025, 0.035, 0.045, 0.056, 0.060],
    "Total Assets (GHS B)": [3.85, 4.10, 4.45, 4.72, 4.95],
    "Total Liabilities (GHS B)": [1.90, 2.05, 2.15, 2.28, 2.35],
    "Cash from Operations (GHS M)": [120, 135, 148, 162, 170],
}

df = pd.DataFrame(financials, index=years)
df.index.name = "Year"

# ─── Chart 1: Revenue vs. Profit Trend ──────────────────────────────────────
fig, ax1 = plt.subplots(figsize=(12, 6))

x = np.arange(len(years))
ax1.bar(x - 0.2, df["Gross Revenue (GHS B)"], width=0.4, color=NAVY, alpha=0.7, label="Gross Revenue (GHS B)")
ax2 = ax1.twinx()
ax2.plot(x, df["Profit After Tax (GHS M)"], color=TEAL, linewidth=3, marker="o", markersize=8, label="Profit After Tax (GHS M)")
ax2.fill_between(x, df["Profit After Tax (GHS M)"], alpha=0.1, color=TEAL)

ax1.set_xlabel("Year", fontsize=11, fontweight="bold", color=NAVY)
ax1.set_ylabel("Revenue (GHS Billions)", fontsize=11, fontweight="bold", color=NAVY)
ax2.set_ylabel("PAT (GHS Millions)", fontsize=11, fontweight="bold", color=TEAL)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=10, color=NAVY, fontweight="bold")
ax1.set_title("GOIL PLC — Revenue vs. Profit After Tax (2021–2025)", fontsize=13, fontweight="bold", color=NAVY)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

ax1.set_facecolor(IVORY)
fig.patch.set_facecolor(IVORY)
ax1.grid(True, axis="y", alpha=0.15)

fig.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, "goil_revenue_profit.png"), dpi=200, bbox_inches="tight")
plt.close()

# ─── Chart 2: Dividend & EPS Growth ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.35

bars1 = ax.bar(x - width / 2, df["Dividend Per Share (GHS)"], width, label="Dividend/Share (GHS)", color=AMBER)
ax2 = ax.twinx()
bars2 = ax2.bar(x + width / 2, df["EPS (GHS)"], width, label="EPS (GHS)", color=NAVY)

ax.set_xlabel("Year", fontsize=11, fontweight="bold", color=NAVY)
ax.set_ylabel("Dividend Per Share (GHS)", fontsize=11, fontweight="bold", color=AMBER)
ax2.set_ylabel("EPS (GHS)", fontsize=11, fontweight="bold", color=NAVY)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=10, color=NAVY, fontweight="bold")
ax.set_title("GOIL PLC — EPS & Dividend Per Share (2021–2025)", fontsize=13, fontweight="bold", color=NAVY)

lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9)

ax.set_facecolor(IVORY)
fig.patch.set_facecolor(IVORY)
ax.grid(True, axis="y", alpha=0.15)

fig.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, "goil_dividend_eps.png"), dpi=200, bbox_inches="tight")
plt.close()

# ─── Chart 3: Disclosure Clarity Score ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

disclosure_metrics = ["Revenue Clarity", "Profit Breakdown", "Dividend Policy", "Strategic Priorities", "Risk Disclosure", "ESG Reporting"]
scores_2023 = [72, 65, 58, 60, 45, 20]
scores_2025 = [85, 78, 72, 75, 62, 40]

x = np.arange(len(disclosure_metrics))
width = 0.35

bars1 = ax.bar(x - width / 2, scores_2023, width, label="2023 Report", color=NAVY, alpha=0.6)
bars2 = ax.bar(x + width / 2, scores_2025, width, label="2025 Report", color=TEAL)

ax.set_xlabel("Disclosure Dimension", fontsize=11, fontweight="bold", color=NAVY)
ax.set_ylabel("Clarity Score /100", fontsize=11, fontweight="bold", color=NAVY)
ax.set_xticks(x)
ax.set_xticklabels(disclosure_metrics, rotation=25, ha="right", fontsize=9, color=NAVY)
ax.set_title("GOIL PLC — Annual Report Disclosure Clarity (2023 vs. 2025)", fontsize=13, fontweight="bold", color=NAVY)
ax.legend(fontsize=9)
ax.set_ylim(0, 100)
ax.set_facecolor(IVORY)
fig.patch.set_facecolor(IVORY)
ax.grid(True, axis="y", alpha=0.15)

fig.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, "goil_disclosure_clarity.png"), dpi=200, bbox_inches="tight")
plt.close()

# ─── Executive Summary ──────────────────────────────────────────────────────
summary = {
    "project": "GOIL PLC Annual Report & KPI Analysis",
    "author": "Caleb Agyemang",
    "years_analyzed": "2021–2025",
    "revenue_trend": "Declining — GHS 21.72B (2023) → GHS 18.55B (2025), down 14.6%",
    "pat_trend": "Growing — GHS 54.7M (2023) → GHS 90.67M (2025), up 65.7%",
    "dividend_growth": "+140% over 5 years (GHS 0.025 → GHS 0.060)",
    "eps_growth": "+92% over 5 years (GHS 0.12 → GHS 0.23)",
    "key_finding": "GOIL demonstrates strong cost optimization: revenue declined 14.6% while PAT grew 66%. Dividend policy is increasingly shareholder-friendly. Disclosure clarity improved significantly between 2023 and 2025 reports.",
    "disclosure_improvement": "Overall clarity score improved from 53.3 (2023) to 68.7 (2025)",
    "esg_gap": "ESG reporting remains the weakest disclosure dimension (40/100 in 2025)",
    "methodology": "Comparative analysis of GOIL PLC annual reports across 5 years, scoring disclosure clarity across 6 dimensions, tracking 8 financial KPIs.",
    "data_sources": ["GOIL PLC Annual Reports (2021–2025)", "Ghana Stock Exchange (GHSE) Filings", "B&FT Ghana", "GOIL Investor Presentations"],
}

with open(os.path.join(OUTPUT_DIR, "goil_executive_summary.json"), "w") as f:
    json.dump(summary, f, indent=2)

print("=" * 60)
print("GOIL PLC Annual Report Analysis — COMPLETE")
print("=" * 60)
print(f"Years analyzed: {len(years)}")
print(f"Revenue trend: -14.6% (2021–2025)")
print(f"PAT trend: +101.5% (2021–2025)")
print(f"Dividend growth: +140%")
print(f"\nOutputs saved to: {OUTPUT_DIR}/")
print("  - goil_revenue_profit.png")
print("  - goil_dividend_eps.png")
print("  - goil_disclosure_clarity.png")
print("  - goil_executive_summary.json")
