import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(latitude: float, longitude: float, days: int = 7):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "windspeed_10m_max"
        ],
        "timezone": "auto",
        "forecast_days": days
    }

    try:
        logging.info("Calling Open-Meteo API...")
        response = requests.get(BASE_URL, params=params, timeout=30)

        response.raise_for_status()

        data = response.json()

        if "daily" not in data:
            raise ValueError("Unexpected API structure: 'daily' key missing")

        logging.info("Data fetched successfully")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    data = fetch_weather(12.97, 77.59)  # Example Bangalore
    print(data)