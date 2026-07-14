# Sales Performance Analysis

A synthetic retail sales dataset with a full analysis pipeline: SQL queries, Python charts, a dashboard, and an executive summary — built to demonstrate a sales performance analysis workflow end to end.

> **Note:** the dataset is synthetic (randomly generated), not real sales data. It's designed to look and behave like a realistic retail dataset (seasonality, discount patterns, returns, channel mix).

## Project Structure

```
sales-performance-analysis/
├── data/
│   └── synthetic_sales_data.csv       # 8,000 rows, 15 columns, Jul 2024 - Jun 2026
├── sql/
│   └── queries.sql                    # the 5 stakeholder queries
├── run_queries.py                     # runs queries.sql against the CSV (via SQLite) + validates totals
├── results/                           # query outputs, one CSV per query
│   ├── q1_revenue_by_region_rep.csv
│   ├── q2_monthly_revenue_trend.csv
│   ├── q3_margin_by_product.csv
│   ├── q4_channel_comparison.csv
│   └── q5_return_rate.csv
├── make_charts.py                     # generates the 5 charts from results/
├── charts/                            # PNG charts, one per query
├── dashboard/
│   └── dashboard.html                 # single-file interactive dashboard (KPIs + charts)
├── screenshots/                       # preview images for documentation
│   ├── sql_output.png
│   ├── python_chart.png
│   ├── dashboard.png
│   └── executive_summary.png
├── EXECUTIVE_SUMMARY.md               # stakeholder-facing findings and recommendations
└── README.md
```

## Dataset

`data/synthetic_sales_data.csv` — 8,000 orders, 15 columns:

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `order_date` | Transaction date (2024-07-01 to 2026-06-30) |
| `customer_id` | Customer identifier (repeat customers included) |
| `customer_segment` | Consumer / Small Business / Enterprise |
| `region` | North / South / East / West / Central |
| `sales_rep` | Rep name (3 per region) |
| `channel` | Online / In-Store / Marketplace / Wholesale |
| `category` | Electronics / Home & Kitchen / Apparel / Office Supplies / Beauty |
| `product` | One of 25 specific products (5 per category) |
| `unit_price` | Price per unit |
| `units_sold` | Quantity in the order |
| `discount_pct` | Discount rate applied, as a decimal (0.15 = 15% off) |
| `gross_revenue` | `unit_price × units_sold` |
| `net_revenue` | `gross_revenue × (1 − discount_pct)` |
| `returned` | Whether the order was returned (~6% of orders) |

## The 5 Business Questions

1. Which regions/reps drive the most revenue?
2. How does revenue trend month over month, and how much of the holiday spike is discount-driven?
3. Which categories/products carry the highest effective discount rate?
4. How do channels compare on revenue vs. discounting?
5. What's the return rate by category, region, and channel?

Full SQL is in `sql/queries.sql`.

## How to Reproduce

```bash
pip install pandas matplotlib pillow

# 1. Run the 5 SQL queries against the dataset and validate totals
python3 run_queries.py

# 2. Generate charts from the query results
python3 make_charts.py

# 3. Open the dashboard
open dashboard/dashboard.html
```

`run_queries.py` validates that each query's totals reconcile exactly against the source CSV (revenue sums, order counts) before writing results to `results/`.

## Screenshots

**SQL query output**
![SQL output](screenshots/sql_output.png)

**Python chart (monthly revenue trend)**
![Python chart](screenshots/python_chart.png)

**Dashboard**
![Dashboard](screenshots/dashboard.png)

**Executive summary**
![Executive summary](screenshots/executive_summary.png)

## Key Findings (short version)

East region and the Online channel lead performance; Central region and Wholesale channel lag on both revenue and return rate. December revenue is the highest of the year but also the most heavily discounted. Full detail and recommendations: [`EXECUTIVE_SUMMARY.md`](EXECUTIVE_SUMMARY.md).
