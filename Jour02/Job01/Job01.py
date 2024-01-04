class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    # Méthode pour afficher les dimensions du rectangle
    def afficher_dimensions(self):
        print(f"Longueur : {self.__longueur}, Largeur : {self.__largeur}")


# Création d'un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(10, 5)

# Affichage des dimensions initiales
mon_rectangle.afficher_dimensions()

# Modification des dimensions
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

# Affichage des nouvelles dimensions
mon_rectangle.afficher_dimensions()
