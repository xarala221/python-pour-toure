# la programmation oriente objet
# proprietes -> caracteristique
# methodes -> fonctionalites


class Television:

    def __init__(self, marque):
        self.marque = marque

    def allumer(self, etat="Allume"):
        print(f"La marque {self.marque} est {etat}")

    def briller(self):
        print(f"La television {self.marque} brille")


class EcranPlat(Television):
    def __init__(self, marque):
        super().__init__(marque)


ecran_plat = EcranPlat("Samsung")
print(ecran_plat.marque)
ecran_plat.briller()
