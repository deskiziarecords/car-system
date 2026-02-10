from fastapi import APIRouter 
 
router = APIRouter(prefix="/customers", tags=["customers"]) 
 
@router.get("/") 
async def get_customers(): 
    return {"message": "Get customers"} 
