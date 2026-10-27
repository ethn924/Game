from pymongo import MongoClient

# Tout d'abord je dois me connecter à ma BDD
# Définition des variables de connexion

db_url = "mongodb://localhost:27017/"  # Ma connection string
db_name = "Game"  # Nom de ma BDD


# Fonction pour me connecter à la BDD
def database_connection():
    client = MongoClient(db_url)
    game = client[db_name]
    print("Connexion OK !")
    return client, game


database_connection()  # Pour s'assurer qu'on sache directement qu'on est bien connectés

# Première étape : lancement de la partie

# Affichage du menu : fonction display_menu()
# MESSAGE DE BIENVENU
# MONTRER LES CHOIX

# Menu affiché, ensuite, sélection du joueur : fonction player_choice()
# Demande au joueur ce qu'il souhaite faire
# Gérer les soucis avec vérifs (chiffre 1 ou 2 ou 3, conversion en int, conversion avec fonction convert_to_int)
# Selon choix du joueur :
# Si démarrer jeu alors appel fonction start_game()
# Création du menu pour les héros choisis (équipe de 3), récup BDD
# Fonction pour créer l'équipe du joueur : create_team()

# Si Afficher classement alors appel fonction show_scoreboard()
# Si quitter jeu alors appel fonction close_game()


def display_menu():
    print("-" * 23)
    print("WELCOME !")
    print("-" * 23)
    print("Choisissez une option (entre 1 et 3):")
    print("(1) : DÉMARRER LE JEU")
    print("(2) : AFFICHER LE CLASSEMENT")
    print("(3) : QUITTER LE JEU")


def player_choice():
    player_choice = input("Entrez ici : ")
    if not (player_choice.isdigit()):
        print("Veuillez entrer un nombre (1 - 2 - 3)")
        display_menu()
        print(player_choice)
        


def convert_to_int(player_choice):
    player_choice = int(player_choice)
    return player_choice


display_menu()
player_choice()
