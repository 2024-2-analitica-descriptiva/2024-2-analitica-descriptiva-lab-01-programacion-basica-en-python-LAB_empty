"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    
    lineas = open("files/input/data.csv", "r").readlines()
    lineas = [z.replace('\n','') for z in lineas]
    lineas = [z.split("\t")for z in lineas]
    lineas
    x = [t[2].split('-')[1] for t in lineas[0:]]
    
    from collections import Counter
    Y = sorted(list(Counter(x).items()))

    return (Y)
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
