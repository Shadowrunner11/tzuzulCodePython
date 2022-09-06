def luhn (number: int, verification_digit: int = 0) -> bool:
  """
  Luhn checker if credit card number is valid 
  not considering verification last digit
  """
  resultado = 0
  flag = False
  while number>0:
    cifra = number%10

    if flag:
      cifra*=2
      if cifra > 9:
        cifra-=9

    flag = not flag
    resultado += cifra
    number//=10

  return resultado%10 == verification_digit


def luhn (number: str)-> bool:
  for digit in number:
    digit = int(digit)
    


""" test = [
  49927398716,
  49927398717,
  1234567812345678,
  1234567812345670
]

print([luhn(x) for x in test])
    """

