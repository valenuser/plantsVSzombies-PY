import fichas
import random

ronda = 1
soles = 0

print('-'*87+'PLANTS VS ZOMBIES'+'-'*87)

contZombie = random.randint(0,3)

print(contZombie)
for i in fichas.tablero:
        i[-1] = fichas.nombresZombies[contZombie]
        contZombie = random.randint(0,3)



for i in fichas.tablero:
    print(i)

