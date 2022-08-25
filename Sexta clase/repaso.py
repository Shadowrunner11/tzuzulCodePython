""" se_ducho = False

buena_actitud = False

es_soberbio = False

tiene_humor = False

if(es_soberbio):
  print("No pasa")
elif(buena_actitud or se_ducho):
  print('Puede ser que pases')
elif(tiene_humor):
  print('Bueno, intentare conocerte')
else:
  print('Si le pasare mi numero pero no le voy a contestar')
 """

# Crear un algoritmo que me permita definir si se debe enviar un correo o hacer una reunion

# Si es un cambio minimo, un correo
# Si es un nuevo producto a crear, una reunion
# Si es una correcion de un error, un correo
# Si se cayo el servidor de produccion, una reunion
# Aumento de sueldo, correo
# Informe de cierre de trimestre, reunion
# Un memoradum corto, correo 


""" print('Responder con S o s si es afirmativo, con otra letra si es negativo')

es_cambio_minimo = input('es un cambio minimo?\n').lower() == 's'
es_nuevo_producto = input('es un nuevo producto?\n').lower() == 's'
es_correcion_minima = input('es una correcion minima\n').lower() == 's'

resultado = ''

if(es_cambio_minimo or es_correcion_minima):
  resultado = 'Enviar correo'
elif(es_nuevo_producto):
  resultado = 'Programar reunion'
else:
  resultado = 'Programar reunion'

print(resultado) """


# si el usario no ingresa nada como username, hacerlo entrar como invitado

http_response = input('Si tienes de usuario escribleo, sino presiona enter')
ROL = ''

if(len(http_response) == 0):
  ROL = 'invitado'
elif(http_response == 'admin'):
  ROL = 'admin'
elif(http_response == 'usuario'):
  ROL = 'usuario'
else:
  print('Error 403')

if(ROL == 'invitado'):
  print('Solo puedes mirar los post publicos')
elif(ROL == 'usuario'):
  print('Solo puedes modificar tus publicaciones')
elif(ROL == 'admin'):
  print('Puedes modificar lo que sea')
else:
  print('Usuario no autentificado')