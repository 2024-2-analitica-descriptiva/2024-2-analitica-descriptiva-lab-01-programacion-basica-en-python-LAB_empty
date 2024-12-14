"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    
    file = open("files/input/data.csv", "r").readlines() #abro el archivo y lo leo linea por linea
    x = [z.replace('\n', '') for z in file] 
    x = [z.split('\t') for z in file] 
    dict = [z[4] for z in x] 
    dict1 = [z.replace('\n', '') for z in dict] 
    dict_splt = [z.split(',') for z in dict1]
    dict_splt1 = [[','.join(z.split(':')) for z in sublist] for sublist in dict_splt]
    dict_splt2 = [[(z.split(',')) for z in sublist] for sublist in dict_splt1]

    l1 = []
    for sublist in dict_splt2:
        for item in sublist:
            l1.append(item)


    words = [z[0]for z in l1]  
    numbers= [int(z[1])for z in l1]  

    new_list = []
    for i in range(len(words)):
            new_list.append((words[i], numbers[i]))


    # Create an empty dictionary to store the count of each key
    count_dict = {}

    # Iterate over each element in the list
    for item in new_list:
        key = item[0]  # Extract the key (first element of the inner list)
        if key in count_dict:
            count_dict[key] += 1  # Increment the count if the key already exists in the dictionary
        else:
            count_dict[key] = 1  # Initialize the count to 1 if the key does not exist in the dictionary
    # Sorting the dictionary by keys in alphabetical order
    sorted_dict = {key: count_dict[key] for key in sorted(count_dict)}
    
    return sorted_dict

    
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
