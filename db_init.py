# Définition des variables de connexion
# db_url = "mongodb://localhost:27017/"  Ma connection string
# db_name = "Game"  Nom de ma BDD

# Fonction pour me connecter à la BDD : database_connection()
#     Se connecter au client MongoClient avec db_url
#     Accéder à la BDD avec db_name
#     Afficher Connexion OK !
#     Retourner le client et la BDD game

# Fonction pour récupérer les scores bruts : get_all_scores()
#     Se connecter à la BDD
#     Accéder à la collection scores
#     Récupérer tous les documents avec find() et les retourner

# Fonction pour récupérer les héros bruts : get_all_heroes()
#     Se connecter à la BDD
#     Cible la collection heroes
#     Effectuer un find en appliquant un filtre pour enlever le _id
#     Convertir le curseur MongoDB en liste heroes_list et la retourner


from pymongo import MongoClient

db_url = "mongodb://localhost:27017/"  # Ma connection string
db_name = "Game"  # Nom de ma BDD


def database_connection():
    client = MongoClient(db_url)
    game = client[db_name]
    # Vérification de la connexion
    print("Connexion réussie, bienvenue !")
    return client, game

def get_all_scores():
    client, game = database_connection() # Connexion BDD
    scores_collection = game["scores"] # Accès à collection scores
    scores_list = list(scores_collection.find()) # Récupération des scores

    return scores_list

def get_all_heroes():
    client, game = database_connection() # Connexion BDD
    heroes_collection = game["heroes"] # Accès à collection heroes
    heroes_list = list(heroes_collection.find()) # Récupération des héros

    return heroes_list
