from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models

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