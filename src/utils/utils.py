import json

def insert(data):
    with open("data.json", "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

def get(data):
    print("TODO")