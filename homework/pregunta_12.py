"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    
    file = open("files/input/data.csv", "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file]

    # Creo un diccionario para almacenar la suma por de los múmeros en el index(4) cada letra del index (0)
    sums_dict = {}

    # Itero sobre los datos previamente organizados
    for sublist in x:
        words = sublist[0]
        values = sublist[4].split(',')


        #Calculo la suma de los números en el index(4)
        total_sum = sum(int(value.split(':')[1]) for value in values)

        # Actualizo la suma en el diccionario
        if words in sums_dict:
            sums_dict[words] += total_sum #si la letra yá está, le sumo el valor
        else:
            sums_dict[words] = total_sum #si la letra no está, la creo en el diccionario y le sumo el valor.
        sorted_dict = {word: sums_dict[word] for word in sorted(sums_dict)}
    return sorted_dict

    
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
