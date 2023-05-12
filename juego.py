import fichas
import random


ronda = 1


print('-'*83+'PLANTS VS ZOMBIES'+'-'*86)

contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[-1] = fichas.nombresZombies[contPersonajes]
        contPersonajes = random.randint(0,4)

for i in fichas.tablero:
        i[0] = fichas.nombresPlantas[contPersonajes]
        contPersonajes = random.randint(0,4)

end = 1


posicionZombies = -1

while True:
        print('\n','\t'*11,'RONDA',ronda,'\n')
        for i in fichas.tablero:
                print(i)

        print('\n'*2)
        contador = 0
        for i in range(len(fichas.tablero)):
                nombrePlanta = fichas.tablero[i][0]
                nombreZombie = fichas.tablero[i][-1]

                if nombrePlanta == 'Explotonuez' and nombreZombie != '':
                        fichas.clases.plantas[nombrePlanta].explotarZombie(fichas.clases.zombies[nombreZombie])
                elif nombrePlanta == 'Girasol' or nombrePlanta == 'Birasol':
                        for i in range(len(fichas.tablero)):
                                if fichas.tablero[i][0] != 'Girasol' and fichas.tablero[i][0] != 'Birasol':
                                        fichas.clases.plantas[fichas.tablero[i][0]].mejoraDaño()
                elif  nombreZombie != '':
                        fichas.clases.plantas[nombrePlanta].golpearZombie(fichas.clases.zombies[nombreZombie])


        for i in range(len(fichas.tablero)):
                nombreZombie = fichas.tablero[i][-1]
                if nombreZombie != '':
                        if fichas.clases.zombies[nombreZombie].vida < 1:
                                fichas.tablero[i][-1] = ''

        nuevaPosicionZombie = posicionZombies-1

        for i in range(len(fichas.tablero)):
                fichas.tablero[i][nuevaPosicionZombie],fichas.tablero[i][posicionZombies] = fichas.tablero[i][posicionZombies],fichas.tablero[i][nuevaPosicionZombie]

        posicionZombies-=1

        print('\n'*2,'TABLERO ACTUALIZADO:')
        for i in fichas.tablero:
                print(i)


        print('\n'*2,'VIDA DE PLANTAS:')
        for i in range(len(fichas.tablero)):
                nombrePlantas = fichas.tablero[i][0]
                print('NOMBRE DE LA PLANTA:',fichas.clases.plantas[nombrePlantas].nombre,', DAÑO:',fichas.clases.plantas[nombrePlantas].daño,', VIDA:',fichas.clases.plantas[nombrePlantas].vida)


        print('\n'*2,'VIDA DE ZOMBIES:')
        for i in range(len(fichas.tablero)):
                nombreZombies = fichas.tablero[i][posicionZombies]
                if nombreZombies != '':
                        print('NOMBRE DE LA ZOMBIE:',fichas.clases.zombies[nombreZombies].nombre,', DAÑO:',fichas.clases.zombies[nombreZombies].daño,', VIDA:',fichas.clases.zombies[nombreZombies].vida)
                else:
                        continue

        end+=1

        ronda+=1

        if end == 4:
                break