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

# Je dois maintenant afficher le menu
# On va créer la fonction, le professeur m'a appris une manière intelligente de le faire
# En temps normal j'aurai bêtement fait la sélection aussi directement dans cette fonction
# Mais cette fois j'ai compris, ELLE DOIT JUSTE AFFICHER LE MENU rien d'autre

