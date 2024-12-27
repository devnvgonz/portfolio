CREATE TABLE weekly_analytics (
    week_start_date DATE,
    sessions INT,
    pageviews INT,
    users INT,
    bounce_rate FLOAT,
    conversion_rate FLOAT
)

-- Métricas WoW
SELECT
    week_start_date,
    sessions,
    LAG(sessions) OVER (ORDER BY week_start_date) AS prev_sessions,
    ((sessions - LAG(sessions) OVER (ORDER BY week_start_date)) / LAG(sessions) OVER (ORDER BY week_start_date)) * 100 AS session_change_pct
FROM weekly_analytics
