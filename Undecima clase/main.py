# descomponer en cifras un numero entero

# Input: 239

# Output: [2, 3, 9]

# 1) cifra =239%10 -> 9
# 2) numero_sin_cifra = 239//10 -> 23
# volver a repetir el paso 1) y 2) ahora con numero_sin_cifra
# debe terminar cuando ya no hay nada que dividir 

def descomponer(numero):
  #proceso para descomponer
  cifras = []
  while(numero > 0):
    cifra = numero%10
    cifras.insert(0, cifra) # colocar al principio
    numero = numero//10

  print(cifras)

numero = int(input('Introduce un numero\n'))
descomponer(numero)

