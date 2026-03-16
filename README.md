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

