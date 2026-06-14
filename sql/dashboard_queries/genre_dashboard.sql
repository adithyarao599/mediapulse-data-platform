SELECT

    genre_name,

    SUM(revenue) AS total_revenue,

    SUM(streams) AS total_streams,

    AVG(engagement_score) AS engagement

FROM fact_content_performance fp

JOIN dim_genre dg

ON fp.genre_key = dg.genre_key

GROUP BY genre_name

ORDER BY total_revenue DESC;
