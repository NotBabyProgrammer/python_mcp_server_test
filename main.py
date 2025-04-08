from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WeatherRequest(BaseModel):
    city: str

@app.post("/weather")
def get_weather(data: WeatherRequest):
    city = data.city.lower()
    if city == "hue":
        return {"weather": "Cloudy", "temperature": "28°C"}
    elif city == "da nang":
        return {"weather": "Sunny", "temperature": "30°C"}
    return {"weather": "Unknown", "temperature": "?"}
