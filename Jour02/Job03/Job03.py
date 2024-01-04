class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nombre_credits = 0
        self.__level = None  # Initialisé à None lors de la création

    def add_credits(self, nouveaux_credits):
        if nouveaux_credits > 0:
            self.__nombre_credits += nouveaux_credits
            # Mise à jour du niveau après l'ajout de crédits
            self.__level = self.studentEval()
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")

    def studentEval(self):
        if self.__nombre_credits >= 90:
            return "Excellent"
        elif self.__nombre_credits >= 80:
            return "Très bien"
        elif self.__nombre_credits >= 70:
            return "Bien"
        elif self.__nombre_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        # Appeler studentEval ici pour évaluer le niveau lors de l'affichage
        if self.__level is None:
            self.__level = self.studentEval()
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Numéro étudiant: {self.__numero_etudiant}, Niveau: {self.__level}")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

# Affichage des informations de l'étudiant
john_doe.studentInfo()
