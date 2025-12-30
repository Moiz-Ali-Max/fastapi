from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get('/get-joke')
def get_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = httpx.get(url)
    data = response.json()

    return {
        "status": 200,
        "joke": data
    }