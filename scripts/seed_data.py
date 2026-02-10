import random 
from src.core.database.models import ServiceOrder 
from config.database import SessionLocal 
 
def seed_data(): 
    db = SessionLocal() 
    # Seed logic here 
    db.close() 
 
if __name__ == "__main__": 
    seed_data() 
