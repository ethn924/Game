# Définition des variables de connexion
# db_url = "mongodb://localhost:27017/"  Ma connection string
# db_name = "Game"  Nom de ma BDD

# Fonction pour me connecter à la BDD : database_connection()
#     Se connecter au client MongoClient avec db_url
#     Accéder à la BDD avec db_name
#     Afficher Connexion OK !
#     Retourner le client et la BDD game

# Fonction show_scoreboard():
#     Se connecter à la BDD avec database_connection()
#     Accéder à la collection scores
#     Récupérer tous les documents avec find
#     Filtrer les 3 meilleurs :
#         Trier le tableau sur element.waves
#         Prendre les 3 derniers éléments du tableau avec mon_array[-3:]
#     Afficher les 3 meilleurs
