# PySpark Weather Station Data Processing & Visualization

## Overview

This project demonstrates the use of **Apache Spark (PySpark)** for processing large-scale meteorological station datasets and visualizing geospatial information through an interactive map.

Using weather station metadata from the Integrated Surface Database (ISD), the application filters stations by country, processes the data using Spark DataFrames, and generates an interactive map displaying all available weather stations for the selected country.

The project was developed as part of coursework focused on **Linux environments, distributed data processing, and scalable data analytics workflows**.

---

## Features

* Load and process weather station datasets using PySpark
* Filter stations dynamically by country code
* Handle missing geographic coordinates
* Generate interactive maps using Folium
* Visualize weather station locations with map markers
* Run in a Linux-based environment using Apache Spark

---

## Technologies Used

* Python
* Apache Spark (PySpark)
* Folium
* Linux
* CSV Data Processing

---

## Dataset

The project uses the `isd-history.csv` dataset, which contains metadata for weather stations worldwide, including:

* Station ID
* Country Code
* Station Name
* Latitude
* Longitude
* Elevation
* Operational Dates

Example fields:

| Column       | Description          |
| ------------ | -------------------- |
| USAF         | Station Identifier   |
| STATION_NAME | Weather Station Name |
| CTRY         | Country Code         |
| LAT          | Latitude             |
| LON          | Longitude            |
| ELEV         | Elevation            |
| BEGIN        | Start Date           |
| END          | End Date             |

---

## Architecture

```text
CSV Dataset
      │
      ▼
PySpark DataFrame
      │
      ▼
Country Filtering
      │
      ▼
Coordinate Validation
      │
      ▼
Folium Map Generation
      │
      ▼
Interactive HTML Map
```

---

## How It Works

1. Create a Spark session.
2. Load the weather station dataset into a Spark DataFrame.
3. Rename columns for easier processing.
4. Request a country code from the user.
5. Filter weather stations belonging to that country.
6. Remove records with missing coordinates.
7. Create map markers for each station.
8. Generate an interactive HTML map.
9. Automatically open the map in a web browser.

---

## Example Usage

```bash
$ python weather_stations.py

Enter country code: CO
```

Output:

```text
mapa.html
```

An interactive map is generated displaying all available weather stations located in Colombia.

---

## Skills Demonstrated

* Distributed data processing with PySpark
* Data filtering and transformation
* Data quality validation
* Geospatial data visualization
* Linux-based development
* Scalable dataset handling
* Data engineering fundamentals

## Author

Cristian Daniel Benavides Ospina

Electronic and Telecommunications Engineer

Python | Data Engineering | Machine Learning | Distributed Processing
