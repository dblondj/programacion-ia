# Problema 2: frecuencia de palabras en un texto

def frecuencia_palabras(palabras, ruta):
    # Creo el diccionario con cada palabra buscada y frecuencia 0
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra.lower()] = 0

    # Signos de puntuación que hay que quitar del texto
    signos = ".,;:!?¡¿()\"'-"

    fichero = open(ruta, "r", encoding="utf-8")
    for linea in fichero:
        linea = linea.lower()  # todo a minúsculas
        for signo in signos:
            linea = linea.replace(signo, "")  # quito los signos de puntuación
        for palabra in linea.split():
            # Si la palabra está en el diccionario, sumo 1 a su frecuencia
            if palabra in frecuencias:
                frecuencias[palabra] = frecuencias[palabra] + 1
    fichero.close()

    return frecuencias


# Programa de prueba
buscadas = ["Python", "inteligencia", "la", "java", "artificial"]
resultado = frecuencia_palabras(buscadas, "texto_ejemplo.txt")

# Muestro las palabras ordenadas
for palabra in sorted(resultado):
    print(palabra + ": " + str(resultado[palabra]))