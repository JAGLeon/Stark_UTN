def mostrar_lista(lista,campos):
    for elem in lista:
       mostrar_elemento_por_campos(elem, campos) 
       print()

def mostrar_elemento_por_campos(elemento, campos):
    for campo in campos:
        valor = elemento.get(campo, "No existe")
        print(f"{valor}", end = " ")

def mostrar_atributo(funct,atributo,lista)->None:
    for elem in lista:
        if funct(elem):
            print(elem[atributo])

def filtrar_lista(funct,lista):
    lista_filtrada = []
    for elem in lista:
        if funct(elem):
            lista_filtrada.append(elem)
    return lista_filtrada

def buscar_mayor_menor(funct,atributo,lista):
    tam = len(lista)
    valor_mayor_menor = lista[0][atributo]
    item = lista[0]

    for i in range(1,tam):
        nuevo_mayor_menor = lista[i][atributo]
        if funct(valor_mayor_menor, nuevo_mayor_menor):
            valor_mayor_menor = nuevo_mayor_menor
            item = lista[i]

    return item

def filtrar_atributo(atributo,lista):
    lista_filtrada = []
    for elem in lista:
        lista_filtrada.append(elem[atributo])
    return lista_filtrada

def sumar_lista(lista):
    suma = 0
    for elem in lista:
        suma += float(elem)
    return suma

def promedio_lista(lista):
    return sumar_lista(lista) / len(lista)

def contador_campo_repetido(campo,lista):
    contador = {}
    for elem in lista:
        cam_rep = elem.get(campo, "No existe")
        if cam_rep == "":
            cam_rep = "No Tiene"
            
        if cam_rep in contador:
            contador[cam_rep] += 1
        else:
            contador[cam_rep] = 1
    return contador
    
def agrupar_elementos(campo,lista):
    agrupador = {}
    for elem in lista:
        cam_rep = elem.get(campo, "No existe")
        if cam_rep == "":
            cam_rep = "No Tiene"
            
        if cam_rep in agrupador:
            agrupador[cam_rep].append(elem)
        else:
            agrupador[cam_rep] = [elem]
    return agrupador

def mostrar_dictionary(dict):
    for x , y in dict.items():
        print(f"{x} => {y}")

def mostrar_dictionary_lista(dict,campos):
    for clave, listas in dict.items():
        print(f"\nclave {clave} :")
        mostrar_lista(listas,campos)