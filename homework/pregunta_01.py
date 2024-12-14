"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    lineas = open("/Users/maferojas/GitHub/Ana_descriptiva_RPOS/Laboratorios/Test/files/input/data.csv", "r").readlines()
    # Limpiar saltos de línea y dividir por tabuladores
    file = [x.replace('\n', "") for x in lineas]  # Eliminar saltos de línea
    file = [x.split('\t') for x in lineas]  # Separar por tabulador

    # Extraer los números en la segunda columna y convertirlos a enteros
    numbers = [int(x[1]) for x in file]  # Asumimos que la columna 1 contiene los números

    # Calcular la suma de los números
    Rta = sum(numbers)
    return Rta

# Llamar a la función con el argumento `lineas`
#x = pregunta_01(lineas)

# Imprimir el resultado
#print(x)
#print(rta)