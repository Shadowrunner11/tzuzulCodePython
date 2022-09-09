
matriz_cuadrada_3 = [
  [1, 2,5],
  [1, 12, 6],
  [10, 22, 1]
]

limite = len(matriz_cuadrada_3) # cuantas listas hay en la lista, es decir cuantas filas
diagonal_principal = 0
diagonal_secundaria = 0

for index in range(limite):
  # sumar a diagonal_principal cada elemento de la diagonal principal
  diagonal_principal+= matriz_cuadrada_3[index][index]
  # sumar a diganal_secundaria cada elemento de la diagonal secundaria
  # primera fila, ultima columna
  # segunda fila, dos columnas desde el final, hacia atras
  # tercera fila, tres columnas desde el final, hacia atras
  diagonal_secundaria+=matriz_cuadrada_3[index][-1*(index+1)]



print(abs(diagonal_secundaria - diagonal_principal))