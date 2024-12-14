"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():

    lineas = open("/Users/maferojas/GitHub/Ana_descriptiva_RPOS/Laboratorios/Test/files/input/data.csv", "r").readlines()

    y = [z.replace('\n','') for z in lineas]
    y = [z.split("\t")for z in lineas]

    y = [x[0] for x in lineas[0:]]
    from collections import Counter
    x = sorted(list(Counter(y).items()))
    return(x)

#x = pregunta_02(lineas)
#print(x)

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
