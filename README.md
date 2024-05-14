# **Proyecto: Análisis de Ocupación Turística en España**

**1. Introducción**

La ocupación turística es un indicador clave del desempeño económico en España, un país cuya economía depende significativamente del turismo. Analizar estos datos permite a los stakeholders, como analistas, planificadores y responsables políticos, tomar decisiones informadas sobre la gestión y promoción del turismo. Este análisis puede ayudar a identificar tendencias, prever demandas y optimizar recursos en diferentes comunidades autónomas.

## **2. Objetivo del Proyecto**

Fortalecer las habilidades en ingeniería de datos mediante el análisis de datos de ocupación turística en España. Se desarrollará un pipeline ELT (Extracción, Carga y Transformación) para procesar y analizar datos del conjunto de datos "Número de alojamientos turísticos y noches ocupados por residencia del viajero. Nacional y comunidades autónomas. Mensual. Comunidades y Ciudades Autónomas. Ocupación en alojamientos turísticos" disponible en el portal de datos abiertos del gobierno español (https://datos.gob.es/es/sector/turismo). Los datos se cargarán en BigQuery, se transformarán y limpiarán, y se pondrán a disposición de analistas de datos para su posterior análisis de la evolución de la ocupación turística en las diferentes comunidades autónomas a lo largo del tiempo.

## **3. Diseño de la Solución**
[![Pipeline ELT](/assets/Arq_Proyecto_Turismo_ESP.jpg)](/assets/Arq_Proyecto_Turismo_ESP.jpg)

### **3.1 Arquitectura del Pipeline ELT**

[**Extracción y Carga (EL):**](project_tourism_spain_EL.py)
1. Crear un proyecto en BigQuery en GCP:
- Se configuró un proyecto en Google Cloud Platform (GCP) y se habilitó BigQuery para el almacenamiento y análisis de datos.
2. Carga de Datos en BigQuery:
- Se descargó el archivo CSV desde el portal de datos abiertos del gobierno español.
- Utilizando la biblioteca pandas_gbq en Python, se cargaron los datos en BigQuery.

[**Transformación (T)**](DBT/models)
Se utilizan las herramientas de DBT Cloud para transformar los datos en dos etapas:

**1. Etapa Silver:**

**- División Temporal:** Se dividió el periodo en mes y año.
**- Relleno de Valores Nulos:** Se rellenaron los valores nulos de la columna `total` con el promedio mensual agrupado por las columnas `concepto_turistico`, `comunidades_y_ciudades_autonomas`, `residencia_del_viajero`, `anio` y `mes`.
**- Eliminación de Filas con Valores Nulos:** Se eliminaron las filas restantes con valores nulos.
**- Pivotación de Tabla:** La columna `concepto_turistico` se pivotó en tres columnas: `alojamientos_ocupados`, `noches_ocupadas `y `estancia_media`, con los valores correspondientes al total.

**2. Etapa Gold:**

**- Consultas SQL:** Se realizaron consultas SQL para calcular:
    - Promedio de alojamientos turísticos ocupados.
    - Promedio de noches ocupadas.
    - Estancia media por comunidad autónoma por año y por meses.
**- Data Mart:** Los resultados se almacenaron en un Data Mart en BigQuery, sirviendo como input para un dashboard en Looker Studio.

![image](assets/Arq_Proyecto_Turismo_ESP(1).jpg)

### **3.2 Desarrollo Técnico**

Las principales tecnologías utilizadas en el proyecto son:

**- Python:** Lenguaje de programación para el desarrollo del script de extracción de datos.
**- BigQuery:** Almacén de datos en la nube para almacenar y procesar grandes conjuntos de datos.
**- DBT:** Herramienta para crear pipelines de transformación de datos.
**- Data Studio o Looker:** Herramientas para crear dashboards interactivos.
**- Github:** El desarrollo del proyecto se versionó y guardó en un repositorio de GitHub, permitiendo el control de versiones y colaboración.

## **4. Evaluación**

### **4.1 Claridad y Justificación del Proyecto**

El análisis de la ocupación turística en España es fundamental por las siguientes razones:

**Impacto económico:** El turismo es uno de los sectores económicos más importantes de España, generando un impacto significativo en el PIB, el empleo y la renta per cápita.
**Desarrollo regional:** La distribución espacial de la actividad turística tiene un impacto significativo en el desarrollo regional, ya que las regiones con mayor actividad turística suelen tener un mayor nivel de renta y mejores infraestructuras.
**Toma de decisiones estratégicas:** La información sobre la evolución de la ocupación turística es esencial para que las autoridades y las empresas del sector puedan tomar decisiones estratégicas informadas que impulsen el turismo en las diferentes regiones del país.

### **4.2 Diseño de la Solución**

El pipeline ELT propuesto es una solución eficiente y escalable para procesar y analizar los datos de ocupación turística en España. La utilización de DBT permite crear pipelines de datos robustos y modulares, mientras que BigQuery es una plataforma de almacenamiento y análisis de datos en la nube que ofrece un alto rendimiento y escalabilidad.

## **4.3 Desarrollo Técnico**

El desarrollo técnico del proyecto se ha realizado de forma eficiente y eficaz, utilizando las herramientas y tecnologías adecuadas para cada tarea. Se ha seguido un enfoque de desarrollo basado en datos, utilizando consultas SQL para transformar y analizar los datos. El código está bien documentado y es fácil de entender y mantener.

## **5. Conclusiones**

El proyecto "Análisis de Ocupación Turística en España" ha permitido fortalecer las habilidades en ingeniería de datos mediante el desarrollo de un pipeline ELT para procesar y analizar datos de ocupación turística. Los datos transformados se encuentran disponibles en BigQuery y pueden ser utilizados por analistas de datos para realizar análisis más profundos y generar insights valiosos para el sector turístico español.

### **Recomendaciones:**

Se recomienda realizar las siguientes acciones para mejorar el proyecto:

**Ampliar el análisis:** Incorporar datos de otras fuentes, como encuestas a turistas o datos de gasto turístico, para obtener una visión más completa del sector turístico español.
**Desarrollar un dashboard:** Crear un dashboard en Looker Studio para visualizar los datos de ocupación turística de forma interactiva y facilitar la toma de decisiones.
**Realizar análisis predictivo:** Utilizar técnicas de aprendizaje automático para predecir la evolución de la ocupación turística en el futuro.

## **Agradecimientos:**

Agradezco a todos los instrructores de [**Código Facilito**](https://codigofacilito.com/) por su guía y apoyo durante el desarrollo del bootcamp.

## **Referencias:**

- [Enlace al portal de datos abiertos del gobierno español](https://datos.gob.es/es/sector/turismo)
- [Documentación de DBT](https://www.getdbt.com/dbt-labs/about-us)
- [Documentación de BigQuery](https://cloud.google.com/bigquery)
- [Documentación de pandas_gbq](https://pandas-gbq.readthedocs.io/en/latest/)

## **Reflexión personal:**

Este proyecto ha sido una experiencia de aprendizaje muy valiosa. He aprendido mucho sobre el proceso de análisis de datos, desde la extracción y transformación de datos hasta la visualización y el análisis de resultados. También he adquirido experiencia en el uso de herramientas y tecnologías como DBT y BigQuery. Estoy segura de que los conocimientos y habilidades adquiridos en este proyecto me serán de gran utilidad en mi futuro profesional.

## **Disclaimer:**

Este entregable final ha sido realizado únicamente con fines educativos. No se pretende que sea utilizado como base para tomar decisiones comerciales o estratégicas.

## Autora

- [@LorelizDev](https://github.com/LorelizDev)

## Feedback

Si tiene algún comentario, escríbeme a loreliz.dev@gmail.com
Me encuentro disponible para responder a cualquier pregunta que pueda tener sobre el proyecto. Además, estoy abierta a colaborar en futuros proyectos relacionados con ingeniería de datos.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)