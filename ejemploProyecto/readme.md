# Algoritmo de Luhn


Es un algoritmo que usan los bancos para
saber si el numero de una tarjeta de credito es válida

1. Invertir el numero de la tarjeta credito
2. Duplicar las cifras de posicion impar
3. Si el resultado de duplicar es mayor que 9, sumar las cifras
4. Sumar los resultados con las cifras de posicion par
5. Dividir entre 10, si no hay residuo es un numero valido

## Ejemplo

132643

Invertmos el numero y nos da 346 231

|Posicion|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|Numero|3|4|6|2|3|1|
|Multiplicador|2|1|2|1|2|1
|Resultado|6|4|12|2|6|1
|Corregido|6|4|3|2|6|1

Suma = 6+4+3+2+6+1 = 22

22%10 = 2 por lo tanto no es numero valido
