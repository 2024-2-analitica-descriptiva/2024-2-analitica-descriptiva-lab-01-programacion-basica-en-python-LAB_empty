"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    lineas = open("/Users/maferojas/GitHub/Ana_descriptiva_RPOS/Laboratorios/Test/files/input/data.csv", "r").readlines()
    lineas = [z.replace('\n','') for z in lineas]
    lineas = [z.split("\t")for z in lineas]
    numbers = [x[1] for x in lineas[0:]]
    numbers = list(map(int, numbers))
    letras = [x[0] for x in lineas[0:]]
    lista_1 = list(zip(letras, numbers))

    from collections import defaultdict
    diccionario = defaultdict(list)

    for clave, valor in lista_1:
        diccionario[clave].append(valor)
    
    resultados = [(clave, max(valores), min(valores)) for clave, valores in diccionario.items()]
    resultados = sorted(resultados)

    return resultados

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
