import random

class Planta:
    def __init__(self,nombre,vida,daño,coste):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.coste = coste


    def golpear(self,enemigo):
        ataque = self.daño + random.randrange(-10,11)
        enemigo.vida - ataque



class Zombie:
    def __init__(self,vida,daño,nombre):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño


    def golpear(self,enemigo):
        ataque = self.daño + 2*random.randrange(-10,11)
        enemigo.vida - ataque



#plantas
LanLanzaguisantes = Planta()
Explotonuez = Planta()
Girasol = Planta()
Repetidora = Planta()
Guisantralladora = Planta()
Birasol = Planta()
Tripitadora = Planta()

#zombies

zombieNormal = Zombie()
zombieEscudo = Zombie()
zombieRockero = Zombie()
zombieRubier = Zombie()
zombieDeportista = Zombie()

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
    'zombieRubier': zombieRubier,
    'zombieDeportista': zombieDeportista
}


