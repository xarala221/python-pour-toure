class Personne:

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def manger(self):
        print(f"{self.nom}{self.prenom} mange")

    def boire(self):
        print(f"{self.nom}{self.prenom} bois")

    def sortire(self):
        print(f"{self.nom}{self.prenom} sorte")


class Etudiant(Personne):
    def __init__(self, nom, prenom, age):
        super().__init__(nom, prenom, age)


modou = Personne("Diop ", "Modou", 25)
modou.manger()
modou.boire()
modou.sortire()

makhtar = Etudiant("Mbacke ", "Makhtar", 24)
makhtar.boire()
