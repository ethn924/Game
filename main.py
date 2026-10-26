from pymongo import MongoClient

# Tout d'abord je dois me connecter à ma BDD
# Définition des variables de connexion

db_url = "mongodb://localhost:27017/"
db_name = "Game"

# Fonction pour me connecter à la BDD
def DatabaseConnection():
    client = MongoClient(db_url)
    game = client[db_name]
    print("Connexion OK !")
    return client, game

DatabaseConnection()

