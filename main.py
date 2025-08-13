from fastapi import FastAPI
from src.models.tienda import tienda

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "mundo"}

@app.get("/api/v1/stores")
def getStore():
    store = tienda.getStoreById(0)
    return store

@app.post("/api/v1/stores")
def createStore():
    storeData = {
        "id": 0,
        "cityID": 0,
        "sufix": "Bello",
        "address": "CRA 80a #112-56"
    }

    res = tienda.createStore(storeData)
    return res