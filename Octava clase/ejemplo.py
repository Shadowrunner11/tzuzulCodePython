nombre = input('INgrese su nombre')
def todo_Pedro():
  for i in range(10):
    print(i)

def todo_Juan():
  cont = 8
  while(cont<70):
    print('Hola')
    cont+=1

def todo_snake():
  for _ in range(80):
    print("🐍 ")

if nombre=='Pedro':
  todo_Pedro()
elif nombre=="Juan":
  todo_Juan()
else:
  todo_snake()
