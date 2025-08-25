from src.utils.utils import db

class producto:
    @staticmethod
    def createProduct(productData):
        try:
            productData = {
                "id": productData['id'],
                "nombre": productData['name'],
                "descripcion": productData['description'],
                "precio_unitario": productData['unitPrice'],
                "id_proveedor": productData['providerID']
            }

            res = db.insert('producto', productData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Producto creado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error creando el producto!\n {e}")
            return { "code": 500, "message": f"Error al crear el producto: {str(e)}" }

    @staticmethod
    def getProducts():
        try:
            return { "code": 200, "data": db.get('producto')["data"] }
        except Exception as e:
            print(f"Error obteniendo los productos\n {e}")
            return { "code": 500, "message": "Error al obtener productos" }

    @staticmethod
    def getProductById(productID):
        try:
            data = db.getOne('producto', productID)
            return { "code": 200, "data": data["data"] }
        except Exception as e:
            print(f"Error obteniendo el producto {e}")
            return { "code": 500, "message": "Error al obtener producto" }

    @staticmethod
    def updateProduct(productID, productData):
        try:
            productData = {
                "nombre": productData['name'],
                "descripcion": productData['description'],
                "precio_unitario": productData['unitPrice'],
                "id_proveedor": productData['providerID']
            }

            res = db.update('producto', productID, productData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Producto actualizado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error actualizando el producto!\n {e}")
            return { "code": 500, "message": f"Error al actualizar el producto: {str(e)}" }

    @staticmethod
    def deleteProduct(productID):
        try:
            res = db.delete('producto', productID)

            if res["status"] == "ok":
                return { "code": 200, "message": "Producto eliminado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error eliminando el producto!\n {e}")
            return { "code": 500, "message": f"Error al eliminar el producto: {str(e)}" }