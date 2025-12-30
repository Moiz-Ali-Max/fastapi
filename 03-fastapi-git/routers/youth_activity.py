from fastapi import APIRouter

router = APIRouter()

@router.get("/youth-activity")
def get_youth_activity(activity: str):
    try:
        return {
            "status": 200,
            "data": activity
        }
    
    except Exception as e:
        return {
            "status": 500,
            "message": str(e),
            "data": None
        }