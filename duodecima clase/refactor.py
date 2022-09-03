def descomponer(numero: int) -> list:
  """
  Funcion para descomponer un entero positivo
  en sus cifras
  """
  cifras = []

  while(numero>0):
    cifra  = numero%10
    numero = numero//10
    cifras.insert(0, cifra)

  return cifras

resultado = descomponer(1324)

print("🐍resultado",resultado)


