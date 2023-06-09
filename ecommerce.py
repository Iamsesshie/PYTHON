class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Panier:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def afficher_panier(self):
        if not self.produits:
            print("Le panier est vide.")
        else:
            total = 0
            print("Contenu du panier :")
            for produit in self.produits:
                print("- Produit :", produit.nom)
                print("  Prix :", produit.prix)
                total += produit.prix
            print("Total :", total)

def main():
    panier = Panier()

    while True:
        print("\n===== Maquette d'e-commerce =====")
        print("1. Ajouter un produit au panier")
        print("2. Afficher le contenu du panier")
        print("3. Quitter")

        choix = input("Entrez votre choix (1-3) : ")

        if choix == "1":
            nom = input("Entrez le nom du produit : ")
            prix = float(input("Entrez le prix du produit : "))

            produit = Produit(nom, prix)
            panier.ajouter_produit(produit)
            print("Le produit a été ajouté au panier.")

        elif choix == "2":
            panier.afficher_panier()

        elif choix == "3":
            print("Merci d'avoir utilisé la maquette d'e-commerce.")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

main()