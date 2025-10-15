import json

def load_config(path="config.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Błąd ładowania konfiguracji: {e}")
        return {}
