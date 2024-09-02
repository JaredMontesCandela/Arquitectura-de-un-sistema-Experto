# -*- coding: utf-8 -*-
"""
@author: jared
Mecatronica
7E  21310114
Para implementar un ejemplo de un Subsistema de Control de la Coherencia en un sistema experto utilizando Python, vamos a simular un sistema que:
1-Verifica la coherencia del conocimiento nuevo antes de agregarlo a la base de conocimiento.
2-Evita la adición de conocimiento que es inconsistente con la información existente.
3-nforma al experto humano sobre cualquier inconsistencia detectada.

"""


# Base de Conocimiento Inicial
base_de_conocimiento = {
    "fiebre": ["gripe", "infección bacteriana", "COVID-19"],
    "tos": ["gripe", "COVID-19", "asma"],
    "dolor de cabeza": ["migraña", "gripe", "tensión alta"]
}


"El subsistema de control de la coherencia evaluará el nuevo conocimiento para detectar posibles inconsistencias:"
# Subsistema de Control de la Coherencia
def verificar_coherencia(sintoma, enfermedades_asociadas):
    if sintoma in base_de_conocimiento:
        conocimiento_existente = set(base_de_conocimiento[sintoma])
        nuevas_enfermedades = set(enfermedades_asociadas)
        
        # Verificamos si hay alguna contradicción (por ejemplo, si una enfermedad es incompatible)
        enfermedades_inconsistentes = conocimiento_existente.intersection(nuevas_enfermedades)
        if enfermedades_inconsistentes:
            print(f"\nInconsistencia detectada para el síntoma '{sintoma}'. Las siguientes enfermedades ya están registradas: {enfermedades_inconsistentes}")
            return False
        else:
            return True
    else:
        return True

def agregar_nuevo_conocimiento(sintoma, enfermedades_asociadas):
    if verificar_coherencia(sintoma, enfermedades_asociadas):
        if sintoma in base_de_conocimiento:
            base_de_conocimiento[sintoma].extend(enfermedades_asociadas)
            print(f"Conocimiento agregado: {sintoma} -> {enfermedades_asociadas}")
        else:
            base_de_conocimiento[sintoma] = enfermedades_asociadas
            print(f"Nuevo síntoma agregado: {sintoma} -> {enfermedades_asociadas}")
    else:
        print(f"El nuevo conocimiento sobre '{sintoma}' no se agregó debido a inconsistencias.")


"Simulamos la adición de nuevo conocimiento y utilizamos el subsistema de control de coherencia para verificar su validez:"
# Simulación de Adquisición y Verificación de Conocimiento
nuevo_conocimiento_1 = ("fiebre", ["COVID-19"])  # Conocimiento ya existente, no debería causar inconsistencias
nuevo_conocimiento_2 = ("fiebre", ["resfriado común"])  # Conocimiento nuevo, coherente
nuevo_conocimiento_3 = ("dolor de cabeza", ["tensión alta"])  # Conocimiento ya existente, no debería causar inconsistencias
nuevo_conocimiento_4 = ("tos", ["asma"])  # Conocimiento ya existente, no debería causar inconsistencias
nuevo_conocimiento_5 = ("tos", ["gripe"])  # Conocimiento ya existente, podría causar inconsistencia si se propaga incorrectamente

# Procesamos el nuevo conocimiento
agregar_nuevo_conocimiento(*nuevo_conocimiento_1)
agregar_nuevo_conocimiento(*nuevo_conocimiento_2)
agregar_nuevo_conocimiento(*nuevo_conocimiento_3)
agregar_nuevo_conocimiento(*nuevo_conocimiento_4)
agregar_nuevo_conocimiento(*nuevo_conocimiento_5)

print("\nBase de Conocimiento Final:")
for sintoma, enfermedades in base_de_conocimiento.items():
    print(f"{sintoma}: {enfermedades}")


