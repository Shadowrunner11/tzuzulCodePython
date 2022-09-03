# Encontrar el numero mas grande dado una lista de numeros positivos desordenada

# Ejemplo de lista
mi_lista  = [1, 4, 20, 28, 32, 34 , 36, 37, 51, 21, 1, 23, 19, 8]

posicion = 0
longitud_lista = len(mi_lista)

# recorrer la lista
""" 
while(stepper < longitud_lista):
  print("🐍 ", mi_lista[stepper])
  stepper+=1 
"""
mayor = 0 

# anidamos una condicional en un bucle
while(posicion < longitud_lista):
  numero_temporal = mi_lista[posicion]
  if(numero_temporal > mayor):
    mayor = numero_temporal     #reasignamos

  posicion+=1

print("\n🐍", mayor)




