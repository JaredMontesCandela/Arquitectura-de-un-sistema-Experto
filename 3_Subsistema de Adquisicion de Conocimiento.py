# -*- coding: utf-8 -*-
"""

@author: jared
Mecatronica
7E  21310114

Para ilustrar cómo se podría implementar un Subsistema de Adquisición de Conocimiento en un
sistema experto utilizando Python, vamos a simular un sistema que:
1-Recibe nuevo conocimiento de un experto humano.
2-Verifica si el conocimiento es nuevo y, si es así, lo agrega a la base de conocimiento.
3-Actualiza la base de conocimiento si el conocimiento recibido es válido y nuevo.
"""

"Partimos de una base de conocimiento que contiene algunas reglas básicas sobre enfermedades y síntomas:"
# Base de Conocimiento Inicial
base_de_conocimiento = {
    "fiebre": ["gripe", "infección bacteriana", "COVID-19"],
    "tos": ["gripe", "COVID-19", "asma"],
    "dolor de cabeza": ["migraña", "gripe", "tensión alta"]
}


"El Subsistema de Adquisición de Conocimiento se encargará de verificar si el conocimiento recibido es nuevo y, en ese caso, lo añadirá a la base de conocimiento:"
# Subsistema de Adquisición de Conocimiento
def agregar_nuevo_conocimiento(sintoma, enfermedades_asociadas):
    if sintoma in base_de_conocimiento:
        conocimiento_existente = set(base_de_conocimiento[sintoma])
        nuevas_enfermedades = set(enfermedades_asociadas) - conocimiento_existente
        
        if nuevas_enfermedades:
            print(f"Agregando nuevas enfermedades para el síntoma '{sintoma}': {nuevas_enfermedades}")
            base_de_conocimiento[sintoma].extend(nuevas_enfermedades)
        else:
            print(f"El conocimiento para el síntoma '{sintoma}' ya está en la base de conocimiento.")
    else:
        print(f"Agregando un nuevo síntoma '{sintoma}' con sus enfermedades asociadas.")
        base_de_conocimiento[sintoma] = enfermedades_asociadas



" simulamos el proceso donde el experto humano proporciona nuevo conocimiento, y el sistema lo verifica y lo añade si es necesario:"
# Simulación de Adquisición de Conocimiento
nuevo_conocimiento_1 = ("dolor muscular", ["COVID-19", "lesión muscular"])
nuevo_conocimiento_2 = ("fiebre", ["infección viral", "malaria"])
nuevo_conocimiento_3 = ("tos", ["neumonía"])  # Ya existe 'tos', pero se añade 'neumonía'
nuevo_conocimiento_4 = ("fiebre", ["gripe"])  # 'gripe' ya está asociado con 'fiebre'

# Procesamos el nuevo conocimiento
agregar_nuevo_conocimiento(*nuevo_conocimiento_1)
agregar_nuevo_conocimiento(*nuevo_conocimiento_2)
agregar_nuevo_conocimiento(*nuevo_conocimiento_3)
agregar_nuevo_conocimiento(*nuevo_conocimiento_4)

print("\nBase de Conocimiento Actualizada:")
for sintoma, enfermedades in base_de_conocimiento.items():
    print(f"{sintoma}: {enfermedades}")
