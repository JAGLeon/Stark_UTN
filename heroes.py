from data_heroes import lista_personajes
from functions_heroes import *
all_campos = ['nombre','identidad','empresa','altura','peso','genero','color_ojos','color_pelo','fuerza','inteligencia']

# mostrar_atributo(lambda heroe: heroe["genero"] == "M","nombre",lista_personajes)
# mostrar_atributo(lambda heroe: heroe["genero"] == "F","nombre",lista_personajes)

# lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
# heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
# mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)

# lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
# heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
# mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)

# lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
# heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
# mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)

# lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
# heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
# mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)

# lista_filtrada_g = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista_personajes)
# lista_filtrada_a = filtrar_atributo("altura",lista_filtrada_g)
# print(f"promedio altura M : {promedio_lista(lista_filtrada_a)}")

# lista_filtrada_f = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista_personajes)
# campos = ["nombre","genero","altura"]
# mostrar_lista(lista_filtrada_f,campos)
# lista_filtrada_a = filtrar_atributo("altura",lista_filtrada_f)
# print(f"promedio altura F : {promedio_lista(lista_filtrada_a)}")


# def informe_heroina_baja_heroe_alto(lista):
#     lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "M",lista)
#     heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) < float(h2),"altura",lista_filtrada)
#     mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)
#     print()
#     lista_filtrada = filtrar_lista(lambda heroe: heroe["genero"] == "F",lista)
#     heroe_mayor_altura = buscar_mayor_menor(lambda h1,h2: float(h1) > float(h2),"altura",lista_filtrada)
#     mostrar_elemento_por_campos(heroe_mayor_altura,all_campos)


# informe_heroina_baja_heroe_alto(lista_personajes)

# mostrar_dictionary(contador_campo_repetido("color_ojos",lista_personajes))
# mostrar_dictionary(contador_campo_repetido("color_pelo",lista_personajes))
# mostrar_dictionary(contador_campo_repetido("inteligencia",lista_personajes))

# mostrar_dictionary_lista(agrupar_elementos("color_ojos",lista_personajes),all_campos)
# mostrar_dictionary_lista(agrupar_elementos("color_pelo",lista_personajes),all_campos)
# mostrar_dictionary_lista(agrupar_elementos("inteligencia",lista_personajes),all_campos)