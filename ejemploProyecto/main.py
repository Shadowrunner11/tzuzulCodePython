def proccesded_number(number):
  numero_invertido = 0

  while number>0:
    cifra_final = number%10
    numero_invertido*=10+cifra_final
    number //=10

  return numero_invertido


def checkCreditCard(number):
 ...





