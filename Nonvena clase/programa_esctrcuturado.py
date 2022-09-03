# Programa estructurado

# 1. Secuencia
# 2. Condicional
# 3. Iteracion

# Secuencia

print('Hola') # primero la linea 9
print('Hola 2') # luego la linea 10

# Condicional

if 4 < 5:
  print('Hola')

#-----------------------------
if 5 > 6:
  print('Mayor')
else:
  print('Menor') 
# un else no puede existir sin su respectivo if

#------------------------------
number_string = input('Ingrese un numero') # es str
number = int(number_string) # esto si es de tipo entero

if number > 9:
  print('Numero muy grande')
elif number > 5:
  print('Estas cerca')
elif number == 5:
  print('Adiviniste el numero')
else:
  print('Numero muy bajo')
