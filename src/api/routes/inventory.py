from fastapi import APIRouter 
 
router = APIRouter(prefix="/inventory", tags=["inventory"]) 
 
@router.get("/") 
async def get_inventory(): 
    return {"message": "Get inventory"} 
