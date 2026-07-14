-- Sales Performance Analysis: 5 stakeholder questions
-- Table: sales  (loaded from data/synthetic_sales_data.csv)

-- 1. Revenue by region and sales rep
SELECT region, sales_rep, SUM(net_revenue) AS total_revenue
FROM sales
GROUP BY region, sales_rep
ORDER BY total_revenue DESC;

-- 2. Monthly revenue trend (gross vs net, to see discount impact)
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(gross_revenue) AS gross_revenue,
    SUM(net_revenue) AS net_revenue,
    SUM(gross_revenue) - SUM(net_revenue) AS discount_amount
FROM sales
GROUP BY month
ORDER BY month;

-- 3. Margin (discount impact) by product/category
SELECT
    category,
    product,
    AVG(discount_pct) AS avg_discount,
    SUM(gross_revenue) AS gross_revenue,
    SUM(net_revenue) AS net_revenue
FROM sales
GROUP BY category, product
ORDER BY avg_discount DESC;

-- 4. Channel comparison: revenue vs discount level
SELECT
    channel,
    COUNT(*) AS num_orders,
    AVG(discount_pct) AS avg_discount,
    SUM(net_revenue) AS total_net_revenue
FROM sales
GROUP BY channel
ORDER BY total_net_revenue DESC;

-- 5. Return rate by category, region, and channel
SELECT category, region, channel,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) AS returned_orders,
    ROUND(100.0 * SUM(CASE WHEN returned = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS return_rate_pct
FROM sales
GROUP BY category, region, channel
ORDER BY return_rate_pct DESC;
