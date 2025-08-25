from fastapi import FastAPI
from src.models.tienda import tienda
from src.models.producto import producto
from src.models.proveedor import proveedor
from src.models.usuario import usuario

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

from src.models.proveedor import proveedor

app = FastAPI()


@app.get("/api/v1/providers")
def getProviders():
    res = proveedor.getProviders()
    return res

@app.get("/api/v1/providers/{provider_id}")
def getProvider(provider_id: int):
    res = proveedor.getProviderById(provider_id)
    return res

@app.post("/api/v1/providers")
def createProvider():
    providerData = {
        "id": 1,
        "name": "Proveedor Ejemplo",
        "phone": "3001234567",
        "address": "Calle 123 #45-67"
    }
    res = proveedor.createProvider(providerData)
    return res


@app.put("/api/v1/providers/{provider_id}")
def updateProvider(provider_id: int):
    providerData = {
        "name": "Proveedor Actualizado",
        "phone": "3107654321",
        "address": "Carrera 45 #67-89"
    }
    res = proveedor.updateProvider(provider_id, providerData)
    return res


@app.delete("/api/v1/providers/{provider_id}")
def deleteProvider(provider_id: int):
    res = proveedor.deleteProvider(provider_id)
    return res

@app.get("/api/v1/products")
def getProducts():
    return producto.getProducts()

@app.get("/api/v1/products/{productID}")
def getProductById(productID: int):
    return producto.getProductById(productID)


@app.post("/api/v1/products")
def createProduct():
    productData = {
        "id": 1,
        "name": "Laptop",
        "description": "Laptop gamer 16GB RAM",
        "unitPrice": 4200.50,
        "providerID": 1
    }
    return producto.createProduct(productData)


@app.put("/api/v1/products/{productID}")
def updateProduct(productID: int):
    productData = {
        "name": "Laptop Pro",
        "description": "Laptop gamer 32GB RAM",
        "unitPrice": 5200.99,
        "providerID": 1
    }
    return producto.updateProduct(productID, productData)

@app.delete("/api/v1/products/{productID}")
def deleteProduct(productID: int):
    return producto.deleteProduct(productID)

@app.get("/api/v1/users")
def getUsers():
    return usuario.getUsers()

@app.get("/api/v1/users/{userID}")
def getUserById(userID: int):
    return usuario.getUserById(userID)

@app.post("/api/v1/users")
def createUser():
    userData = {
        "id": 2,
        "name": "Andrea",
        "last_name": "Lopez",
        "password": "supersecreta"
    }
    return usuario.createUser(userData)

@app.put("/api/v1/users/{userID}")
def updateUser(userID: int):
    userData = {
        "name": "Andrea",
        "last_name": "Lopez",
        "password": "nuevaClave"
    }
    return usuario.updateUser(userID, userData)

@app.delete("/api/v1/users/{userID}")
def deleteUser(userID: int):
    return usuario.deleteUser(userID)