import fichas


ronda = 1
soles = 0

print('-'*87+'PLANTS VS ZOMBIES'+'-'*87)

contZombie = 0
for i in fichas.tablero:
        i[-1] = fichas.nombresZombies[contZombie]
        contZombie+=1


for i in fichas.tablero:
    print(i)

