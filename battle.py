import random
import time

jugador_1 = input('Nombre jugador 1: ')
jugador_2 = input('\nNombre jugador 2: ')

lista_jugadores = [jugador_1,jugador_2]

puntos_jugador_1 = 20
puntos_jugador_2 = 20

print('\nPuntos iniciales del jugador',jugador_1,'es',puntos_jugador_1)
print('\nPuntos iniciales del jugador',jugador_2,'es',puntos_jugador_2)



iniciar_juego = True

while iniciar_juego:
    
    jugador_aleatorio = random.choice(lista_jugadores)
    
    print('\nEl juego ha elegido de manera aleatoria que comience el jugador',jugador_aleatorio)
    
    if jugador_aleatorio==jugador_1:
        puntos_jugador_1 = puntos_jugador_1 - random.randint(0,5)
        print('Los puntos que tiene el jugador',jugador_1,'hasta el momento es de',puntos_jugador_1)
        time.sleep(2)
        if puntos_jugador_1 <=0:
            print('\nGanó el juego',jugador_2,'quedando con un total de',puntos_jugador_2,'puntos')
            iniciar_juego = False
    
    else:
        puntos_jugador_2 = puntos_jugador_2 - random.randint(0,5)
        print('Los puntos que tiene el jugador',jugador_2,'hasta el momento es de',puntos_jugador_2)
        time.sleep(2)
        if puntos_jugador_2 <=0:
            print('\nGanó el juego',jugador_1,'quedando con un total de',puntos_jugador_1,'puntos')
            iniciar_juego = False
    
    