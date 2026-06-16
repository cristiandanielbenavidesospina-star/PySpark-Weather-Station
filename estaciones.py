from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Importar la librería Folium
import folium

# Crear la sesión de Spark
spark = SparkSession.builder.appName("Prueba").getOrCreate()

# Definir las columnas a utilizar
columnas_df = ["USAF", "WBAN", "STATION_NAME", "CTRY", "ST", "CALL", "LAT", "LON", "ELEV", "BEGIN", "END"]

# Leer el archivo CSV
archivo = spark.read.csv('/home/enfasis3/Descargas/isd-history.csv', header=True)

# Renombrar las columnas
archivo = archivo.toDF(*columnas_df)

# Seleccionar las columnas de interés y filtrar por el país ingresado
pais = input('Ingrese el código del país: ')

m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

#query = archivo.select(col('CTRY'), col('LAT'), col('LON')).filter(archivo['CTRY'] == pais)
query = archivo.filter(archivo["CTRY"] == pais).filter(archivo["LAT"].isNotNull()).filter(archivo["LON"].isNotNull())
for row in query.collect():
    lat = row["LAT"]
    lon = row["LON"]
    folium.Marker (location=[lat, lon]).add_to(m)

# Mostrar el mapa en el navegador
m.save('mapa.html')
import webbrowser
webbrowser.open_new_tab('mapa.html')
