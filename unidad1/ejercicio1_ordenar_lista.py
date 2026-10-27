# Problema 1: procesamiento de una lista de enteros

def procesar_lista(lista):
    resultado = []
    for numero in lista:
        # Guardo el número solo si no es negativo y si todavía no está en la lista
        if numero >= 0 and numero not in resultado:
            resultado.append(numero)
    # Ordeno los números de menor a mayor
    resultado.sort()
    return resultado


# Programa de prueba con el ejemplo del enunciado
ejemplo = [4, -1, 2, 4, 3, -5, 2]
print("Lista original:", ejemplo)
print("Lista procesada:", procesar_lista(ejemplo))