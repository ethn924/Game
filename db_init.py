from pymongo import MongoClient

# Définition des variables de connexion
# db_url = "mongodb://localhost:27017/"  Ma connection string
# db_name = "Game"  Nom de ma BDD

db_url = "mongodb://localhost:27017/"  # Ma connection string
db_name = "Game"  # Nom de ma BDD


# Fonction pour me connecter à la BDD : database_connection()
#     Se connecter au client MongoClient avec db_url
#     Accéder à la BDD avec db_name
#     Afficher Connexion OK !
#     Retourner le client et la BDD game
def database_connection():
    client = MongoClient(db_url)
    game = client[db_name]
    # Vérification de la connexion
    print("Connexion réussie, bienvenue !")
    return client, game


# Fonction pour récupérer les scores bruts : get_all_scores()
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection scores
#     Récupérer tous les documents avec find() et les convertir en liste
#     Retourner la liste des scores
def get_all_scores():
    client, game = database_connection()  # Connexion BDD
    scores_collection = game["scores"]  # Accès à collection scores
    scores_list = list(scores_collection.find())  # Récupération des scores

    return scores_list


# Fonction pour sauvegarder un score : save_score(player_name, waves)
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection scores
#     Insérer un nouveau document contenant player_name et le nombre de waves
def save_score(player_name, waves):
    client, game = database_connection()
    scores_collection = game["scores"]

    # J'ajoute le score du joueur et attention insert_one veut un dictionnaire
    add_score = scores_collection.insert_one(
        {"player_name": player_name, "waves": waves}
    )

    return "Votre score a été sauvegardé !"


# Fonction pour récupérer les héros : get_all_heroes()
#     Se connecter à la BDD en appelant database_connection()
#     Cible la collection heroes
#     Effectuer un find en appliquant un filtre pour enlever le _id (ex: find({}, {"_id": 0}))
#     Convertir le curseur MongoDB en liste heroes_list et la retourner
def get_all_heroes():
    client, game = database_connection()  # Connexion BDD
    heroes_collection = game["heroes"]  # Accès à collection heroes
    heroes_list = list(heroes_collection.find({}, {"_id": 0})) # Récupération des héros mais je veux pas l'id

    return heroes_list


# Fonction pour récupérer les monstres : get_all_monsters()
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection monsters
#     Récupérer tous les documents (monstres) avec find
#     Convertir le curseur MongoDB en liste de monstres et la retourner
def get_all_monsters():
    client, game = database_connection()  # Connexion BDD
    monsters_collection = game["monsters"]  # Accès à la collection monsters
    monsters_list = list(monsters_collection.find())  # Récupération des monstres

    return monsters_list