import json

class db:
    base_path = 'src/data/'
    @staticmethod
    def insert(file: str, new_data: dict):
        try:
            with open(f"{db.base_path}{file}.json", "r", encoding="utf-8") as archivo:
                try:
                    data = json.load(archivo)
                except json.JSONDecodeError:
                    data = []
            
            if not isinstance(data, list):
                data = [data]

            data.append(new_data)

            with open(f"{db.base_path}{file}.json", "w", encoding="utf-8") as archivo:
                json.dump(data, archivo, indent=4, ensure_ascii=False)

            return { "status": "ok" }
        except Exception as e:
            return { "status": 500, "message": f"Error inserting data: {e}" }
    
    @staticmethod
    def get(file):
        try:
            with open(f"{db.base_path}{file}.json", "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
            return { "status": "ok", "data": data }
        except Exception as e:
            return { "status": 500, "message": f"Error getting data: {e}" }
    
    @staticmethod
    def getOne(file, id):
        try:
            with open(f"{db.base_path}{file}.json", "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
            return { "status": "ok", "data": data[id] }
        except Exception as e:
            return { "status": 500, "message": f"Error getting data: {e}" }