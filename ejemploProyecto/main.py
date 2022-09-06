
def luhn_checker(number):
  resultado = 0
  is_odd = True

  while number>0:
    cifra_final = number%10

    if is_odd:
      cifra_final*=2 # cifra_final = cifra_final*2
      if cifra_final > 9:
        """ 
        resulta que para los numenros entre 10 y 18
        da el mismo resultado si le quitamos 9 o
        sumamos sus cifras 
        """
        cifra_final-=9 # cifra_final = cifra_final - 9
    
    is_odd = not is_odd

    resultado+=cifra_final
    number //=10 # number = number // 10

  return resultado%10 == 0


""" 
10 -> 1 + 0 = 1
11 -> 1 + 1 = 2
12 -> 1+ 2 = 3

18 -> 1 + 8 = 9 
"""

resultado = luhn_checker(132643)

print(resultado)


