class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    # Méthode privée pour calculer le total d'une commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # Méthodes publiques
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"{nom_plat} a été ajouté à la commande.")
        else:
            print(f"{nom_plat} est déjà dans la commande.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande}")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat}: {details['prix']} € - Statut: {details['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer: {total} € (TVA incluse)")
        print(f"Statut de la commande: {self.__statut_commande}")

    def calculer_tva(self, taux_tva=0.2):
        total = self.__calculer_total()
        tva = total * taux_tva
        return tva


# Exemple d'utilisation
commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 8.0)
commande1.afficher_commande()

tva_calculée = commande1.calculer_tva()
print(f"TVA à payer: {tva_calculée} €")

commande1.annuler_commande()
commande1.afficher_commande()
