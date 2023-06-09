

class Utilisateur:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

def inscription():
    nom = input("Entrez votre nom : ")
    age = int(input("Entrez votre âge : "))
    email = input("Entrez votre adresse e-mail : ")

    utilisateur = Utilisateur(nom, age, email)

    # Vous pouvez ajouter ici la logique pour enregistrer l'utilisateur dans une base de données ou un fichier.

    print("Inscription réussie !")

inscription()