def mostrar_lista_campos(lista:list,campos:list):
    print()
    for elem in lista:
       mostrar_elemento_por_campos(elem, campos) 
       print()

def mostrar_elemento_por_campos(elemento:dict, campos:list):
    print()
    for campo in campos:
        valor = elemento.get(campo, "No existe")
        print(f"{valor}", end = " ")

def mostrar_dictionary(dict:dict):
    for x , y in dict.items():
        print(f"{x} => {y}")

def mostrar_dictionary_lista_campos(dict:dict,campos:list):
    for clave, listas in dict.items():
        print(f"\nclave {clave} :")
        mostrar_lista_campos(listas,campos)

def filtrar_lista(funct:function,lista:list)->list:
    lista_filtrada = []
    for elem in lista:
        if funct(elem):
            lista_filtrada.append(elem)
    return lista_filtrada

def filtrar_atributo(clave:str,lista:list)->list:
    lista_filtrada = []
    for elem in lista:
        lista_filtrada.append(elem[clave])
    return lista_filtrada

def comprar_items(funct:function, lista:list)->dict:     
    bandera = True     
    for i in lista:         
        if bandera or funct(i, item):             
            bandera = False
            item = i
    return item

def sumar_lista(lista:list)->float:
    suma = 0
    for elem in lista:
        suma += float(elem)
    return suma

def promedio_lista(lista:list)->float:
    return sumar_lista(lista) / len(lista)
    
def agrupar_elementos(clave:str,lista:list)->dict:
    diccionario = {}
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
    dic_new = {}
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

