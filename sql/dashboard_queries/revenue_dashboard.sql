SELECT

    content_name,

    platform_name,

    revenue,

    views,

    (

        revenue

        /

        NULLIF(
            views,
            0
        )

    ) * 1000 AS rpm

FROM fact_content_performance fp

JOIN dim_content dc

ON fp.content_key = dc.content_key

JOIN dim_platform dp

ON fp.platform_key = dp.platform_key;
