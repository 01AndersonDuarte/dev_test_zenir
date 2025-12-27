from fastapi import FastAPI

from .database import Base, engine
from .api import products_api
from .models import products_model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dev Test Zenir", version="1.0.0")
app.include_router(products_api.router)

@app.get("/health")
def health_route():
    return {"Status": "Is running"}

