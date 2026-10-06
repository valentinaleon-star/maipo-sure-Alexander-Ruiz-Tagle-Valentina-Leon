"""
Servicio que lee el nivel de cloro desde un PLC y lo publica.
Planta Maipo Sur - Taller DevSecOps
"""

import os
import yaml
import logging
import requests
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cargar_configuracion(ruta="config.yaml"):
    """Carga la configuración desde el archivo YAML."""
    with open(ruta, "r") as f:
        return yaml.safe_load(f)


def obtener_password_plc(config):
    """
    Obtiene la contraseña del PLC.
    Primero intenta desde variable de entorno; si no, desde el archivo.
    """
    password_env = config["plc"].get("password_env")
    if password_env:
        return os.environ.get(password_env)
    return config["plc"].get("password")


@app.route("/cloro", methods=["GET"])
def leer_cloro():
    """Devuelve el nivel de cloro actual del PLC."""
    config = cargar_configuracion()
    password = obtener_password_plc(config)

    # Simulación de lectura del PLC
    nivel_cloro = 0.75  # mg/L (valor simulado)

    return jsonify({
        "planta": "Maipo Sur",
        "nivel_cloro_mg_l": nivel_cloro,
        "estado": "ok"
    })


@app.route("/salud", methods=["GET"])
def salud():
    """Endpoint de health check."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
