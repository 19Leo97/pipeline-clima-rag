"""
extraer_clima.py — Fase 0 del proyecto E2E
Extrae datos meteorológicos diarios de la API Open-Meteo (gratuita, sin API key)
y los guarda como JSON local en la carpeta datos_crudos/.
"""

import json
import os
import time
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

# Carga las variables del archivo .env (aunque Open-Meteo no necesita key,
# practicamos el patrón de configuración desde el día 1)
load_dotenv()

# --- Configuración centralizada: todo lo que puede cambiar va aquí arriba ---
CIUDAD = os.getenv("CIUDAD", "Bogota")
LATITUD = float(os.getenv("LATITUD", "4.71"))
LONGITUD = float(os.getenv("LONGITUD", "-74.07"))
URL_API = "https://api.open-meteo.com/v1/forecast"
MAX_REINTENTOS_429 = 3
ESPERA_429_SEGUNDOS = 5

PARAMETROS = {
    "latitude": LATITUD,
    "longitude": LONGITUD,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "America/Bogota",
    "forecast_days": 7,
}


def extraer_datos() -> dict:
    """Llama la API y devuelve el JSON como diccionario de Python."""
    respuesta = None
    for intento in range(MAX_REINTENTOS_429 + 1):
        respuesta = requests.get(URL_API, params=PARAMETROS, timeout=30)
        if respuesta.status_code == 429 and intento < MAX_REINTENTOS_429:
            time.sleep(ESPERA_429_SEGUNDOS)
            continue
        break
    # Si el servidor responde 4xx o 5xx, esto lanza una excepción con detalle
    respuesta.raise_for_status()
    return respuesta.json()


def guardar_json(datos: dict) -> str:
    """Guarda el JSON con fecha en el nombre, para nunca sobrescribir."""
    os.makedirs("datos_crudos", exist_ok=True)
    marca_tiempo = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    ruta = f"datos_crudos/clima_{CIUDAD.lower()}_{marca_tiempo}.json"
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    return ruta


if __name__ == "__main__":
    datos = extraer_datos()
    ruta = guardar_json(datos)
    print(f"Datos guardados en: {ruta}")
    print(f"Días extraídos: {len(datos['daily']['time'])}")