from src.utils.utils import db

class proveedor:
    @staticmethod
    def createProvider(providerData):
        try:
            providerData = {
                "id": providerData['id'],
                "nombre": providerData['name'],
                "telefono": providerData['phone'],
                "direccion": providerData['address']
            }

            res = db.insert('proveedor', providerData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Proveedor creado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error creando el proveedor!\n {e}")
            return { "code": 500, "message": "Error al crear el proveedor" }
    
    @staticmethod
    def getProviders():
        try:
            return { "code": 200, "data": db.get('proveedor')["data"] }
        except Exception as e:
            print(f"Error obteniendo los proveedores\n {e}")
            return { "code": 500, "message": "Error al obtener proveedores" }

    @staticmethod
    def getProviderById(providerID):
        try:
            data = db.getOne('proveedor', providerID)
            return { "code": 200, "data": data["data"] }
        except Exception as e:
            print(f"Error obteniendo el proveedor {e}")
            return { "code": 500, "message": "Error al obtener proveedor" }

    @staticmethod
    def updateProvider(providerID, providerData):
        try:
            providerData = {
                "nombre": providerData['name'],
                "telefono": providerData['phone'],
                "direccion": providerData['address']
            }

            res = db.update('proveedor', providerID, providerData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Proveedor actualizado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error actualizando el proveedor!\n {e}")
            return { "code": 500, "message": "Error al actualizar el proveedor" }

    @staticmethod
    def deleteProvider(providerID):
        try:
            res = db.delete('proveedor', providerID)

            if res["status"] == "ok":
                return { "code": 200, "message": "Proveedor eliminado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error eliminando el proveedor!\n {e}")
            return { "code": 500, "message": "Error al eliminar el proveedor" }
