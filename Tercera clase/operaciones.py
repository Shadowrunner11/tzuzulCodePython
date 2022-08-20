# adicion
suma_enteros = 4 + 6
suma_flotantes = 3.8 + 7.6
suma_flotantes2 = 1.5 + .5
suma_mixta = 3 + 1.5
print('suma de enteros', suma_enteros) # -> 10

print('suma de flotantes 1', suma_flotantes) # -> 11.3999999999
# La FPU no opera con decimal sino con binarios
# Cuando convertimos de decimal flotante a binario, el resultado binario es infinito
# El bit mas significativo se usa para el signo

print('suma de flotantes 2', suma_flotantes2) # -> 2.0

# multiplicacion
producto_enteros = 2*3 # 6
producto_flotantes = 2.3*4.3 # 9.8899999
producto_mixto = 3*8.9 # 26.7000..3

print("producto enteros", producto_enteros)
print("producto flotantes", producto_flotantes)
print("producto mixto", producto_mixto)

# division entera
cociente = 14//3 # 4
cociente_2 = 12.3//6.5 # 1.0

print(cociente)
print(cociente_2)

# divsion
resultado = 4/2 # 2.0
resultado_2 = 6/4 # 1.5

print(resultado)
print(resultado_2)

# modulo
residuo = 14%3
residuo_2 = 12.3%6.3

print(residuo)
print(residuo_2)

# potenciacion

power = 3**2 #9
print("🐍 power",power)
power_2 = 4.5**2 # 20.25
print("🐍 power_2",power_2)
power_3 = 7**3 # 343
print("🐍 power_3",power_3)


