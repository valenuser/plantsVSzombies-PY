import fichas
import random



# def finJuego(tablero,verificacion = False,count = 0):
#     if count == len(tablero):
#           return False
#     elif verificacion == True:
#           return True
#     else:
#           if tablero[i][0] == '' 

ronda = 1


print('-'*87+'PLANTS VS ZOMBIES'+'-'*87)

contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[-1] = fichas.nombresZombies[contPersonajes]
        contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[0] = fichas.nombresPlantas[contPersonajes]
        contPersonajes = random.randint(0,4)





while True:
    print('RONDA',ronda)
    for i in fichas.tablero:
        print(i)


    break