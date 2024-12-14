"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():

    lineas = open("files/input/data.csv", "r").readlines()
    lineas = [z.replace('\n','') for z in lineas]
    lineas = [z.split("\t")for z in lineas]
    letras = [x[0] for x in lineas[0:]]
    numbers = [x[1] for x in lineas[0:]]
    numbers = list(map(int, numbers))

    lista_1 = list(zip(letras, numbers))
    resultados = {}
    
    for l, n in lista_1:
        if l in resultados:
            resultados[l] += n
    
        else:
            resultados[l] = n

    tupla = sorted(list(resultados.items()))
    return(tupla)

    
    
    
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
