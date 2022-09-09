# lista de listas

lista_listas = [
  [1, 2],
  [3, 4]
]

print(lista_listas[0]) # estoy accediendo a la primera lista

print(lista_listas[0][0]) # estoy accediendo al primer elemento de la primera lista

print(lista_listas[0][1]) # estoy accediendo al segundo elemento de la primera lista


matriz_cuadrada_2 = [
  ['00', '01'],
  ['10', '11']
]

matriz_cuadrada_3 = [
  ['00','01','02'],
  ['10','11','12'],
  ['20','21','22']
]

print("🐍 Line: 26 | matriz_cuadrada_3", matriz_cuadrada_3)
print("🐍 Line: 27 | elemento(1,0)", matriz_cuadrada_3[1][0])


matriz_cuadrada_3 = [
  [1, 2,5],
  [1, 12, 6],
  [10, 22, 1]
]

limite = len(matriz_cuadrada_3) # cuantas listas hay en la lista, es decir cunatas filas
diagonal_principal = 0
for index in range(limite):
  # sumar a diagonal_principal cada elemento de la diagonal principal
  diagonal_principal+= matriz_cuadrada_3[index][index]

"""   
matriz_cuadrada_3[0][-1]
matriz_cuadrada_3[1][-2]
matriz_cuadrada_3[2][-3] 
"""
diagonal_secundaria = 0
for index in range(limite):
  diagonal_secundaria+=matriz_cuadrada_3[index][-1*(index+1)]

print(abs(diagonal_secundaria - diagonal_principal))

