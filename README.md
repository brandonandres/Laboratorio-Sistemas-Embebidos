# Laboratorio-Sistemas-Embebidos
Aplicaciones en Sistemas Embebidos Primer Laboratorio

	Brandon Andrés León Caro.
	Samuel Felipe Rojas Heredia.
	Luis Alejandro Naranjo Garavito.

El presente proyecto tiene como objetivo integrar diferentes tecnologías de hardware y software para desarrollar un sistema interactivo capaz de detectar información del entorno, procesarla y responder mediante acciones físicas y comunicación conversacional. 
Para ello se combinan herramientas de visión artificial con OpenCV en Python, comunicación serial entre dispositivos (PC, Arduino y microcontrolador PIC16F887), y un chatbot básico ya sea integrado con DeepSeek o Chatgpt que permite interactuar con el sistema mediante texto o voz.
El sistema propuesto permite detectar y clasificar objetos simples mediante visión artificial, consultar información a través de un chatbot y ejecutar acciones físicas en el hardware. Esta arquitectura modular permite comprender la integración entre software de alto nivel (Python y OpenCV) y sistemas embebidos (Arduino y PIC).

Durante la práctica se desarrollan los siguientes objetivos:

•	Programar visión artificial con OpenCV en Python para detección y clasificación básica.

•	Implementar comunicación serial entre PC (Python), Arduino y PIC.

•	Programar el PIC16F887 en lenguaje C para controlar actuadores basados en comandos recibidos.

•	Desarrollar un chatbot simple que interprete preguntas sobre los objetos detectados.

•	Integrar diversas tecnologías en un sistema funcional de monitoreo y control.

Materiales que se utilizarán en los distintos puntos:
Los siguientes son los componentes de hardware necesarios para implementar los sistemas que se describirán en la práctica.
Entre los elementos principales se encuentran:

•	Placa Arduino (UNO, Nano o similar) utilizada como interfaz de comunicación entre la computadora y los dispositivos electrónicos.

•	PIC16F887.

•	Sensor de temperatura (LM35, DHT11 o TMP36) encargado de medir la temperatura del entorno.

•	LEDs con resistencias que funcionan como actuadores visuales del sistema.

•	Displays de siete segmentos.

•	Resistencias.

•	Capacitores.

•	Cristal de cuarzo.

•	Protoboard y cables de conexión para el montaje del circuito.

•	Computadora con Visual estudio Code, Arduino IDE y Python, incluyendo librerías como pyserial para la comunicación serial y speech_recognition para el procesamiento de voz.

Las siguientes secciones describen los diferentes módulos del sistema representados en el proyecto:

Punto 1 - Sistema conversor binario con PIC16F887

El primer punto muestra el diseño conceptual de un sistema basado en el microcontrolador PIC16F887 encargado de realizar conversiones numéricas desde binario hacia octal, hexadecimal y decimal.
En el montaje se utilizan cuatro entradas digitales (A, B, C y D) que representan un número binario de 4 bits. Estas entradas pueden ser activadas mediante interruptores o pulsadores. 
El microcontrolador recibe estos valores, ejecuta el proceso de conversión numérica mediante programación en lenguaje C y posteriormente envía el resultado hacia displays de siete segmentos.
Los displays permiten visualizar el resultado de las conversiones de manera clara para el usuario. Este módulo tiene como propósito reforzar el manejo de sistemas de numeración, lógica digital y programación de microcontroladores, además de mostrar la interacción entre hardware y software en sistemas embebidos.

Metodología y realización:

Punto 2 – Sistema de iluminación y monitoreo de temperatura mediante chatbot 

En el segundo punto se presenta un sistema de control básico que integra Arduino, sensores y un chatbot conversacional para interactuar con el usuario en este caso integrado con DeepSeek. 

En este sistema, el chatbot se ejecuta en el computador y se comunica con el Arduino a través de comunicación serial. El usuario puede enviar comandos por texto o voz, los cuales son interpretados por el chatbot y convertidos en instrucciones para el microcontrolador. 

El sistema permite realizar dos funciones principales: 

Control de iluminación: encender o apagar dos LEDs (rojo y verde) mediante comandos del chatbot. 
Monitoreo de temperatura: cuando el usuario solicita la temperatura, el Arduino lee los datos de un sensor y envía la información al chatbot para mostrarla al usuario. 
Este modelo introduce conceptos importantes como interfaces conversacionales, adquisición de datos de sensores y control de actuadores mediante comunicación serial. 

Metodología y realización: 

Para el desarrollo de este ejercicio se implementó un sistema de control mediante reconocimiento de voz utilizando el lenguaje de programación Python y una interfaz desarrollada con Streamlit, la cual permite controlar dispositivos conectados a un microcontrolador Arduino. 

Inicialmente se configuró la interfaz del programa para permitir la interacción entre el usuario y el sistema mediante el uso del micrófono del computador. Para esto se utilizó la librería streamlit_mic_recorder, la cual permite capturar la voz del usuario y convertirla en texto. Una vez obtenido el texto, el programa analiza las palabras clave para identificar la acción que el usuario desea realizar. 

Posteriormente se estableció una comunicación serial entre el computador y el microcontrolador Arduino utilizando la librería pyserial, a través del puerto COM5 y a una velocidad de 9600 baudios. En el Arduino se programó un código mediante Arduino IDE, donde se configuran los pines 8 y 9 como salidas para controlar un LED rojo y un LED verde. El programa del microcontrolador recibe comandos enviados desde Python por medio del puerto serial y, dependiendo del comando recibido, utiliza la función digitalWrite para encender o apagar los LEDs. 

Cuando el sistema detecta comandos relacionados con el encendido o apagado de luces, como por ejemplo “enciende rojo”, “apaga rojo”, “enciende verde” o “apaga verde”, el programa envía instrucciones específicas al Arduino como ROJO_ON, ROJO_OFF, VERDE_ON o VERDE_OFF, activando o desactivando los LEDs conectados al circuito electrónico. 

Además, el sistema incluye un módulo de síntesis de voz utilizando la librería gTTS, el cual permite que el chatbot genere respuestas habladas para confirmar las acciones ejecutadas. También se puede realizar la consulta de la temperatura, enviando el comando TEMP al Arduino y mostrando la respuesta obtenida en la interfaz. 

En caso de que el comando de voz no corresponda a una acción de control del Arduino, el sistema envía la consulta a un modelo de inteligencia artificial mediante una API externa (DeepSeek Chat), generando una respuesta automática que es mostrada y reproducida en la interfaz. De esta manera, el sistema integra reconocimiento de voz, comunicación con hardware e inteligencia artificial, permitiendo controlar dispositivos físicos mediante lenguaje natural 



Pruebas de Laboratorio y Componentes: 

Para el desarrollo y validación de este proyecto, se realizaron pruebas físicas utilizando el siguiente hardware y software: 

  

Hardware Utilizado 

Microcontrolador: Arduino UNO. 

Sensores: Sensor de temperatura (ej. LM35 o DHT11). 

Actuadores: LEDs indicadores (Rojo y Verde). 

Componentes Pasivos: Resistencias (220Ω), Protoboard y Jumpers de conexión. 

  

Entorno de Software y APIs 

IA Generativa: API Key de DeepSeek (Chatbot). 

IDE/Editores: Visual Studio Code y Arduino IDE. 

Lenguajes: Python (para la lógica de integración y procesamiento de voz). 

  

Escenarios de Prueba 

El sistema fue sometido a tres metodologías de validación para garantizar la robustez de la integración: 

Modo Texto: Interacción exclusiva mediante consola/chat escrito. 

Modo Voz: Interacción mediante reconocimiento de voz (Speech-to-Text). 

Modo Híbrido: Funcionamiento simultáneo donde el sistema responde correctamente independientemente del canal de entrada elegido por el usuario. 

Se adjunta un video de las pruebas realizadas en el que se muestra el correcto funcionamiento del ejercicio propuesto. 

Código Usado en Arduino IDE: 

código_arduino.ino 

Código usado en Visual Studio Code: 

app_punto_2.py 

Procesos realizados y librerías descargadas para su uso en el punto: 

LÉAME N° 2 

Punto 3 – Sistema de reconocimiento en el aula con OpenCV, Arduino y PIC 

El punto 3 describe la arquitectura general del sistema final, en el cual se integran visión artificial, procesamiento conversacional y control de hardware. 

En este escenario, la cámara de la computadora captura imágenes del entorno y utiliza OpenCV en Python para detectar y clasificar objetos simples, como colores o figuras geométricas. Esta información es procesada por el sistema y puede ser consultada por los usuarios a través del chatbot. 

El flujo de funcionamiento del sistema es el siguiente: 

La cámara de la PC detecta y clasifica objetos mediante OpenCV. 

El chatbot procesa las preguntas realizadas por los estudiantes. 

Arduino actúa como puente de comunicación entre la computadora y el microcontrolador. 

El PIC16F887 recibe comandos y ejecuta acciones físicas, como activar LEDs indicadores. 

Este enfoque demuestra cómo es posible integrar visión artificial, sistemas embebidos y procesamiento conversacional para desarrollar aplicaciones interactivas dentro de un entorno educativo. 

Metodología y realización: 

En el tercer ejercicio se desarrolló un sistema de visión artificial capaz de detectar colores en tiempo real utilizando la cámara del computador y controlar dispositivos conectados a un Arduino. 

El programa fue desarrollado en Python utilizando la librería OpenCV, la cual permite el procesamiento de imágenes y video. Inicialmente se activó la cámara del computador para capturar imágenes continuamente mediante VideoCapture(0). Cada imagen capturada fue convertida al espacio de color HSV (Hue, Saturation, Value), ya que este modelo facilita la identificación de colores dentro de una imagen. Posteriormente se definieron rangos de valores HSV específicos para los colores rojo y verde, generando máscaras que permiten identificar las regiones donde se encuentran estos colores. 

El sistema analiza cada cuadro de video y utiliza técnicas de detección de contornos para identificar objetos que tengan un tamaño significativo dentro de la imagen, evitando así errores causados por ruido visual. Cuando se detecta un objeto rojo o verde, el programa dibuja un contorno alrededor del objeto y muestra una etiqueta indicando el color detectado en la ventana de visualización. 

Además, el programa establece una comunicación serial con Arduino mediante el puerto COM5 a una velocidad de 9600 baudios, utilizando la librería serial. Dependiendo del color detectado, el sistema envía comandos específicos al microcontrolador como ROJO_ON, ROJO_OFF, VERDE_ON o VERDE_OFF, los cuales son interpretados por el código programado en Arduino IDE. Este código recibe los comandos desde el puerto serial y utiliza la función digitalWrite para enviar señales HIGH o LOW a los pines 8 y 9, donde se encuentran conectados un LED rojo y un LED verde, permitiendo encenderlos o apagarlos según la instrucción recibida. 

De esta manera, el sistema integra visión artificial, procesamiento de imágenes y comunicación con hardware, permitiendo controlar dispositivos electrónicos a partir de la información visual capturada por la cámara en tiempo real. 
