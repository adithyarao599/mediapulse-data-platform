SELECT

    SUM(revenue) AS total_revenue,

    SUM(views) AS total_views,

    SUM(streams) AS total_streams,

    AVG(engagement_score) AS average_engagement

FROM fact_content_performance;
