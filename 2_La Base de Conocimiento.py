# -*- coding: utf-8 -*-
"""

@author: jared
Mecatronica
7E  21310114

Para ilustrar cómo se maneja la "Base de Conocimiento" en un sistema experto en Python, crearemos
un ejemplo relacionado con el diagnóstico médico. En este ejemplo, la Base de Conocimiento
contendrá reglas generales sobre enfermedades y síntomas, mientras que la Base de Hechos 
(o memoria de trabajo) se llenará con los síntomas específicos de un paciente.
"""

# Base de Conocimiento: Reglas generales sobre síntomas y enfermedades
base_de_conocimiento = {
    "fiebre": ["gripe", "infección bacteriana", "COVID-19"],
    "tos": ["gripe", "COVID-19", "asma"],
    "dolor de cabeza": ["migraña", "gripe", "tensión alta"],
    "dificultad para respirar": ["asma", "COVID-19", "neumonía"],
    "dolor muscular": ["gripe", "COVID-19", "lesión muscular"],
    "pérdida de olfato": ["COVID-19"]
}
# Motor de Inferencia: Deducción basada en los síntomas del paciente
def inferir_enfermedad(sintomas_paciente):
    posibles_enfermedades = {}
    
    for sintoma in sintomas_paciente:
        if sintoma in base_de_conocimiento:
            enfermedades = base_de_conocimiento[sintoma]
            for enfermedad in enfermedades:
                if enfermedad in posibles_enfermedades:
                    posibles_enfermedades[enfermedad] += 1
                else:
                    posibles_enfermedades[enfermedad] = 1
    
    # Ordenamos las enfermedades posibles por número de coincidencias de síntomas
    posibles_enfermedades = sorted(posibles_enfermedades.items(), key=lambda x: x[1], reverse=True)
    
    return posibles_enfermedades

# Ejemplo de síntomas reportados por un paciente
sintomas_paciente = ["fiebre", "tos", "dolor muscular", "pérdida de olfato"]

# Usamos el motor de inferencia para deducir posibles enfermedades
enfermedades_sugeridas = inferir_enfermedad(sintomas_paciente)

print("\nDiagnóstico basado en los síntomas del paciente:\n")
for enfermedad, coincidencias in enfermedades_sugeridas:
    print(f"{enfermedad} (coincidencia de {coincidencias} síntomas)")
