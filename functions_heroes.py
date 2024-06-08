from typing import Callable
def validar_lista(lista:list):
    '''
        Recibe una lista, en caso de no ser tipo list da un TypeError
    '''

    if not isinstance(lista,list):
        raise TypeError("Se esperaba una lista")
    
def validar_diccionario(diccionario:dict):
    '''
        Recibe una diccionario, en caso de no ser tipo dict da un TypeError
    '''

    if not isinstance(diccionario,dict):
        raise TypeError("Se esperaba una diccionario")

def validar_funcion(funct:Callable):
    '''
        Recibe una función lambda o una función regular, en caso de no ser tipo dict da un TypeError
    '''
    if not callable(funct):
        raise ValueError('El argumento proporcionado no es una función.')

def mostrar_lista_campos(lista:list,campos:list):
    '''
        Recibe una lista
        Imprime en terminal la lista
        Caso contrario da un mensaje de error
    '''

    validar_lista(lista)

    if(len(lista) > 0):
        for elem in lista:
            mostrar_elemento_por_campos(elem, campos) 
            print()
    else:
        print('ERROR: La lista no puede ser recorrida')

def mostrar_elemento_por_campos(elemento:dict, campos:list):
    print()
    for campo in campos:
        valor = elemento.get(campo, "No existe")
        print(f"{valor}", end = " ")

def mostrar_dictionary(diccionario:dict):
    '''
        Recibe un diccionario
        Imprime en terminal el diccionario
        Caso contrario da un mensaje de error
    '''

    validar_diccionario(diccionario)
    if len(diccionario) > 0:
        for clave , valor in diccionario.items():
            print(f"{clave} => {valor}")
    else: 
        print('ERROR: El diccionario no puede ser recorrido')


def mostrar_dictionary_lista_campos(diccionario:dict,campos:list):
    '''
        Recibe un diccionario con valor lista
        Imprime en terminal el diccionario
        Caso contrario da un mensaje de error
    '''

    validar_diccionario(diccionario)
    if len(diccionario) > 0:
        for clave, listas in dict.items():
            print(f"\nclave {clave} :")
            mostrar_lista_campos(listas,campos)
    else: 
        print('ERROR: El diccionario no puede ser recorrido')


def filtrar_lista(funct:Callable,lista:list)->list:
    '''
        Recibe una lista,funcion
        Filtra la lista segun la criterio que se envie en funct
        Caso contrario devuelve una lista vacia
    '''

    validar_lista(lista)
    lista_filtrada = []

    if(len(lista) > 0):
        for elem in lista:
            if funct(elem):
                lista_filtrada.append(elem)

    return lista_filtrada
#Map hace algo por cada elemento, recibe funct
def mapear_lista(funct:Callable,lista:list)->list:
    '''
        Recibe una lista,funcion
        Mapea la lista segun la criterio que se envie en funct
        Caso contrario devuelve una lista vacia
    '''

    validar_lista(lista)
    lista_filtrada = []

    if(len(lista) > 0):
        for elem in lista:
            lista_filtrada.append(funct(elem))

    return lista_filtrada


#Each modifica la lista original, recibe funct
def each_lista(funct:Callable,clave,lista:list)->list:
    '''
        Recibe una lista,funcion
        Modifica la lista original segun el criterio que se envie en funct
        Caso contrario devuelve una lista vacia
    '''

    validar_lista(lista)
    if(len(lista) > 0):
        for indice in range(len(lista)):
            lista[indice][clave] = funct(lista[indice][clave])


def filtrar_atributo(clave:str,lista:list)->list:
    lista_filtrada = []
    for elem in lista:
        lista_filtrada.append(elem[clave])
    return lista_filtrada

def comprar_items(funct, lista:list)->dict:   
    '''
        Recibe una lista de la cual filtra dependiendo del lamba
        Retorna un elemento
    '''  
    validar_lista(lista)
    if(len(lista) > 0):
        bandera = True     
        for i in lista:         
            if bandera or funct(i, item):             
                bandera = False
                item = i
        return item
    return None

def sumar_lista(lista:list)->float:
    '''
        Recibe una lista suma sus elementos
        Retorna la suma
    '''  
    validar_lista(lista)
    suma = 0

    if(len(lista) > 0):
        for elem in lista:
            suma += float(elem)
    return suma

def promedio_lista(lista:list)->float:
    '''
        Recibe una lista suma sus elementos y saca el promedio
        Retorna el promedio
    '''  
    validar_lista(lista)
    if(len(lista) > 0):
        return sumar_lista(lista) / len(lista)
    return None

def agrupar_elementos(clave:str,lista:list)->dict:
    '''
        Recibe una lista con diccionarios agrupa en un diccionario segun su valor
        Retorna un diccionario
    '''  
    validar_lista(lista)
    diccionario = {}
    if(len(lista) > 0):
        for elem in lista:
            cam_rep = elem.get(clave, "No existe")
            if cam_rep == "":
                cam_rep = "No Tiene"
                
            if cam_rep in diccionario:
                diccionario[cam_rep].append(elem)
            else:
                diccionario[cam_rep] = [elem]
    return diccionario

def contar_elementos(clave:str,lista:list)->dict:
    '''
        Recibe una lista con diccionarios agrupa en un diccionario segun su valor 
        Retorna un diccionario con las veces que se repitio ese valor
    '''  
    dic_new = {}
    if(len(lista) > 0):
        dic = agrupar_elementos(clave,lista) 
        for c in dic:
            dic_new[c] = len(dic[c])
    return dic_new

######################Funciones Especificas#######################

def lista_masculinos(lista:list)->list:
    return filtrar_lista(lambda heroe: heroe["genero"] == "M",lista)

def lista_femeninos(lista:list)->list:
    return filtrar_lista(lambda heroe: heroe["genero"] == "F",lista)

def heroe_alto(lista:list)->dict:
    return comprar_items(lambda h1,h2: float(h1["altura"]) > float(h2["altura"]),lista_masculinos(lista))

def heroe_bajo(lista:list)->dict:
    return comprar_items(lambda h1,h2: float(h1["altura"]) < float(h2["altura"]),lista_masculinos(lista))

def heroina_alta(lista:list)->dict:
    return comprar_items(lambda h1,h2: float(h1["altura"]) > float(h2["altura"]),lista_femeninos(lista))

def heroina_baja(lista:list)->dict:
    return comprar_items(lambda h1,h2: float(h1["altura"]) < float(h2["altura"]),lista_femeninos(lista))

def promedio_altura_masculinos(lista:list)->float:
    return promedio_lista(filtrar_atributo("altura",lista_masculinos(lista)))

def promedio_altura_femeninos(lista:list)->float:
    return promedio_lista(filtrar_atributo("altura",lista_femeninos(lista)))

def supers_altos_bajos(lista:list)->list:
    return [heroe_alto(lista),heroina_alta(lista),heroe_bajo(lista),heroina_baja(lista)]

def color_ojos_repetidos(lista:list)->dict:
    return contar_elementos("color_ojos",lista)

def color_pelo_repetidos(lista:list)->dict:
    return contar_elementos("color_pelo",lista)

def inteligencia_repetidos(lista:list)->dict:
    return contar_elementos("inteligencia",lista)

def supers_color_ojos(lista:list)->dict:
    return agrupar_elementos("color_ojos",lista)

def supers_color_pelo(lista:list)->dict:
    return agrupar_elementos("color_pelo",lista)

def supers_inteligencia(lista:list)->dict:
    return agrupar_elementos("inteligencia",lista)

