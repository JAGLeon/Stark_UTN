from data_heroes import lista_personajes
from functions_heroes import *
all_campos = ['nombre','identidad','empresa','altura','peso','genero','color_ojos','color_pelo','fuerza','inteligencia']

def menu():
    print("""
    A - superhéroe de género M.
    B - superhéroe de género F.
    C - superhéroe más alto de género M.
    D - superhéroe más alto de género F.
    E - superhéroe más bajo de género M.
    F - superhéroe más bajo de género F.
    G - altura promedio de los superhéroes de género M.
    H - altura promedio de los superhéroes de género F.
    I - superhéroe más alto de género M & superhéroe más bajo de género F.
    J - superhéroes con cada tipo de color de ojos.
    K - superhéroes con cada tipo de color de pelo.
    L - superhéroes con cada tipo de inteligencia.
    M - superhéroes agrupados por color de ojos.
    N - superhéroes agrupados por color de pelo.
    O - superhéroes agrupados por color de inteligencia.
    S - SALIR
    """)
    return input("\nSeleccione una opcion del menu : \n").lower()

while True:
    match menu():
        case "a":
            mostrar_lista(filtrar_lista(lambda heroe: heroe["genero"] == "G",lista_personajes),["nombre"])
        case "b":
            mostrar_lista(filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes),["nombre"])
        case "c":
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
        case "d":
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
        case "e":
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
        case "f":
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
        case "g":
            lista_filtrada_g = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
            lista_filtrada_a = filtrar_atributo("altura",lista_filtrada_g)
            print(f"promedio altura M : {promedio_lista(lista_filtrada_a)}")
        case "h":
            lista_filtrada_f = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
            lista_filtrada_a = filtrar_atributo("altura",lista_filtrada_f)
            print(f"promedio altura F : {promedio_lista(lista_filtrada_a)}")
        case "i":
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
            print()
            lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
            heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
            mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
        case "j":
            mostrar_dictionary(contador_campo_repetido("color_ojos",lista_personajes))
        case "k":
            mostrar_dictionary(contador_campo_repetido("color_pelo",lista_personajes))
        case "l":
            mostrar_dictionary(contador_campo_repetido("inteligencia",lista_personajes))
        case "m":
            mostrar_dictionary_lista(agrupar_elementos("color_ojos",lista_personajes),all_campos)
        case "n":
            mostrar_dictionary_lista(agrupar_elementos("color_pelo",lista_personajes),all_campos)
        case "o":
            mostrar_dictionary_lista(agrupar_elementos("inteligencia",lista_personajes),all_campos)
        case "s":
            break