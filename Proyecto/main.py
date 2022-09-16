
""" user_response = getInput(
  [
    "Si",
    "No"
  ]
)

print('🐍 ', 'el usuario escogio', user_response)
 """


from utils.main import getInput


user_response = getInput(
  [
    'Agarrar la espada',
    'Correr',
    'Dialogar'
  ]
)

if user_response == 1:
  print('Has escogido pelear')
  getInput([
    'Ataque rapido',
    'Ataque pesado'
  ])

elif user_response == 2:
  print('En pleno escape te han matado, game over')

elif user_response == 3:
  print('No te han eschando y te han rbado todas tus pertenecias')
  getInput([
    'Perseguir a los ladrones',
    'Escapar al pueblo',
    'Pedir ayuda gritando'
  ])