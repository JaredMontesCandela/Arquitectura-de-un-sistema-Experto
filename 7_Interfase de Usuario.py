# -*- coding: utf-8 -*-
"""
@author: jared
Mecatronica
7E  21310114

# Iniciar la interfaz de usuario
interfaz_usuario()

Para implementar un ejemplo de un sistema experto en Python con una interfaz de usuario
básica, podemos utilizar una interfaz de línea de comandos (CLI) para interactuar con el usuario.
La interfaz de usuario solicitará información, mostrará las conclusiones del motor de inferencia,
y en caso de que el motor de inferencia no pueda llegar a una conclusión debido a la falta de
información, pedirá al usuario que proporcione datos adicionales.
"""

# Base de Conocimiento Inicial
base_de_conocimiento = {
    "fiebre": {"gripe": 0.7, "COVID-19": 0.9},
    "tos": {"gripe": 0.6, "COVID-19": 0.8}
}

def interfaz_usuario():
    print("Bienvenido al Sistema Experto de Diagnóstico Médico")
    
    while True:
        sintomas = input("Por favor, ingrese los síntomas del paciente separados por comas (o 'salir' para terminar): ").strip().lower()
        if sintomas == 'salir':
            print("Gracias por usar el sistema experto. ¡Hasta luego!")
            break

        sintomas_lista = [s.strip() for s in sintomas.split(",")]

        # Diagnóstico con adquisición de conocimiento
        resultado = motor_inferencia_con_adquisicion(sintomas_lista)
        
        if resultado:
            print("\nResultado del Diagnóstico:")
            for enfermedad, probabilidad in resultado.items():
                print(f"{enfermedad}: Probabilidad acumulada = {probabilidad:.2f}")
            
            print("\nRazones:")
            for sintoma in sintomas_lista:
                if sintoma in base_de_conocimiento:
                    print(f"El síntoma '{sintoma}' está asociado con {list(base_de_conocimiento[sintoma].keys())}.")
                else:
                    print(f"No hay conocimiento previo sobre el síntoma '{sintoma}'.")
        else:
            print("No se pudo realizar un diagnóstico basado en la información proporcionada.")
        print("\n----------------------------------------\n")


def motor_inferencia_con_adquisicion(sintomas):
    posibles_enfermedades = {}
    
    for sintoma in sintomas:
        if sintoma in base_de_conocimiento:
            for enfermedad, probabilidad in base_de_conocimiento[sintoma].items():
                if enfermedad in posibles_enfermedades:
                    posibles_enfermedades[enfermedad] += probabilidad
                else:
                    posibles_enfermedades[enfermedad] = probabilidad
        else:
            # Solicitar información adicional si el síntoma no está en la base de conocimiento
            nueva_informacion = subsistema_adquisicion_conocimiento(sintoma)
            if nueva_informacion:
                base_de_conocimiento[sintoma] = nueva_informacion
                for enfermedad, probabilidad in nueva_informacion.items():
                    if enfermedad in posibles_enfermedades:
                        posibles_enfermedades[enfermedad] += probabilidad
                    else:
                        posibles_enfermedades[enfermedad] = probabilidad
    
    # Ordenamos las enfermedades por la suma de probabilidades
    posibles_enfermedades = dict(sorted(posibles_enfermedades.items(), key=lambda item: item[1], reverse=True))
    
    return posibles_enfermedades

def subsistema_adquisicion_conocimiento(sintoma):
    print(f"No se encontró información sobre el síntoma: {sintoma}")
    respuesta = input(f"¿Conoces alguna enfermedad asociada con el síntoma {sintoma}? (sí/no): ").strip().lower()
    
    if respuesta == "sí":
        nuevas_enfermedades = {}
        while True:
            enfermedad = input("Nombre de la enfermedad: ").strip()
            probabilidad = float(input(f"Probabilidad de que {enfermedad} esté asociada con {sintoma} (0 a 1): ").strip())
            nuevas_enfermedades[enfermedad] = probabilidad
            otra = input("¿Agregar otra enfermedad? (sí/no): ").strip().lower()
            if otra != "sí":
                break
        # Verificar la consistencia de la nueva información
        if comprobar_consistencia(nuevas_enfermedades):
            print(f"Nueva información sobre {sintoma} agregada a la base de conocimiento.")
            return nuevas_enfermedades
        else:
            print("La información proporcionada no es consistente. No se agregará a la base de conocimiento.")
            return None
    else:
        print(f"No se puede continuar el proceso de inferencia sin más información sobre {sintoma}.")
        return None

def comprobar_consistencia(nuevas_enfermedades):
    suma_probabilidades = sum(nuevas_enfermedades.values())
    if suma_probabilidades <= 1.0:
        return True
    else:
        print("La suma de las probabilidades excede 1.0, lo que es inconsistente.")
        return False

def subsistema_adquisicion_conocimiento(sintoma):
    print(f"No se encontró información sobre el síntoma: {sintoma}")
    respuesta = input(f"¿Conoces alguna enfermedad asociada con el síntoma {sintoma}? (sí/no): ").strip().lower()
    
    if respuesta == "sí":
        nuevas_enfermedades = {}
        while True:
            enfermedad = input("Nombre de la enfermedad: ").strip()
            probabilidad = float(input(f"Probabilidad de que {enfermedad} esté asociada con {sintoma} (0 a 1): ").strip())
            nuevas_enfermedades[enfermedad] = probabilidad
            otra = input("¿Agregar otra enfermedad? (sí/no): ").strip().lower()
            if otra != "sí":
                break
        # Verificar la consistencia de la nueva información
        if comprobar_consistencia(nuevas_enfermedades):
            print(f"Nueva información sobre {sintoma} agregada a la base de conocimiento.")
            return nuevas_enfermedades
        else:
            print("La información proporcionada no es consistente. No se agregará a la base de conocimiento.")
            return None
    else:
        print(f"No se puede continuar el proceso de inferencia sin más información sobre {sintoma}.")
        return None

def comprobar_consistencia(nuevas_enfermedades):
    suma_probabilidades = sum(nuevas_enfermedades.values())
    if suma_probabilidades <= 1.0:
        return True
    else:
        print("La suma de las probabilidades excede 1.0, lo que es inconsistente.")
        return False
