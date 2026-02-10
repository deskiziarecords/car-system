from fastapi import APIRouter 
 
router = APIRouter(prefix="/financial", tags=["financial"]) 
 
@router.get("/") 
async def get_financial_reports(): 
    return {"message": "Get financial reports"} 
