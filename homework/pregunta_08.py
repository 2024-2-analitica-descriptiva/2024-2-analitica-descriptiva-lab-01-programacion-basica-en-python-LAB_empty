"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
   
    file = open("files/input/data.csv", "r").readlines() #abro el archivo y lo leo linea por linea
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

    # Process each tuple to sort and remove duplicates from the list of letters
    processed_data = []
    for number, letters in final_list:
         unique_sorted_letters = sorted(set(letters))  # Remove duplicates and sort
         processed_data.append((number, unique_sorted_letters))    
    return processed_data

   
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
