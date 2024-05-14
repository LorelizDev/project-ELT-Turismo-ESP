SELECT
    comunidades_y_ciudades_autonomas,
    concepto_turistico,
    residencia_del_viajero,
    EXTRACT(MONTH FROM periodo) AS mes,
    EXTRACT(YEAR FROM periodo) AS anio,
    total
FROM {{ source("raw", "tourism_spain_raw") }}