from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/user-check")
def user_check(user_check_id: str):
    try:
        return {
            "status": 200,
            "data": f"User Check is valid, ID is: {user_check_id}"
        }

    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": None
        }

class user_activity_request(BaseModel):
    activity: str

class user_activity_response(BaseModel):
    user_id: int
    activity: str

@router.post("/user-activity", response_model = user_activity_response)
async def user_activity(request: user_activity_request):
    user_id = 1
    activity = request.activity
    
    return user_activity_response(user_id = user_id, activity = activity)

