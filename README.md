# 📊 Análisis Automatizado de la Premier League

## 📝 Descripción
Este proyecto es un script de **ETL (Extracción, Transformación y Carga)** que automatiza la obtención de datos de fútbol.
El programa se conecta a Wikipedia, extrae la clasificación actual de la Premier League, limpia los datos y genera visualizaciones automáticas para el análisis deportivo.

## 🛠️ Tecnologías Usadas
* **Python 3.13**
* **Pandas:** Para la manipulación y limpieza de datos (Data Cleaning).
* **Matplotlib:** Para la generación de gráficos de barras.
* **Requests & BeautifulSoup:** Para Web Scraping y peticiones HTTP.
* **Git & GitHub:** Para el control de versiones.

## 🚀 Cómo funciona
1.  El script `proyecto_premier.py` realiza una petición HTTP disfrazada (User-Agent).
2.  Localiza las tablas HTML dentro del código de la web.
3.  Convierte los datos a numéricos y filtra el TOP 5.
4.  Exporta un CSV y genera un gráfico comparativo de puntos.

## 📈 Resultados
El script genera automáticamente informes sobre el rendimiento del Manchester City, Arsenal, Liverpool, etc.

---
*Proyecto realizado por [Christian NM] como parte de formación en Análisis de Datos Deportivos.*