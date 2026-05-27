import pandas as pd

def transform_weather(raw_data: dict):

    daily = raw_data["daily"]

    df = pd.DataFrame({
    "date": pd.to_datetime(daily["time"]).date,
    "temp_max": daily["temperature_2m_max"],
    "temp_min": daily["temperature_2m_min"],
    "precipitation": daily["precipitation_sum"],
    "wind_speed_max": daily["windspeed_10m_max"]
})

    df["temp_range"] = df["temp_max"] - df["temp_min"]

    df["weather_risk_score"] = (
        df["precipitation"] * 0.6 +
        df["wind_speed_max"] * 0.4
    )

    df = df.fillna(0)

    return df