def getInput(options: list)-> int:
  if(len(options) == 0):
    raise Exception('No hay suficintes opciones para mostrar')
    
  printOptions(options)

  stdin = input('Ingrese su elección\n')

  while True:
    if isValidInput(stdin, len(options)):
      return int(stdin)
    
    stdin = input('Reintenlo no es una opcion valida\n')


def printOptions(options: list):
  for index in range(len(options)):
    print(f'{index+1}. {options[index]}')


def isValidInput(input: str, length: int) -> bool:
  try:
    input = int(input)
    return 1 <= input <= length
  except ValueError:
    return False