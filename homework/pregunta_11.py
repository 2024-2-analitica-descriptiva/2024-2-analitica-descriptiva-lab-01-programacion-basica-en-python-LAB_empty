"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    
    file = open("files/input/data.csv", "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file]

    # Creo un diccionario para almacenar la suma por cada letra del index (3)
    sums_dict = {}

    # Itero sobre los datos previamente organizados
    for sublist in x:
        words = sublist[3].split(',')
        value = int(sublist[1])

        for word in words:
            # Actualizo la suma en el diccionario
            if word in sums_dict:
                sums_dict[word] += value
            else:
                sums_dict[word] = value

        sorted_dict = {word: sums_dict[word] for word in sorted(sums_dict)}
    return sorted_dict


    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
