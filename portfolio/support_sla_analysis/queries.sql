-- Support Ticket SLA Quality Monitor
-- All rows are synthetic. SLA values are example assumptions.
CREATE TABLE support_tickets (
    ticket_id VARCHAR(12) PRIMARY KEY,
    created_date DATE NOT NULL,
    priority VARCHAR(10) NOT NULL,
    category VARCHAR(40) NOT NULL,
    channel VARCHAR(20) NOT NULL,
    first_response_hours DECIMAL(6,1) NOT NULL,
    resolution_hours DECIMAL(6,1) NOT NULL,
    sla_hours DECIMAL(6,1) NOT NULL,
    sla_met TINYINT NOT NULL,
    customer_rating TINYINT NOT NULL
);

-- Monthly SLA compliance
SELECT DATE_FORMAT(created_date, '%Y-%m') AS month,
       COUNT(*) AS tickets,
       SUM(sla_met) AS met_sla,
       ROUND(100 * AVG(sla_met), 1) AS sla_rate_pct,
       ROUND(AVG(resolution_hours), 1) AS avg_resolution_hours
FROM support_tickets
GROUP BY DATE_FORMAT(created_date, '%Y-%m')
ORDER BY month;

-- Compare priority level against resolution and customer rating
SELECT priority, COUNT(*) AS tickets,
       ROUND(100 * AVG(sla_met), 1) AS sla_rate_pct,
       ROUND(AVG(resolution_hours), 1) AS avg_resolution_hours,
       ROUND(AVG(customer_rating), 2) AS avg_rating
FROM support_tickets
GROUP BY priority
ORDER BY FIELD(priority, 'High', 'Medium', 'Low');

-- Check calculated SLA flag against target
SELECT COUNT(*) AS inconsistent_sla_flags
FROM support_tickets
WHERE sla_met <> CASE WHEN resolution_hours <= sla_hours THEN 1 ELSE 0 END;
