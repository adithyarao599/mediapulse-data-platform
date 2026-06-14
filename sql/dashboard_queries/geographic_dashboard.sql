SELECT

    country_name,

    SUM(views) AS total_views,

    SUM(revenue) AS total_revenue,

    SUM(streams) AS total_streams

FROM fact_content_performance fp

JOIN dim_country dc

ON fp.country_key = dc.country_key

GROUP BY country_name;
