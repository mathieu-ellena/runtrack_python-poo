class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        print(f"L'âge de l'animal est maintenant {self.age}")

    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom
        print(f"L'animal se nomme {self.prenom}")


# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'âge initial
print(f"L'âge de l'animal est {mon_animal.age}")

# Faire vieillir l'animal et afficher le nouvel âge
mon_animal.vieillir()

# Nommer l'animal et afficher le nom
mon_animal.nommer("Luna")
