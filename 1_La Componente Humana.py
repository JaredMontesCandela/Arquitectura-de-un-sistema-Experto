# -*- coding: utf-8 -*-
"""

@author: jared
Mecatronica
7E  21310114

Para crear un ejemplo sencillo de un sistema experto en Python, podemos utilizar la estructura
básica de reglas "if-then" para emular cómo podría funcionar la lógica de un sistema experto. Aquí
un ejemplo que simula un sistema experto básico para diagnosticar problemas en una
computadora, basándonos en el conocimiento proporcionado por un experto en soporte técnico.
"""

# Base de Conocimiento: Reglas if-then proporcionadas por el experto
def diagnosticar_problema():
    print("Responde las siguientes preguntas con 'sí' o 'no'.")

    respuesta1 = input("¿La computadora enciende? ").strip().lower()
    if respuesta1 == 'no':
        print("Solución: Verifica la conexión del cable de alimentación y la fuente de poder.")
        return

    respuesta2 = input("¿La computadora emite pitidos al encender? ").strip().lower()
    if respuesta2 == 'sí':
        print("Solución: Hay un problema de hardware. Revisa la memoria RAM y la tarjeta madre.")
        return

    respuesta3 = input("¿El sistema operativo se carga? ").strip().lower()
    if respuesta3 == 'no':
        print("Solución: Reinstala el sistema operativo o repara el disco duro.")
        return

    respuesta4 = input("¿La computadora funciona lentamente? ").strip().lower()
    if respuesta4 == 'sí':
        print("Solución: Revisa si hay software malicioso o actualiza el hardware.")
        return

    print("\nDiagnóstico: No se detectó ningún problema grave.")

# Interfaz de Usuario: Aquí es donde el usuario interactúa con el sistema experto
if __name__ == "__main__":
    print("\nBienvenido al Sistema Experto de Diagnóstico de Computadoras")
    diagnosticar_problema()
