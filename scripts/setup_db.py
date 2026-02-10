import sqlalchemy 
from src.core.database.models import Base 
from config.database import engine 
 
def setup_database(): 
    Base.metadata.create_all(bind=engine) 
 
if __name__ == "__main__": 
    setup_database() 
