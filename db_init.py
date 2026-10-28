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
    print("Connexion réussie, bienvenue !")
    return client, game


# Fonction pour récupérer les scores bruts : get_all_scores()
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection scores
#     Récupérer tous les documents avec find() et les convertir en liste
#     Retourner la liste des scores
def get_all_scores():
    client, game = database_connection()
    scores_collection = game["scores"]
    scores_list = list(scores_collection.find())
    return scores_list


# Fonction pour sauvegarder un score : save_score(player_name, waves)
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection scores
#     Mettre à jour le document du joueur s'il existe déjà (en filtrant sur player_name)
#     Si le joueur n'existe pas, l'insérer (upsert=True)
#     Mettre à jour la valeur de "waves" avec le nouveau score
def save_score(player_name, waves):
    client, game = database_connection()
    scores_collection = game["scores"]

    add_score = scores_collection.update_one(
        {"player_name": player_name},
        {"$set": {"waves": waves}},
        upsert=True,
    )

    return "Votre score a été sauvegardé !"


# Fonction pour récupérer les héros : get_all_heroes()
#     Se connecter à la BDD en appelant database_connection()
#     Cible la collection heroes
#     Effectuer un find en appliquant un filtre pour enlever le _id
#     Convertir le curseur MongoDB en liste heroes_list et la retourner
def get_all_heroes():
    client, game = database_connection()
    heroes_collection = game["heroes"]
    heroes_list = list(heroes_collection.find({}, {"_id": 0}))
    return heroes_list


# Fonction pour récupérer les monstres : get_all_monsters()
#     Se connecter à la BDD en appelant database_connection()
#     Accéder à la collection monsters
#     Récupérer tous les documents (monstres) avec find
#     Convertir le curseur MongoDB en liste de monstres et la retourner
def get_all_monsters():
    client, game = database_connection()
    monsters_collection = game["monsters"]
    monsters_list = list(monsters_collection.find())
    return monsters_list