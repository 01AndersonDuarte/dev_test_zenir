from fastapi import FastAPI

from .database import Base, engine
from .models import Products

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health_route():
    return {"Status": "Is running"}