if __name__ == '__main__':
  n = int(input().strip())
  
  """ 
  if n%2 != 0: # si es impar
      print('Weird')
  if n%2 == 0 and (n >= 2 and n <=5): # si es par
      print('Not Weird')
  if n%2 == 0 and  (n >=6 and n<=20):
      print('Weird')
  if n%2 ==0 and n > 20:
      print('Not Weird') """

  # No es necesario sobrecomparar porque, por ejemplo
  # si es no entro a la condicon de ser mayor que 20
  # entonces es 20 o menos, pero se ecuentra con que debe ser
  # mayor que 5, es decir esta entre entre 6 y 20
  result = ''

  if n%2 != 0:
    result = 'Weird'
  elif n>20:
    result = 'Not Weird'
  elif n>5:
    result = 'Weird'
  elif n>1:
    result = 'Not Weird'
  
  print(result)