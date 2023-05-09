import random


class Personaje:
    nombre = ''
    vida = 0
    daño = 0

    def __init__(self,nombre,vida,daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def golpearZombie(self,enemigo):
        ataque = self.daño + random.randrange(-10,11)
        enemigo.vida = enemigo.vida - ataque
        print(enemigo.nombre)
        print('ATACA',self.nombre)
        print('Vida del enemigo:',enemigo.vida)

    def explotarZombie(self,enemigo):
        enemigo.vida = 0
        print('ATACA',self.nombre)
        print('Vida del enemigo:',enemigo.vida)

    def mejoraDaño(self):
        self.daño+=15
        print('Daño de',self.nombre,':',self.daño)

    
    def golpearPlanta(self,enemigo):
        ataque = self.daño + 2*random.randrange(-10,11)
        enemigo.vida - ataque




#plantas
LanLanzaguisantes = Personaje('Lanzaguisantes',150,15)
Explotonuez = Personaje('Explotonuez',1,100)
Girasol = Personaje('Girasol',100,0)
Repetidora = Personaje('Repetidora',150,30)
Guisantralladora = Personaje('Guisantralladora',100,40)
Birasol = Personaje('Birasol',150,0)
Tripitadora = Personaje('Tripitadora',150,50)

#zombies

zombieNormal = Personaje('zombieNormal',100,15)
zombieEscudo = Personaje('zombieEscudo',150,15)
zombieRockero = Personaje('zombieRockero',100,25)
zombieRugbier = Personaje('zombieRugbier',100,40)
zombieDeportista = Personaje('zombieDeportista',100,20)

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


