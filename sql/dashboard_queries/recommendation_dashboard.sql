SELECT

    content_name,

    recommendation_score,

    trend_score,

    engagement_score

FROM recommendation_gold

ORDER BY recommendation_score DESC;
