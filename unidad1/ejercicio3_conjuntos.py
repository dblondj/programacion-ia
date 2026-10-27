# Problema 3: trabajo con conjuntos

def operaciones_conjuntos(lista1, lista2):
    # Convierto las listas en conjuntos (set)
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    resultado = {}
    # Elementos que están en los dos conjuntos
    resultado["interseccion"] = sorted(conjunto1.intersection(conjunto2))
    # Todos los elementos sin duplicados
    resultado["union"] = sorted(conjunto1.union(conjunto2))
    # Elementos que están en uno u otro, pero no en ambos
    resultado["diferencia_simetrica"] = sorted(conjunto1.symmetric_difference(conjunto2))
    return resultado


# Programa de prueba
lista_a = [1, 2, 3, 4, 4]
lista_b = [3, 4, 5, 6]
print("Lista 1:", lista_a)
print("Lista 2:", lista_b)
resultado = operaciones_conjuntos(lista_a, lista_b)
print("Intersección:", resultado["interseccion"])
print("Unión:", resultado["union"])
print("Diferencia simétrica:", resultado["diferencia_simetrica"])