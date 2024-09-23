import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="chatbot"
)
cursor = conn.cursor()

# Crear la tabla 'respuestas' si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS respuestas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        pregunta VARCHAR(255) NOT NULL,
        respuesta VARCHAR(255) NOT NULL
    )
""")

# Preguntas precargadas
preguntas_precargadas = [
    ("Como estas", "Estoy bien, gracias por preguntar."),
    ("De que te gustaría hablar", "Podemos hablar de cualquier tema que te interese.")
]

# Insertar preguntas precargadas si no existen en la base de datos
for pregunta, respuesta in preguntas_precargadas:
    cursor.execute("SELECT * FROM respuestas WHERE pregunta = %s", (pregunta,))
    result = cursor.fetchone()
    # Convertir el mensaje del usuario a minúsculas
    respuesta = respuesta.lower()
    if not result:
        cursor.execute("INSERT INTO respuestas (pregunta, respuesta) VALUES (%s, %s)", (pregunta, respuesta))
        conn.commit()

# Función para obtener respuesta del chatbot
def obtener_respuesta(pregunta):
    cursor.execute("SELECT respuesta FROM respuestas WHERE pregunta = %s", (pregunta,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        nueva_pregunta = input("No conozco la respuesta a eso. ¿Cuál debería ser la respuesta? ")
        nueva_pregunta = nueva_pregunta.lower()
        cursor.execute("INSERT INTO respuestas (pregunta, respuesta) VALUES (%s, %s)", (pregunta, nueva_pregunta))
        conn.commit()
        return "Gracias por enseñarme algo nuevo."

# Bucle principal del chatbot
def chatbot():
    print("¡Hola! Soy tu chatbot. Pregúntame algo. Si deseas salir, solo escribe algunas de estas palabras (-salir- , -adios- , -exit-)")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ["salir", "adios", "exit"]:
            print("Chatbot: ¡Adiós!")
            break
        respuesta = obtener_respuesta(pregunta)
        print(f"Chatbot: {respuesta}")

# Ejecutar el chatbot
chatbot()

# Cerrar la conexión a la base de datos al finalizar
cursor.close()
conn.close()


