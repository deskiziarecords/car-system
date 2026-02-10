from sqlalchemy import Column, Integer, String, DateTime, Float 
from sqlalchemy.ext.declarative import declarative_base 
 
Base = declarative_base() 
 
class ServiceOrder(Base): 
    __tablename__ = "service_orders" 
    id = Column(Integer, primary_key=True, index=True) 
    customer_id = Column(Integer) 
    vehicle_id = Column(Integer) 
    status = Column(String) 
    total_cost = Column(Float) 
