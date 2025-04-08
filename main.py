from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

@app.get("/weather")
def get_weather(city: str = Query(..., description="City to get weather for")):
    if city.lower() == "hue":
        return {"weather": "Cloudy", "temperature": "25°C"}
    elif city.lower() == "da nang":
        return {"weather": "Sunny", "temperature": "30°C"}
    return {"weather": "Unknown", "temperature": "?"}
