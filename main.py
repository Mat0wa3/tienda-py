from fastapi import FastAPI
from src.models.tienda import tienda

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "mundo"}

@app.get("/api/v1/stores")
def getStore():
    store = tienda.getStoreById(0)
    return store["data"]