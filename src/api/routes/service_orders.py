from fastapi import APIRouter, HTTPException 
 
router = APIRouter(prefix="/service-orders", tags=["service-orders"]) 
 
@router.get("/") 
async def get_service_orders(): 
    return {"message": "Get all service orders"} 
