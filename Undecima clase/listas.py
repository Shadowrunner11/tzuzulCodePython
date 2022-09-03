# listas

# creacion literal

mi_lista = [ 1, 2, 3, 4, 20, 24, 28 ]

#  index     0  1  2  3   4    5  6
#  pseudo   -7 -6  -5 -4  -3  -2 -1 

# las listas son iterables y de acceso a traves de su indice

primer_elemento_lista = mi_lista[0]
segundo_elemento_lista = mi_lista[1]

# slicing
slice = mi_lista[3:6]

print("🐍 File: Undecima clase/listas.py | Line: 17 | undefined ~ silice",slice)

slice_con_step = mi_lista[1:6:2]
print("🐍 File: Undecima clase/listas.py | Line: 20 | undefined ~ silice_con_step",slice_con_step)

slice_omision_final = mi_lista[3:]
print("🐍 File: Undecima clase/listas.py | Line: 23 | undefined ~ slice_con_omision",slice_omision_final)

slice_omision_inicio =mi_lista[:4]

print("🐍 File: Undecima clase/listas.py | Line: 26 | undefined ~ slice_omision_inicio",slice_omision_inicio)

slice_only_step = mi_lista[::2]
print("🐍 File: Undecima clase/listas.py | Line: 30 | undefined ~ slice_only_step",slice_only_step)

elemento_desc = mi_lista[-4]
print("🐍 File: Undecima clase/listas.py | Line: 33 | undefined ~ elemento",elemento_desc)