import clases


space = ''
tablero = [[space for i in range(5)] for j in range(5)]

for i in tablero:
    print(i)


nombresPlantas = [clases.plantas['Lanzaguisantes'].nombre,clases.plantas['Explotonuez'].nombre,clases.plantas['Girasol'].nombre,clases.plantas['Guisantralladora'].nombre,clases.plantas['Birasol'].nombre]

nombresZombies = [clases.zombies['zombieNormal'].nombre,clases.zombies['zombieEscudo'].nombre,clases.zombies['zombieRockero'].nombre,clases.zombies['zombieRugbier'].nombre,clases.zombies['zombieDeportista'].nombre]

print(nombresPlantas)
print(nombresZombies)


clases.plantas['Lanzaguisantes'].golpear(clases.zombies['zombieNormal'])
clases.plantas['Lanzaguisantes'].golpear(clases.zombies['zombieNormal'])