# -*- coding: utf-8 -*-
"""
@author: jared
Mecatronica
7E  21310114
Para implementar un ejemplo del Subsistema de Adquisición de Conocimiento en Python,
podemos simular un escenario donde el motor de inferencia no puede llegar a una conclusión
debido a la falta de conocimiento, y, por lo tanto, solicita información adicional del usuario para
continuar con el proceso de inferencia. Este subsistema también verificará la consistencia de la
información proporcionada antes de integrarla en la base de conocimiento.
"""

# Base de Conocimiento Inicial
base_de_conocimiento = {
    "fiebre": {"gripe": 0.7, "COVID-19": 0.9},
    "tos": {"gripe": 0.6, "COVID-19": 0.8}
}


# Comprobación de la Consistencia
def comprobar_consistencia(nuevas_enfermedades):
    suma_probabilidades = sum(nuevas_enfermedades.values())
    if suma_probabilidades <= 1.0:
        return True
    else:
        print("La suma de las probabilidades excede 1.0, lo que es inconsistente.")
        return False

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
    
    if respuesta == "si":
        nuevas_enfermedades = {}
        while True:
            enfermedad = input("Nombre de la enfermedad: ").strip()
            probabilidad = float(input(f"Probabilidad de que {enfermedad} esté asociada con {sintoma} (0 a 1): ").strip())
            nuevas_enfermedades[enfermedad] = probabilidad
            otra = input("¿Agregar otra enfermedad? (si/no): ").strip().lower()
            if otra != "si":
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


# Síntomas reportados por el paciente
sintomas_reportados = ["fiebre", "tos", "dolor de cabeza"]

# Diagnóstico con adquisición de conocimiento
resultado = motor_inferencia_con_adquisicion(sintomas_reportados)
print("\nResultado del Diagnóstico:")
for enfermedad, probabilidad in resultado.items():
    print(f"{enfermedad}: Probabilidad acumulada = {probabilidad:.2f}")
