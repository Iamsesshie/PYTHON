class Cours:
    
    def __init__(self, titre, description, duree):
        
        self.titre = titre
        
        self.description = description
        
        self.duree = duree
        

class GestionnaireCours:
    
    def __init__(self):
        
        self.cours = []

    def ajouter_cours(self, cours):
        
        self.cours.append(cours)

    def afficher_cours(self):
        
        if not self.cours:
            
            print("Aucun cours enregistré.")
            
        else:
            
            for index, cours in enumerate(self.cours):
                
                print(f"\nCours {index+1}:")
                
                print("Titre :", cours.titre)
                
                print("Description :", cours.description)
                
                print("Durée :", cours.duree)
                

def menu():
    
    gestionnaire = GestionnaireCours()

    while True:
        
        print("\n===== Menu =====")
        
        print("1. Ajouter un cours")
        
        print("2. Afficher les cours")
        
        print("3. Quitter")

        choix = input("Entrez votre choix (1-3) : ")

        if choix == "1":
            
            titre = input("Entrez le titre du cours : ")
            
            description = input("Entrez la description du cours : ")
            
            duree = input("Entrez la durée du cours : ")

            cours = Cours(titre, description, duree)
            
            gestionnaire.ajouter_cours(cours)
            
            print("Le cours a été ajouté avec succès.")

        elif choix == "2":
            
            gestionnaire.afficher_cours()

        elif choix == "3":
            
            print("Merci d'avoir utilisé l'interface de gestion de cours.")
            
            break

        else:
            
            print("Choix invalide. Veuillez réessayer.")

menu()