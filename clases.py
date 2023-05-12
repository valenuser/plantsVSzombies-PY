import random


class Personaje:
    nombre = ''
    vida = 0
    daño = 0



class Plantas(Personaje):
        def __init__(self,nombre,vida,daño):
            Personaje.__init__(self)
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
            self.daño+=5
            print('Daño de',self.nombre,'mejorado:',self.daño)



class Zombies(Personaje):
    def __init__(self,nombre,vida,daño):
        Personaje.__init__(self)
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
    
    def golpearPlanta(self,enemigo):
        ataque = self.daño + 2*random.randrange(-10,11)
        enemigo.vida - ataque




#plantas
LanLanzaguisantes = Plantas('Lanzaguisantes',150,15)
Explotonuez = Plantas('Explotonuez',1,100)
Girasol = Plantas('Girasol',100,0)
Repetidora = Plantas('Repetidora',150,30)
Guisantralladora = Plantas('Guisantralladora',100,40)
Birasol = Plantas('Birasol',150,0)
Tripitadora = Plantas('Tripitadora',150,50)

#zombies

zombieNormal = Zombies('zombieNormal',100,15)
zombieEscudo = Zombies('zombieEscudo',150,15)
zombieRockero = Zombies('zombieRockero',100,25)
zombieRugbier = Zombies('zombieRugbier',100,40)
zombieDeportista = Zombies('zombieDeportista',100,20)

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


