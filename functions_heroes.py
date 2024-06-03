def mostrar_lista_campos(lista,campos):
    print()
    for elem in lista:
       mostrar_elemento_por_campos(elem, campos) 
       print()

def mostrar_elemento_por_campos(elemento, campos):
    print()
    for campo in campos:
        valor = elemento.get(campo, "No existe")
        print(f"{valor}", end = " ")

def mostrar_dictionary(dict):
    for x , y in dict.items():
        print(f"{x} => {y}")

def mostrar_dictionary_lista_campos(dict,campos):
    for clave, listas in dict.items():
        print(f"\nclave {clave} :")
        mostrar_lista_campos(listas,campos)

def filtrar_lista(funct,lista):
    lista_filtrada = []
    for elem in lista:
        if funct(elem):
            lista_filtrada.append(elem)
    return lista_filtrada

def filtrar_atributo(atributo,lista):
    lista_filtrada = []
    for elem in lista:
        lista_filtrada.append(elem[atributo])
    return lista_filtrada

def comprar_items(fun, lista):     
    bandera = True     
    for i in lista:         
        if bandera or fun(i, item):             
            bandera = False
            item = i
    return item

def sumar_lista(lista):
    suma = 0
    for elem in lista:
        suma += float(elem)
    return suma

def promedio_lista(lista):
    return sumar_lista(lista) / len(lista)
    
def agrupar_elementos(clave,lista):
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

######################Funciones Especificas#######################
def lista_masculinos(lista):
    lista_heroes = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista)
    return lista_heroes

def lista_femeninos(lista):
    return filtrar_lista(lambda heroe: heroe["genero"] == "F",lista)

def heroe_alto(lista):
    lista_heroes = lista_masculinos(lista)
    return comprar_items(lambda h1,h2: float(h1["altura"]) > float(h2["altura"]),lista_heroes)

def heroe_bajo(lista):
    lista_heroes = lista_masculinos(lista)
    return comprar_items(lambda h1,h2: float(h1["altura"]) < float(h2["altura"]),lista_heroes)

def heroina_alta(lista):
    lista_heroinas = lista_femeninos(lista)
    return comprar_items(lambda h1,h2: float(h1["altura"]) > float(h2["altura"]),lista_heroinas)

def heroina_baja(lista):
    lista_heroinas = lista_femeninos(lista)
    return comprar_items(lambda h1,h2: float(h1["altura"]) < float(h2["altura"]),lista_heroinas)

def promedio_altura_masculinos(lista):
    lista_heroes = lista_masculinos(lista)
    lista_alturas = filtrar_atributo("altura",lista_heroes)
    return promedio_lista(lista_alturas)

def promedio_altura_femeninos(lista):
    lista_heroinas = lista_femeninos(lista)
    lista_alturas = filtrar_atributo("altura",lista_heroinas)
    return promedio_lista(lista_alturas)

def supers_altos_bajos(lista):
    return [heroe_alto(lista),heroina_alta(lista),heroe_bajo(lista),heroina_baja(lista)]

def color_ojos_repetidos(lista):
    dic_new = {}
    dic = agrupar_elementos("color_ojos",lista) 
    for clave in dic:
        dic_new[clave] = len(dic[clave])
    return dic_new

def color_pelo_repetidos(lista):
    dic_new = {}
    dic = agrupar_elementos("color_pelo",lista) 
    for clave in dic:
        dic_new[clave] = len(dic[clave])
    return dic_new

def inteligencia_repetidos(lista):
    dic_new = {}
    dic = agrupar_elementos("inteligencia",lista) 
    for clave in dic:
        dic_new[clave] = len(dic[clave])
    return dic_new

def supers_color_ojos(lista):
    return agrupar_elementos("color_ojos",lista)

def supers_color_pelo(lista):
    return agrupar_elementos("color_pelo",lista)

def supers_inteligencia(lista):
    return agrupar_elementos("inteligencia",lista)

