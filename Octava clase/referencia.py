x = 10

def modifier(m):
  m+=1
  print(m)

# paso por valor por ser primitivo
modifier(x)

print(x)



lista = ["pollito"]

def addPotates(list):
  list.append("papas")
  print(list)

# paso por referencia
addPotates(lista)

print(lista)