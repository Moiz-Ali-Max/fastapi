from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/check-weather")
async def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 33.7215,
	    "longitude": 73.0433,
	    "hourly": "temperature_2m",
    }

    response = httpx.get(url, params = params)
    data = response.json()
    return {
        "status": 200,
        "weather": data
    }
