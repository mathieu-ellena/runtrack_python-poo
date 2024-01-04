class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nombre_pages(nombre_pages)

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        if not isinstance(nouveau_nombre_pages, int):
            raise ValueError("Erreur : Le nombre de pages doit être un nombre entier.")
        elif nouveau_nombre_pages <= 0:
            raise ValueError("Erreur : Le nombre de pages doit être un nombre entier strictement positif.")
        self.__nombre_pages = nouveau_nombre_pages

    def afficher_informations(self):
        print(f"Titre : {self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nombre_pages}")

# Exemple d'utilisation de la classe Livre
mon_livre = Livre("Harry Potter", "J.K. Rowling", 500)
mon_livre.afficher_informations()

try:
    # Tentative de modification du nombre de pages avec une valeur invalide
    mon_livre.set_nombre_pages(-100)
except ValueError as e:
    print(e)

try:
    # Modification du nombre de pages avec une valeur valide
    mon_livre.set_nombre_pages(700)
except ValueError as e:
    print(e)

mon_livre.afficher_informations()
