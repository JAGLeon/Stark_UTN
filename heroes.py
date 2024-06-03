from data_heroes import *
from functions_heroes import *

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
    I - supers más altos & supers más bajos.
    J - superhéroes con cada tipo de color de ojos.
    K - superhéroes con cada tipo de color de pelo.
    L - superhéroes con cada tipo de inteligencia.
    M - superhéroes agrupados por color de ojos.
    N - superhéroes agrupados por color de pelo.
    O - superhéroes agrupados por color de inteligencia.
    S - SALIR.
    """)
    return input("\nSeleccione una opcion del menu : \n").lower()


while True:
    match menu():
        case "a":
            mostrar_lista_campos(lista_masculinos(lista_personajes),["nombre"])
        case "b":
            mostrar_lista_campos(lista_femeninos(lista_personajes),["nombre"])
        case "c":
            mostrar_elemento_por_campos(heroe_alto(lista_personajes),["nombre"])
        case "d":
            mostrar_elemento_por_campos(heroina_alta(lista_personajes),["nombre"])
        case "e":
            mostrar_elemento_por_campos(heroe_bajo(lista_personajes),["nombre"])
        case "f":
            mostrar_elemento_por_campos(heroina_baja(lista_personajes),["nombre"])
        case "g":
            print(f"promedio altura M : {promedio_altura_masculinos(lista_personajes)}")
        case "h":
            print(f"promedio altura F : {promedio_altura_femeninos(lista_personajes)}")
        case "i":
            mostrar_lista_campos(supers_altos_bajos(lista_personajes),["nombre"])
        case "j":
            mostrar_dictionary(color_ojos_repetidos(lista_personajes))
        case "k":
            mostrar_dictionary(color_pelo_repetidos(lista_personajes))
        case "l":
            mostrar_dictionary(inteligencia_repetidos(lista_personajes))
        case "m":
            mostrar_dictionary_lista_campos(supers_color_ojos(lista_personajes),claves)
        case "n":
            mostrar_dictionary_lista_campos(supers_color_pelo(lista_personajes),claves)
        case "o":
            mostrar_dictionary_lista_campos(supers_inteligencia(lista_personajes),claves)
        case "s":
            break


