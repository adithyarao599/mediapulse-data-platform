SELECT

    artist_name,

    SUM(streams) AS total_streams,

    SUM(revenue) AS total_revenue,

    AVG(engagement_score) AS average_engagement

FROM fact_content_performance fp

JOIN dim_artist da

ON fp.artist_key = da.artist_key

GROUP BY artist_name

ORDER BY total_streams DESC;
