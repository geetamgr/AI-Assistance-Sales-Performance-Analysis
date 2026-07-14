import sqlite3
import pandas as pd

df = pd.read_csv('data/synthetic_sales_data.csv')
df['returned'] = df['returned'].astype(bool).astype(int)  # SQLite-friendly bool

conn = sqlite3.connect(':memory:')
df.to_sql('sales', conn, index=False)

queries = {
    'q1_revenue_by_region_rep': """
        SELECT region, sales_rep, SUM(net_revenue) AS total_revenue
        FROM sales
        GROUP BY region, sales_rep
        ORDER BY total_revenue DESC;
    """,
    'q2_monthly_revenue_trend': """
        SELECT
            strftime('%Y-%m', order_date) AS month,
            SUM(gross_revenue) AS gross_revenue,
            SUM(net_revenue) AS net_revenue,
            SUM(gross_revenue) - SUM(net_revenue) AS discount_amount
        FROM sales
        GROUP BY month
        ORDER BY month;
    """,
    'q3_margin_by_product': """
        SELECT
            category, product,
            AVG(discount_pct) AS avg_discount,
            SUM(gross_revenue) AS gross_revenue,
            SUM(net_revenue) AS net_revenue
        FROM sales
        GROUP BY category, product
        ORDER BY avg_discount DESC;
    """,
    'q4_channel_comparison': """
        SELECT
            channel,
            COUNT(*) AS num_orders,
            AVG(discount_pct) AS avg_discount,
            SUM(net_revenue) AS total_net_revenue
        FROM sales
        GROUP BY channel
        ORDER BY total_net_revenue DESC;
    """,
    'q5_return_rate': """
        SELECT category, region, channel,
            COUNT(*) AS total_orders,
            SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) AS returned_orders,
            ROUND(100.0 * SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS return_rate_pct
        FROM sales
        GROUP BY category, region, channel
        ORDER BY return_rate_pct DESC;
    """
}

results = {}
for name, q in queries.items():
    res = pd.read_sql_query(q, conn)
    results[name] = res
    res.to_csv(f'results/{name}.csv', index=False)
    print(f"--- {name} ({len(res)} rows) ---")
    print(res.head(5).to_string())
    print()

# Validation checks against source data
total_net = df['net_revenue'].sum()
q1_total = results['q1_revenue_by_region_rep']['total_revenue'].sum()
q2_total = results['q2_monthly_revenue_trend']['net_revenue'].sum()
q4_total = results['q4_channel_comparison']['total_net_revenue'].sum()
print("VALIDATION")
print("source total net_revenue:", round(total_net,2))
print("q1 total matches:", abs(q1_total - total_net) < 0.01)
print("q2 total matches:", abs(q2_total - total_net) < 0.01)
print("q4 total matches:", abs(q4_total - total_net) < 0.01)
print("q4 order count matches source rows:", results['q4_channel_comparison']['num_orders'].sum() == len(df))
print("q5 order count matches source rows:", results['q5_return_rate']['total_orders'].sum() == len(df))
