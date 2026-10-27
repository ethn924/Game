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

# Affichage du menu : fonction display_menu()
# MESSAGE DE BIENVENU
# MONTRER LES CHOIX

# Menu affiché, ensuite, sélection du joueur : fonction player_choice()
# fonction player_choice():
    # Demande au joueur ce qu'il souhaite faire
    # Gérer les soucis avec vérifs (chiffre 1 ou 2 ou 3, conversion en int, conversion avec fonction convert_to_int)
    # On va utiliser player_choice_int (résultat de la conversion en int de player_choice) pour faciliter

# Selon choix du joueur :
    # Si démarrer jeu (1) alors appel fonction start_game()
        # Fonction start_game():
            # Récupère les héros dans la BDD et les mets dans une liste
            # Retourne cette liste
        # Création de la fonction display_heroes(heroes_list):
            # Reçoit la liste retournée par start_game et s'occupe de bien l'afficher

# Fonction pour créer l'équipe du joueur : create_team(), équipe de 3 max

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


# Récupérer le choix du joueur et gérer ses bêtises
def player_choice():
    player_choice = input("Entrez ici : ")
    while not (player_choice.isdigit()):
        print("Veuillez entrer un nombre (1 - 2 - 3)")
        display_menu()
        player_choice = input("Entrez ici : ")

    while player_choice < 1 or player_choice > 3:
        print("Veuillez entrer un nombre (1 - 2 - 3)")
        display_menu()
        player_choice = input("Entrez ici : ")

    player_choice_int = convert_to_int(player_choice)

    return player_choice_int

def start_game():
    heroes_list = []

    return heroes_list

if (player_choice_int == 1):
        start_game()




# Conversion du choix en int
def convert_to_int(player_choice):
    player_choice = int(player_choice)
    return player_choice


display_menu()
player_choice()
