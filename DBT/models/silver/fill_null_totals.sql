WITH fill_null_totals AS (
  SELECT
    t.concepto_turistico,
    t.comunidades_y_ciudades_autonomas,
    t.residencia_del_viajero,
    t.mes,
    t.anio,
    AVG(CASE
      WHEN d.concepto_turistico = t.concepto_turistico
        AND d.comunidades_y_ciudades_autonomas = t.comunidades_y_ciudades_autonomas
        AND d.residencia_del_viajero = t.residencia_del_viajero
        AND d.mes = t.mes
        AND d.anio = t.anio
        AND d.total IS NOT NULL THEN d.total
    END) AS total
  FROM {{ ref("extract_year_month") }} t
  LEFT JOIN {{ ref("extract_year_month") }} d ON (
    t.concepto_turistico = d.concepto_turistico
    AND t.comunidades_y_ciudades_autonomas = d.comunidades_y_ciudades_autonomas
    AND t.residencia_del_viajero = d.residencia_del_viajero
    AND t.mes = d.mes
    AND t.anio = d.anio
  )
  GROUP BY t.concepto_turistico, t.comunidades_y_ciudades_autonomas, t.residencia_del_viajero, t.mes, t.anio
)
SELECT concepto_turistico, comunidades_y_ciudades_autonomas, residencia_del_viajero, mes, anio, total
FROM fill_null_totals
WHERE total IS NOT NULL