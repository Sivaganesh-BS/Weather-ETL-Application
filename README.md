# 🌦️ Weather ETL Application

This project automates the collection and storage of weather data using Apache Airflow. It extracts weather parameters such as temperature, humidity, wind speed, and UV index from a weather API every 30 minutes and stores them into a SQL table (SQLite by default).

---

## 📌 Key Features

- 🔄 **Automated ETL** every 30 minutes using Airflow scheduler
- 🌐 **Weather API Integration** to fetch real-time weather data
- 🧮 Stores parameters like temperature, humidity, wind direction, UV index, and more
- 🗃️ **SQL Table Storage** (using SQLite)
- 🔧 Easily extendable to PostgreSQL or MySQL

---

## 🗂️ Data Captured

| Field              | Type    | Description                                 |
|--------------------|---------|---------------------------------------------|
| `time`             | TEXT    | Timestamp (local or UTC)                    |
| `temperature`      | REAL    | Ambient temperature in °C                   |
| `humidity`         | REAL    | Relative humidity in %                      |
| `windspeed`        | REAL    | Wind speed in km/h                          |
| `winddirection`    | REAL    | Wind direction in degrees (0-360°)          |
| `rain`             | REAL    | Rainfall in mm                              |
| `showers`          | REAL    | Showers in mm                               |
| `is_day`           | INTEGER | 1 = Day, 0 = Night                          |
| `max_temperature`  | REAL    | Max temperature of the day in °C            |
| `min_temperature`  | REAL    | Min temperature of the day in °C            |
| `ux_index_max`     | REAL    | Max UV index value                          |

---

## 🛠️ How It Works

- The **Airflow DAG** runs on a `*/30 * * * *` schedule (every 30 mins).
- It calls a **public weather API** with predefined latitude and longitude.
- Transforms the API response to extract only relevant fields.
- Saves the formatted data to a **SQLite** database.

---


