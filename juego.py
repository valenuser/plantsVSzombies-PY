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


print('-'*83+'PLANTS VS ZOMBIES'+'-'*86)

contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[-1] = fichas.nombresZombies[contPersonajes]
        contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[0] = fichas.nombresPlantas[contPersonajes]
        contPersonajes = random.randint(0,4)





while True:
        print('\n','\t'*11,'RONDA',ronda,'\n')
        for i in fichas.tablero:
                print(i)

        print('\n'*2)
        contador = 0
        for i in range(len(fichas.tablero)):
                nombrePlanta = fichas.tablero[i][0]
                nombreZombie = fichas.tablero[i][-1]
                fichas.clases.plantas[nombrePlanta].golpearZombie(fichas.clases.zombies[nombreZombie])

        break