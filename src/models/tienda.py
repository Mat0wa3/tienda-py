storeData = [
    {
        "storeID": 0,
        "id_ciudad": "Medellín",
        "sufijo": "calasanz",
        "direccion": "CRA 80a #112-56"
    },
    {
        "storeID": 1,
        "id_ciudad": "Bello",
        "sufijo": "Paris",
        "direccion": "CRA 83a #112-75"
    }
]

class tienda: 
    @staticmethod
    def createStore(storeData):
        try:
            storeData = {
                "id_ciudad": storeData.cityID,
                "sufijo": storeData.sufix,
                "direccion": storeData.address
            }

            return { "code": 200, "message": "Tienda creada correctamente" }
        except ValueError:
            print("Error creando la tienda! " + ValueError)
            return { "code": 500, "message": "Error al crear la tienda" }
    
    @staticmethod
    def getStores():
        try:
            return { "code": 200, "data": storeData }
        except ValueError:
            print("Error obteniendo las tiendas " + ValueError)

    @staticmethod
    def getStoreById(storeID):
        try:
            data = next((store for store in storeData if store["storeID"] == storeID), None)

            return { "code": 200, "data": data }
        except ValueError:
            print("Error obteniendo la tiendas " + ValueError)