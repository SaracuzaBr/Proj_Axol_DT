from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
from fastapi.middleware.cors import CORSMiddleware # Importe isso

# Cria as tabelas no banco de dados se elas não existirem
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nexus Industry - API")

@app.get("/")
def health_check():
    """Rota para verificar se a API está online."""
    return {
        "status": "healthy",
        "timestamp": models.datetime.utcnow(),
        "database": "connected"
    }

from pydantic import BaseModel

# Esquema para validar os dados que chegam do simulador
class SensorData(BaseModel):
    machine_id: str
    temperature: float
    vibration: float

@app.post("/readings")
def receive_reading(data: SensorData, db: Session = Depends(get_db)):
    # Criando o registro no banco de dados
    new_reading = models.SensorReading(
        machine_id=data.machine_id,
        temperature=data.temperature,
        vibration=data.vibration
    )
    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)
    return {"message": "Dado recebido com sucesso!", "id": new_reading.id}

# 1. Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, use o endereço do seu React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Rota para retornar as últimas 10 leituras
@app.get("/readings")
def get_readings(db: Session = Depends(get_db)):
    # Busca as 10 leituras mais recentes, ordenadas por ID decrescente
    readings = db.query(models.SensorReading).order_by(models.SensorReading.id.desc()).limit(10).all()
    return readings