"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():

    lineas = open("/Users/maferojas/GitHub/Ana_descriptiva_RPOS/Laboratorios/Test/files/input/data.csv", "r").readlines()
    lineas = [z.replace('\n','') for z in lineas]
    lineas = [z.split("\t")for z in lineas]
    lineas
    lista_1 = [x[4] for x in lineas[0:]]

    # Crear un diccionario para almacenar el mínimo y máximo por clave
    lista_final = {}

    for x in lista_1:
    # Separar pares clave:valor
        pares = x.split(',')
        for par in pares:
            clave, valor = par.split(':')  # Dividir cada par en clave y valor
            valor = int(valor)  # Convertir valor a entero
        
            if clave in lista_final:
                # Actualizar mínimo y máximo
                lista_final[clave] = (
                min(lista_final[clave][0], valor),  # Actualizar mínimo
                max(lista_final[clave][1], valor)   # Actualizar máximo
            )
            else:
                # Inicializar con el primer valor como mínimo y máximo
                lista_final[clave] = (valor, valor)

    # Convertir el diccionario a una lista de tuplas
    resultado = [(clave, valores[0], valores[1]) for clave, valores in lista_final.items()]
    resultado = sorted(resultado)

    return resultado

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
