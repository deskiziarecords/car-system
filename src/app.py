from fastapi import FastAPI 
from .api.routes import service_orders, inventory, customers, financial, dashboard 
 
app = FastAPI(title="Automotive Workshop Elixir") 
 
@app.get("/") 
async def root(): 
    return {"message": "Welcome to Automotive Workshop Elixir API"} 
