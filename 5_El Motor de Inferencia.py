# -*- coding: utf-8 -*-
"""
@author: jared
Mecatronica
7E  21310114
Para implementar un ejemplo de un Subsistema de Control de la Coherencia en un sistema experto utilizando Python, vamos a simular un sistema que:
1-Verifica la coherencia del conocimiento nuevo antes de agregarlo a la base de conocimiento.
2-Evita la adición de conocimiento que es inconsistente con la información existente.
3-Informa al experto humano sobre cualquier inconsistencia detectada.

"""

# Base de Conocimiento Inicial (Determinista y Probabilística)
base_de_conocimiento = {
    "fiebre": {"gripe": 0.7, "COVID-19": 0.9, "infección bacteriana": 0.5},
    "tos": {"gripe": 0.6, "COVID-19": 0.8, "asma": 0.4},
    "dolor de cabeza": {"migraña": 0.9, "gripe": 0.4, "tensión alta": 0.7}
}
def motor_inferencia_determinista(sintomas):
    posibles_enfermedades = {}
    
    for sintoma in sintomas:
        if sintoma in base_de_conocimiento:
            for enfermedad, probabilidad in base_de_conocimiento[sintoma].items():
                if enfermedad in posibles_enfermedades:
                    posibles_enfermedades[enfermedad] += probabilidad
                else:
                    posibles_enfermedades[enfermedad] = probabilidad
    
    # Ordenamos las enfermedades por la suma de probabilidades
    posibles_enfermedades = dict(sorted(posibles_enfermedades.items(), key=lambda item: item[1], reverse=True))
    
    return posibles_enfermedades

def motor_inferencia_probabilistico(sintomas, certidumbre):
    posibles_enfermedades = {}
    
    for sintoma, certeza in zip(sintomas, certidumbre):
        if sintoma in base_de_conocimiento:
            for enfermedad, probabilidad in base_de_conocimiento[sintoma].items():
                probabilidad_ajustada = probabilidad * certeza
                if enfermedad in posibles_enfermedades:
                    posibles_enfermedades[enfermedad] += probabilidad_ajustada
                else:
                    posibles_enfermedades[enfermedad] = probabilidad_ajustada
    
    # Ordenamos las enfermedades por la suma de probabilidades ajustadas
    posibles_enfermedades = dict(sorted(posibles_enfermedades.items(), key=lambda item: item[1], reverse=True))
    
    return posibles_enfermedades

# Síntomas reportados por el paciente
sintomas_reportados = ["fiebre", "dolor de cabeza"]
certidumbre_sintomas = [0.7, 0.8]  # Nivel de certeza sobre cada síntoma (para el motor probabilístico)

# Diagnóstico determinista
resultado_determinista = motor_inferencia_determinista(sintomas_reportados)
print("Resultado del Diagnóstico Determinista:")
for enfermedad, probabilidad in resultado_determinista.items():
    print(f"{enfermedad}: Probabilidad acumulada = {probabilidad:.2f}")

# Diagnóstico probabilístico
resultado_probabilistico = motor_inferencia_probabilistico(sintomas_reportados, certidumbre_sintomas)
print("\nResultado del Diagnóstico Probabilístico:")
for enfermedad, probabilidad in resultado_probabilistico.items():
    print(f"{enfermedad}: Probabilidad ajustada = {probabilidad:.2f}")

