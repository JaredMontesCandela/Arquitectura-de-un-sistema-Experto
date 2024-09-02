# -*- coding: utf-8 -*-
"""
@author: jared
Mecatronica
7E  21310114

"""
# Base de Conocimiento Inicial
base_de_conocimiento = {
    "fiebre": {"gripe": 0.7, "COVID-19": 0.9},
    "tos": {"gripe": 0.6, "COVID-19": 0.8},
    "dificultad_respiratoria": {"COVID-19": 0.9}
}

def motor_inferencia(sintomas):
    explicacion = {}
    conclusiones = {}

    for sintoma in sintomas:
        if sintoma in base_de_conocimiento:
            for enfermedad, probabilidad in base_de_conocimiento[sintoma].items():
                if enfermedad in conclusiones:
                    conclusiones[enfermedad] += probabilidad
                else:
                    conclusiones[enfermedad] = probabilidad
                # Guardar la explicación de cómo se llegó a esta conclusión
                if enfermedad not in explicacion:
                    explicacion[enfermedad] = []
                explicacion[enfermedad].append(f"Se observó el síntoma '{sintoma}', lo que sugiere un {probabilidad*100:.1f}% de probabilidad de {enfermedad}.")
        else:
            print(f"Sintoma desconocido: {sintoma}")

    # Ordenar conclusiones por probabilidad
    conclusiones = dict(sorted(conclusiones.items(), key=lambda item: item[1], reverse=True))
    
    return conclusiones, explicacion


def ejecutar_orden(conclusion, explicacion):
    if conclusion:
        enfermedad, probabilidad = list(conclusion.items())[0]
        print(f"\nAcción Sugerida: Diagnóstico de {enfermedad} con una probabilidad del {probabilidad*100:.1f}%.")
        # Explicar la acción
        subsistema_explicacion(enfermedad, explicacion[enfermedad])
    else:
        print("No se pudo llegar a una conclusión basada en la información proporcionada.")


def subsistema_explicacion(enfermedad, explicacion_detalles):
    print(f"\nExplicación del Diagnóstico para {enfermedad}:")
    for detalle in explicacion_detalles:
        print(f"- {detalle}")



def interfaz_usuario():
    print("Bienvenido al Sistema Experto de Diagnóstico Médico")
    
    while True:
        sintomas = input("Por favor, ingrese los síntomas del paciente separados por comas (o 'salir' para terminar): ").strip().lower()
        if sintomas == 'salir':
            print("Gracias por usar el sistema experto. ¡Hasta luego!")
            break

        sintomas_lista = [s.strip() for s in sintomas.split(",")]

        # Diagnóstico basado en los síntomas proporcionados
        conclusiones, explicacion = motor_inferencia(sintomas_lista)
        
        # Ejecución de la acción sugerida y explicación
        ejecutar_orden(conclusiones, explicacion)
        
        print("\n----------------------------------------\n")
