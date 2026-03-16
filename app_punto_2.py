import streamlit as st
from streamlit_mic_recorder import speech_to_text
from gtts import gTTS
import serial
import time
import requests
import io

# =========================
# CONFIGURACIÓN IA
# =========================
API_KEY = "sk-2d5996dc3b04479e9dacbf5d0085ce60"
API_URL = "https://api.deepseek.com/v1/chat/completions"

def enviar_mensaje(mensaje):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "Error con la API."

# =========================
# FUNCIÓN HABLAR (SIN ARCHIVO)
# =========================
def hablar(texto):
    tts = gTTS(texto, lang="es")
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    st.audio(mp3_fp, format="audio/mp3")

# =========================
# INICIALIZAR SERIAL SOLO UNA VEZ
# =========================
if "arduino" not in st.session_state:
    try:
        st.session_state.arduino = serial.Serial('COM5', 9600, timeout=1)
        time.sleep(2)
    except:
        st.error("No se pudo abrir el puerto COM5. Cierra Arduino IDE.")
        st.stop()

arduino = st.session_state.arduino

# =========================
# INTERFAZ
# =========================
st.title("Chatbot con Voz y Arduino")
st.write("Controla LEDs y consulta temperatura con tu voz")

text = speech_to_text(language="es", use_container_width=True, just_once=True, key="STT")

if text:
    texto = text.lower()
    st.write("Tú:", texto)
    st.write("DEBUG:", texto)

    # =========================
    # LED ROJO
    # =========================
    if "rojo" in texto and any(p in texto for p in ["enciende", "prende", "activar"]):
        arduino.write(b'ROJO_ON\n')
        respuesta = "Encendiendo luz roja"
        st.write("Sistema:", respuesta)
        hablar(respuesta)

    elif "rojo" in texto and any(p in texto for p in ["apaga", "apagar", "desactiva"]):
        arduino.write(b'ROJO_OFF\n')
        respuesta = "Apagando luz roja"
        st.write("Sistema:", respuesta)
        hablar(respuesta)

    # =========================
    # LED VERDE
    # =========================
    elif "verde" in texto and any(p in texto for p in ["enciende", "prende", "activar"]):
        arduino.write(b'VERDE_ON\n')
        respuesta = "Encendiendo luz verde"
        st.write("Sistema:", respuesta)
        hablar(respuesta)

    elif "verde" in texto and any(p in texto for p in ["apaga", "apagar", "desactiva"]):
        arduino.write(b'VERDE_OFF\n')
        respuesta = "Apagando luz verde"
        st.write("Sistema:", respuesta)
        hablar(respuesta)

    # =========================
    # TEMPERATURA
    # =========================
    elif "temperatura" in texto:
        arduino.reset_input_buffer()
        arduino.write(b'TEMP\n')
        time.sleep(0.5)

        respuesta = arduino.readline().decode().strip()

        if respuesta == "":
            respuesta = "No pude leer la temperatura"

        st.write("Sistema:", respuesta)
        hablar(respuesta)

    # =========================
    # IA GENERAL
    # =========================
    else:
        if API_KEY != "":
            respuesta = enviar_mensaje(texto)
        else:
            respuesta = "Comando no reconocido."

        st.write("Chatbot:", respuesta)
        hablar(respuesta)
