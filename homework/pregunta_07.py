"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

   
from collections import Counter
from collections import defaultdict
from operator import itemgetter

def pregunta_07():

    file = open("/Users/maferojas/GitHub/Ana_descriptiva_RPOS/Laboratorios/Test/files/input/data.csv", "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    letters = [z[0]for z in x]  
    numbers= [int(z[1])for z in x]  

    new_list = []
    for i in range(len(letters)):
            new_list.append((numbers[i], letters[i]))

    # Create a dictionary to group letters by numbers
    grouped_data = {}
    for number, letter in new_list:
        if number not in grouped_data:
            grouped_data[number] = []
        grouped_data[number].append(letter)

    # Convert the dictionary to a list of tuples
    result = [(number, letters) for number, letters in grouped_data.items()] 

    final_list = sorted(result, key=lambda x: x[0])

    return final_list
   
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
