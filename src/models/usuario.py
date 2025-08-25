from src.utils.utils import db

class usuario:
    @staticmethod
    def createUser(userData):
        try:
            userData = {
                "id": userData['id'],
                "nombre": userData['name'],
                "apellido": userData['last_name'],
                "password": userData['password']
            }

            res = db.insert('usuario', userData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Usuario creado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error creando el usuario!\n {e}")
            return { "code": 500, "message": f"Error al crear el usuario: {str(e)}" }

    @staticmethod
    def getUsers():
        try:
            return { "code": 200, "data": db.get('users')["data"] }
        except Exception as e:
            print(f"Error obteniendo los usuarios\n {e}")
            return { "code": 500, "message": "Error al obtener usuarios" }

    @staticmethod
    def getUserById(userID):
        try:
            data = db.getOne('usuario', userID)
            return { "code": 200, "data": data["data"] }
        except Exception as e:
            print(f"Error obteniendo el usuario {e}")
            return { "code": 500, "message": "Error al obtener usuario" }

    @staticmethod
    def updateUser(userID, userData):
        try:
            userData = {
                "nombre": userData['name'],
                "apellido": userData['last_name'],
                "password": userData['password']
            }

            res = db.update('usuario', userID, userData)

            if res["status"] == "ok":
                return { "code": 200, "message": "Usuario actualizado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error actualizando el usuario!\n {e}")
            return { "code": 500, "message": f"Error al actualizar el usuario: {str(e)}" }

    @staticmethod
    def deleteUser(userID):
        try:
            res = db.delete('usuario', userID)

            if res["status"] == "ok":
                return { "code": 200, "message": "Usuario eliminado correctamente" }
            else:
                return { "code": res["status"], "message": res["message"] }
        except Exception as e:
            print(f"Error eliminando el usuario!\n {e}")
            return { "code": 500, "message": f"Error al eliminar el usuario: {str(e)}" }
