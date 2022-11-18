class personnage:
    def __init__(self):
        self.name = "Personnnage"
        self.pv = 100
        self.attaque = 20
        self.defense = 10

        self.catchphrase = "Je suis un personnage"

    def __init__(self, name, catchphrase):
        self.name = name
        self.pv = 100
        self.attaque = 20
        self.defense = 10
        self.catchphrase = catchphrase

    def attaquer(self, cible):
        print("pv de la cible"+str(cible.pv))
        if (cible.defense > self.attaque):
            print("La cible a trop de defense")
        else:
            cible.pv = cible.pv - (self.attaque - cible.defense)
            print("pv de la cible"+str(cible.pv))

    def sePresenter(self):
        print(self.catchphrase)

class guerrier(personnage):
    def __init__(self):
        personnage.__init__(self, "Guerrier", "Je suis un guerrier")

    def criDeGuerre(self):
        print(self.catchphrase)

class clerc(personnage):
    def __init__(self):
        personnage.__init__(self, "Clerc", "Je suis un clerc")

    def soigner(self, cible):
        print("pv de la cible"+str(cible.pv))
        cible.pv = cible.pv + (self.attaque)
        print("pv de la cible après soin"+str(cible.pv))

class paladin(clerc, guerrier):
   def __init__(self):
        personnage.__init__(self, "Paladin", "Je suis un paladin")

class mage(personnage):
    def __init__(self):
        self.mana = 30
        personnage.__init__(self, "Mage", "Je suis un mage")

    def jeterUnSort(self, cible):
        if(self.mana > 10):
            self.mana = self.mana - 10

        print("pv de la cible :"+str(cible.pv)+" vos pv:"+str(self.pv))
        if (cible.defense > self.attaque):
            print("La cible a trop de defense")
        else:
            cible.pv = cible.pv - (self.attaque - cible.defense)
            self.pv = self.pv + (self.attaque - cible.defense)
            print("pv de la cible :"+str(cible.pv)+" vos pv:"+str(self.pv))

class archer(personnage):
    def __init__(self):
        personnage.__init__(self, "Guerrier", "Je suis un guerrier")

    def tirer(self, cible):
        print("pv de la cible"+str(cible.pv))
        if (cible.defense > self.attaque):
            print("La cible a trop de defense")
        else:
            cible.pv = cible.pv - (self.attaque - cible.defense)
            print("pv de la cible"+str(cible.pv))


perso1 = guerrier()

perso2 = mage()

perso1.sePresenter()

perso2.sePresenter()


perso2.jeterUnSort(perso1)