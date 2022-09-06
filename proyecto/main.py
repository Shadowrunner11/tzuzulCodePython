from luhn import luhn

stdIn = ''
while True:
  try:
    stdIn = input('Ingrese un numero de tarjeta a validar\n')
    stdIn = int(stdIn)
    if stdIn < 0:
      raise Exception('No se admite negativos')
    break
  except:
    print('Ingrese un numero entero')

if __name__ == '__main__':
  result = luhn(stdIn)
  print("🐍 ", "Numero valido" if result else "Numero invalido")

