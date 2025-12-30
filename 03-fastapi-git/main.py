from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import user_activity, weather, jokes


app = FastAPI()

@app.get("/")
def server_check():
    try:
        return {
            "status": 200,
            "data": "Server is running"
        }

    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": None
        }




app.include_router(user_activity.router, prefix="/user", tags=["Youth Activity Routes"])
app.include_router(weather.router, prefix="/weather", tags=["Weather Route"])
app.include_router(jokes.router, prefix="/joke", tags=['Jokes Route'])