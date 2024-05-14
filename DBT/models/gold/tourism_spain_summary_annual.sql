SELECT
    comunidades_y_ciudades_autonomas,
    anio,
    residencia_del_viajero,
    AVG(alojamientos_ocupados) AS alojamientos_ocupados_total,
    AVG(noches_ocupadas) AS noches_ocupadas_total,
    AVG(estancia_media) AS estancia_media_promedio
FROM {{ ref("tourism_spain_slvr") }}
GROUP BY comunidades_y_ciudades_autonomas, anio, residencia_del_viajero