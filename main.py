from pymongo import MongoClient

# Tout d'abord je dois me connecter à ma BDD
# Définition des variables de connexion

db_url = "mongodb://localhost:27017/" # Ma connection string
db_name = "Game" # Nom de ma BDD

# Fonction pour me connecter à la BDD
def DatabaseConnection():
    client = MongoClient(db_url)
    game = client[db_name]
    print("Connexion OK !")
    return client, game

DatabaseConnection() # Pour s'assurer qu'on sache directement qu'on est bien connectés

# AFFICHAGE DU MENU SEULEMENT
def AfficherMenu():
    print("-----------------------")
    print("WELCOME !")
    print("-----------------------")

    print("Choisissez une option (entre 1 et 3):")
    print("(1) : DÉMARRER LE JEU")
    print("(2) : AFFICHER LE CLASSEMENT")
    print("(3) : QUITTER LE JEU")


AfficherMenu()



