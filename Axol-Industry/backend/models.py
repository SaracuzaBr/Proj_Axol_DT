from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .database import Base

class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, index=True) # Ex: "CNC-01"
    temperature = Column(Float)
    vibration = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)