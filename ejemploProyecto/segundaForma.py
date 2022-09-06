def luhn_checker(number: int):
  resultado = 0
  parsed_number = str(number)
  len_number = len(parsed_number) 

  for index in range(len_number): #[0,1,2,3,4,5,6,...,len_number-1]
    digito = int(parsed_number[index])

    if index%2 == 0: # verificacion si es par
      digito*=2
      if digito > 9:
        digito-=9

    resultado+=digito

  return resultado%10 == 0  

resultado = luhn_checker(132643)

print(resultado)

