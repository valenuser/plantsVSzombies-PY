import random

class Planta:
    def __init__(self,nombre,vida,daño,coste):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.coste = coste



    def golpear(self,enemigo):
        ataque = self.daño + random.randrange(-10,11)
        enemigo.vida = enemigo.vida - ataque
        print(enemigo.nombre)
        print('Vida del enemigo:',enemigo.vida)

    
    def explotar(self,enemigo):
        enemigo.vida = enemigo.vida - enemigo.vida



class Zombie:
    def __init__(self,nombre,vida,daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño


    def golpear(self,enemigo):
        ataque = self.daño + 2*random.randrange(-10,11)
        enemigo.vida - ataque



#plantas
LanLanzaguisantes = Planta('Lanzaguisantes',150,15,25)
Explotonuez = Planta('Explotonuez',1,100,75)
Girasol = Planta('Girasol',100,0,5)
Repetidora = Planta('Repetidora',150,30,100)
Guisantralladora = Planta('Guisantralladora',100,40,200)
Birasol = Planta('Birasol',150,0,250)
Tripitadora = Planta('Tripitadora',150,50,300)

#zombies

zombieNormal = Zombie('zombieNormal',100,15)
zombieEscudo = Zombie('zombieEscudo',150,15)
zombieRockero = Zombie('zombieRockero',100,25)
zombieRugbier = Zombie('zombieRugbier',100,40)
zombieDeportista = Zombie('zombieDeportista',100,20)

plantas = {
    'Lanzaguisantes' : LanLanzaguisantes ,
    'Explotonuez': Explotonuez,
    'Girasol': Girasol,
    'Repetidora': Repetidora,
    'Guisantralladora': Guisantralladora,
    'Birasol': Birasol
}

zombies = {
    'zombieNormal' : zombieNormal ,
    'zombieEscudo': zombieEscudo,
    'zombieRockero': zombieRockero,
    'zombieRugbier': zombieRugbier,
    'zombieDeportista': zombieDeportista
}


