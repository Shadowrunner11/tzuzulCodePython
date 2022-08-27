# Hallar la suma de los 100 primeros numeros enteros positivos

# while

# 1+ 2+ 3 + 4 + ..+ 100 
# empieza en 1 y termina en 100
# contador = 1 y while(contador<=100): ...proceso

#O(n)
resultado = 0
contador  = 1

while(contador<=100):
  # aca va la logica para actualizar el resultado
  # el resultado es un acumulador asi que hay actualzar utilizando su valor prio
  resultado+=contador # resultado = resutlado + contador
  contador+=1 # contador = contador + 1

print("🐍", resultado)


# Otra forma
#O(1)
print("🐍 mas easy", 100*101//2)
