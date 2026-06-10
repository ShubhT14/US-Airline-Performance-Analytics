# US Airline Performance Analytics
### COVID-19 Impact Analysis — 45 Million Flight Records (2019–2025)

![Executive Summary](Executive%20Summary.png)

## Project Question
**"Which airlines and airports cost passengers the most time — and is delay 
performance getting better or worse post-COVID?"**

## Dataset
- **Source:** US Bureau of Transportation Statistics (BTS)
- **Size:** 45.7 million flight records
- **Period:** January 2019 — 2025
- **Files:** 84 monthly CSV files combined via Python

## What I Built

### Data Pipeline
- Downloaded 84 monthly CSV files from BTS using Python
- Combined into single 45M row dataset
- Built complete ETL pipeline in Power Query (M code)
- Extracted dimension tables from raw source

### Data Model — Star Schema
- `Fact_Flights` — 45M rows, 20 columns
- `Dim_Airline` — 19 airlines with full names
- `Dim_Airport` — 400+ US airports with city and state
- `Dim_Date` — 2019–2025 with COVID period classification
- `Dim_DelayType` — 7 delay cause categories
- 5 relationships configured in Power BI Model View

### DAX Measures (12 total)
- Total Flights, Total Delayed, On Time Rate %
- Delay Rate %, Cancellation Rate %, Avg Arrival Delay
- Weather Delay Flights, Carrier Delay Flights
- Total Flights LY (SAMEPERIODLASTYEAR)
- YoY Flight Volume %, COVID Recovery Index

### Dashboard — 3 Pages
**Page 1 — Executive Summary**
![Executive Summary](Executive%20Summary.png)

**Page 2 — Airport & Route Performance**
![Airport Performance](Airport%20Performance.png)

**Page 3 — COVID Impact Analysis**
![COVID Impact](Covid%20Impact.png)

## Key Insights

### COVID Impact
- April 2020: **-63% flight volume** vs April 2019 — most dramatic single month drop
- 2020 full year: **-37% total flights** (7.4M → 4.7M)
- Full recovery achieved by **2024** — back to pre-COVID levels

### Delay Performance
- Overall on-time rate: **81.9%** across 45M flights
- **COVID Collapse period had LOWEST delay rate (9%)** — airlines only flew reliable routes
- Post-COVID "New Normal" has HIGHEST delays (20%) — demand surged faster than capacity

### Airline Rankings
- **Best on-time:** Delta Air Lines (85.3% overall)
- **Worst on-time:** Frontier Airlines (74.5% overall)
- **ExpressJet ceased operations Sept 2020** — visible in data as blank cells post-2020

### Airport Intelligence
- **Busiest:** Atlanta (ATL) — world's busiest airport confirmed
- **Most cancellations:** LaGuardia (LGA) — Northeast weather impact
- **Most delays:** Orlando (MCO) — surprising finding for a vacation hub

## Tools & Skills
- **Python** — bulk data download (84 files), initial pipeline
- **Power Query (M code)** — ETL, dimension extraction, data cleaning
- **DAX** — 12 measures including time intelligence
- **Power BI** — Star Schema modelling, relationships, dashboard design
- **Star Schema** — Fact + 4 dimension tables, 5 relationships
- **GitHub** — version control and portfolio documentation

## Files
- `download_flights.py` — Python script to download all 84 BTS files
- `Airline_Analysis.pbix` — Power BI file (available on request)
