import random
import time

ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'

print(AMARILLO+'*****BIENVENIDO A MI TRIVIA*****\n'+RESET)

print(AZUL+"""Hola mi nombre es Edson Effio Velasco
Pondré a prueba tus conocimientos
¿Cuál es tu nombre?"""+RESET)
nombre = input('\n: ')

print(MAGENTA+"\nHola", nombre,"""te haré unas preguntas en donde vas a contestar escribiendo la letra que creas que es correcta y luego presionas 'Enter' para enviar tu respuesta\n"""+RESET)

comienzo = input('\nPresiona enter si quieres comenzar: ')

print('\nCuenta regresiva:\n')

for i in range(5,0,-1):
  print(i)
  time.sleep(1)

print('\nComencemos')

time.sleep(1)

iniciar_trivia = True

intento = 0

while iniciar_trivia==True:

  intento += 1
  print('\nIntento',intento,'\n')

  puntaje = random.randint(0,11)

  print('Comienzas con',puntaje,'puntos\n')

  print(AMARILLO+"""1- ¿En qué año nació Albert Einstein?
a) 1847
b) 1885
c) 1879
d) 1881\n"""+RESET)

  respuesta_1 = input('Introduce tu respuesta: ')
  while respuesta_1 not in('a','b','c','d'):
    print('Ingresa las alternativas que se presenta. Vuelve a intentarlo')
    respuesta_1 = input('Introduce tu respuesta: ')
  if respuesta_1 == 'a':
    print(ROJO+'Incorrecto',nombre,'en ese año nació Thomas Edison'+RESET)
    puntaje -= random.randint(1,3)
  elif respuesta_1 == 'b':
    print(ROJO+'Incorrecto',nombre,'en ese año nació Niels Bohr'+RESET)
    puntaje -= random.randint(1,3)
  elif respuesta_1 == 'd':
    print(ROJO+'Incorrecto',nombre,'en ese año nació Alexander Fleming'+RESET)
    puntaje -= random.randint(1,3)
  else:
    print(CYAN+'Felicidades',nombre, 'acertaste'+RESET)
    puntaje += random.randint(1,3)

  print(VERDE+'\nPor el momento llevas',puntaje,'puntos'+RESET)
  time.sleep(2)

  print(AMARILLO+"""\n2- ¿Qué deporte practicaba Michael Jordan?
a) Baloncesto
b) Fútbol
c) Tenis
d) Esgrima\n"""+RESET)

  respuesta_2 = input('Introduce tu respuesta: ')
  while respuesta_2 not in('a','b','c','d'):
    print('Ingresa las alternativas que se presenta. Vuelve a intentarlo')
    respuesta_2 = input('Introduce tu respuesta: ')
  if respuesta_2 == 'b':
    print(ROJO+'Incorrecto',nombre,'ese deporte lo practica Lionel Messi'+RESET)
    puntaje -= random.randint(2,5)
  elif respuesta_2 == 'c':
    print(ROJO+'Incorrecto',nombre,'ese deporte lo practica Rafael Nadal'+RESET)
    puntaje -= random.randint(2,5)
  elif respuesta_2 == 'd':
    print(ROJO+'Incorrecto',nombre,'ese deporte lo practica Lucas Lutar'+RESET)
    puntaje -= random.randint(2,5)
  else:
    print(CYAN+'Felicidades',nombre, 'acertaste'+RESET)
    puntaje += random.randint(2,5)
  print(VERDE+'\nPor el momento llevas',puntaje,'puntos'+RESET)
  time.sleep(2)

  print(AMARILLO+"""\n3- ¿Qué se celebra el 08 de octubre en Perú?
a) Día de Todos los Santos
b) Batalla de Ayacucho
c) Día de la Inmaculada Concepción
d) Combate de Angamos\n"""+RESET)

  respuesta_3 = input('Introduce tu respuesta: ')

  while respuesta_3 not in('a','b','c','d'):
    print('Ingresa las alternativas que se presenta. Vuelve a intentarlo')
    respuesta_3 = input('Introduce tu respuesta: ')
  if respuesta_3 == 'a':
    print(ROJO+'Incorrecto',nombre,'el Día de Todos los Santos es el 01 de noviembre'+RESET)
    puntaje -= random.randint(3,7)
  elif respuesta_3 == 'b':
    print(ROJO+'Incorrecto',nombre,'La Batalla de Ayacucho se conmemora el 09 de diciembre'+RESET)
    puntaje -= random.randint(3,7)
  elif respuesta_3 == 'c':
    print(ROJO+'Incorrecto',nombre,'el Día de la Inmaculado Concepción es el 08 de diciembre'+RESET)
    puntaje -= random.randint(3,7)
  else:
    print(CYAN+'Felicidades',nombre, 'acertaste'+RESET)
    puntaje += random.randint(3,7)

  print(VERDE+'\nPor el momento llevas',puntaje,'puntos'+RESET)
  time.sleep(2)

  print(AMARILLO+"""\n4- ¿Cuándo es el día de la Independencia del Perú?
a) 28 de noviembre
b) 28 de julio
c) 05 de julio 
d) 15 de septiembre\n"""+RESET)

  respuesta_4 = input('Introduce tu respuesta: ')
  while respuesta_4 not in('a','b','c','d'):
    print('Ingresa las alternativas que se presenta. Vuelve a intentarlo')
    respuesta_4 = input('Introduce tu respuesta: ')
  if respuesta_4 == 'a':
    print(ROJO+'Incorrecto',nombre,'ese día se celebra la independencia de Panamá'+RESET)
    puntaje -= random.randint(5,10)
  elif respuesta_4 == 'c':
    print(ROJO+'Incorrecto',nombre,'ese día se celebra la independencia de Venezuela'+RESET)
    puntaje -= random.randint(5,10)
  elif respuesta_4 == 'd':
    print(ROJO+'Incorrecto',nombre,'ese día se celebra la independencia de Guatemala'+RESET)
    puntaje -= random.randint(5,10)
  else:
    print(CYAN+'Felicidades',nombre, 'acertaste'+RESET)
    puntaje += random.randint(5,10)
  
  time.sleep(2)
  print(VERDE+'\nGracias',nombre,'por jugar la trivia que realicé, alcanzaste',puntaje,'puntos\n'+RESET)

  print('¿Quieres repetir la trivia?\n')
  respuesta_5=input('Ingresa si o no: ').lower()
  if respuesta_5 == 'si':
    time.sleep(2)
    iniciar_trivia = True
    
  else:
    print('\nGracias por participar de mi trivia')
    iniciar_trivia = False
    
    