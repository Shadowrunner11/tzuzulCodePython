# Teorema del programa esctructurado

#  Estructuras de control

# 1. Secuencia: Debe haber una instruccion despues de otra
# 2. Seleccion: Decidir de un grupo de posibilidades que instruccion ejecutas
# 3. Iteracion: Poder ejecutar una instruccion muchas veces

# input es una funcion propia de python que me permite pedir al usuario que escriba algo
# alamacenar el resultado del input en username para usar
# el nombre de usario en diversas partes de las respuestas
username = input('Dime tu nombre\n')
print('Hola', username)

print('Responde con [S/N]')
lavar_ropa = input('Lavaste la ropa?\n') == 'S' # Si el usario introduce S, entonces S == S saldra true
hacer_la_tarea = input('Hiciste la tarea\n') == 'S' # Si no pasara lo contrario

if(lavar_ropa and hacer_la_tarea): # true and true -> true
  print('Sí sales a la calle', username, '😻 ')
else:
  print('Te quedas castigado en la casa', username, '😥')

