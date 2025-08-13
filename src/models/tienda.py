from src.utils.utils import db

class tienda: 
    @staticmethod
    def createStore(storeData):
        try:
            storeData = {
                "id": storeData['id'],
                "id_ciudad": storeData['cityID'],
                "sufijo": storeData['sufix'],
                "direccion": storeData['address']
            }

            res = db.insert('tienda', storeData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Tienda creada correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error creando la tienda!\n {e}")
            return { "code": 500, "message": "Error al crear la tienda" }
    
    @staticmethod
    def getStores():
        try:
            return { "code": 200, "data": db.get('tienda')["data"] }
        except Exception as e:
            print(f"Error obteniendo las tiendas\n {e}")

    @staticmethod
    def getStoreById(storeID):
        try:
            data = db.getOne('tienda', storeID)

            return { "code": 200, "data": data["data"] }
        except Exception as e:
            print(f"Error obteniendo la tienda {e}")
