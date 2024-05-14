SELECT
    comunidades_y_ciudades_autonomas,
    mes,
    anio,
    residencia_del_viajero,
    MAX(CASE WHEN concepto_turistico = 'Número de alojamientos turísticos ocupados' THEN total END) AS alojamientos_ocupados,
    MAX(CASE WHEN concepto_turistico = 'Número de noches ocupadas' THEN total END) AS noches_ocupadas,
    MAX(CASE WHEN concepto_turistico = 'Estancia media' THEN total END) AS estancia_media
FROM {{ ref("fill_null_totals") }}
GROUP BY comunidades_y_ciudades_autonomas, mes, anio, residencia_del_viajero