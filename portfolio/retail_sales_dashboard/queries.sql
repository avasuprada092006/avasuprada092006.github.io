-- Retail Revenue & Margin Explorer
-- All rows come from the included synthetic sample, not real business records.
CREATE TABLE retail_orders (
    order_id VARCHAR(12) PRIMARY KEY,
    order_date DATE NOT NULL,
    region VARCHAR(20) NOT NULL,
    category VARCHAR(30) NOT NULL,
    product VARCHAR(60) NOT NULL,
    quantity INT NOT NULL,
    unit_price_inr DECIMAL(12,2) NOT NULL,
    discount_pct DECIMAL(5,2) NOT NULL,
    revenue_inr DECIMAL(12,2) NOT NULL,
    cost_inr DECIMAL(12,2) NOT NULL,
    profit_inr DECIMAL(12,2) NOT NULL
);

-- Monthly revenue and gross profit
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       SUM(revenue_inr) AS revenue_inr,
       SUM(profit_inr) AS profit_inr,
       ROUND(100 * SUM(profit_inr) / NULLIF(SUM(revenue_inr), 0), 1) AS margin_pct
FROM retail_orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;

-- Category and region comparison
SELECT category, region, COUNT(*) AS order_lines,
       SUM(revenue_inr) AS revenue_inr,
       SUM(profit_inr) AS profit_inr
FROM retail_orders
GROUP BY category, region
ORDER BY revenue_inr DESC;

-- Basic data quality check
SELECT COUNT(*) AS invalid_rows
FROM retail_orders
WHERE quantity <= 0 OR revenue_inr < 0 OR cost_inr < 0
   OR profit_inr <> ROUND(revenue_inr - cost_inr, 2);
