
SELECT
    a.*,
    b.*
FROM {{ ref('my_first_dbt_model') }} AS a
LEFT JOIN {{ source('mage_phi', 'private_health_gov_data') }} AS b ON 1 = 1
WHERE a.id = 1
