def descomponerNumero(numeroEntero):
  cifras = []

  while(numeroEntero>0):
    cifra  = numeroEntero%10
    numeroEntero = numeroEntero//10
    cifras.insert(0, cifra)

  return cifras

resultado = descomponerNumero(1324)

print("🐍resultado",resultado)