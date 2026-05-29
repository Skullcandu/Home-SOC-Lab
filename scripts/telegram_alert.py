#!/usr/bin/env python3
"""
Script de Respuesta Activa para Wazuh
Objetivo: Enviar notificaciones de alertas críticas a un bot de Telegram.
"""

import sys
import json
import requests

# ==========================================
# CONFIGURACIÓN (Reemplazar con datos reales)
# ==========================================
CHAT_ID = "<TU_CHAT_ID>"
BOT_TOKEN = "<TU_BOT_TOKEN>"
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram_alert(message):
    """Envía el mensaje formateado a la API de Telegram."""
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(TELEGRAM_URL, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar la alerta a Telegram: {e}")
        sys.exit(1)

def main():
    # Wazuh pasa el archivo de alerta como primer argumento al script
    if len(sys.argv) < 2:
        print("Error: No se proporcionó el archivo de alerta.")
        sys.exit(1)
        
    alert_file = sys.argv[1]
    
    try:
        with open(alert_file, 'r') as f:
            alert_data = json.load(f)
    except Exception as e:
        print(f"Error al leer el archivo de alerta: {e}")
        sys.exit(1)

    # Extraer información clave de la alerta generada por el SIEM
    description = alert_data.get('rule', {}).get('description', 'Sin descripción')
    level = alert_data.get('rule', {}).get('level', 'N/A')
    agent_name = alert_data.get('agent', {}).get('name', 'N/A')
    
    # Formatear el mensaje que llegará al celular
    message = (
        f"🚨 *ALERTA CRÍTICA SOC* 🚨\n\n"
        f"**Nivel:** {level}\n"
        f"**Agente:** {agent_name}\n"
        f"**Descripción:** {description}\n"
    )
    
    send_telegram_alert(message)

if __name__ == "__main__":
    main()
