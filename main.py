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

# Méthode pour récupérer des documents d'une base :
# ouvrir base
# accéder à la collection souhaitée
# find
# convertir curseur en list

# Affichage du menu : fonction display_menu()
# display_menu():
    # config globale : tableau contenant des string : MENU =
    # ["Lancer Jeu",
    # "Afficher les scores",
    # "Quitter le jeu"
    # ]
    # Boucle sur tout élément de MENU
    # Afficher numéro élément et texte élément
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
        # Récupère les héros dans la BDD et les mets dans la liste heroes_list
        # Retourne cette liste
        # Appel de la fonction display_heroes
            # Création de la fonction display_heroes(heroes_list):
                # Reçoit la liste retournée par start_game() et s'occupe de bien l'afficher

# Si afficher les scores (2) :
    # Appel de la fonction show_scoreboard()
        # récupérer scores dans la base
        # accéder à la collection score
        # find
        # filtrer les 3 meilleurs
            # trie le tableau sur element.waves
            # prendre les 3 derniers éléments : mon_array [-3, -1]
        # Afficher les 3 meilleurs

# Si quitter le jeu (3) :
    # Raise SystemExit()

# Fonction pour créer l'équipe du joueur : create_team(), équipe de 3 max

# Si Afficher classement alors appel fonction show_scoreboard()
# Si quitter jeu alors appel fonction close_game()

# Config globale :
MENU = [
    "Démarrer le jeu",
    "Afficher le tableau des scores",
    "Quitter le jeu"
]
def display_menu():
    for i in range(len(MENU)):
        print(i + 1, MENU[i])



# Conversion du choix en int
def convert_to_int(player_choice):
    player_choice = int(player_choice)
    return player_choice


# Récupérer le choix du joueur et gérer ses bêtises
def player_choice():
    player_choice = input("Entrez ici : ")
    while not (player_choice.isdigit()):
        print("Veuillez entrer un nombre (1 - 2 - 3)")
        display_menu()
        player_choice = input("Entrez ici : ")

    player_choice_int = convert_to_int(player_choice)

    while not (1 <= player_choice_int <= 3):
        print("Veuillez entrer un nombre (1 - 2 - 3)")
        display_menu()
        player_choice = input("Entrez ici : ")
        while not (player_choice.isdigit()):
            print("Veuillez entrer un nombre (1 - 2 - 3)")
            display_menu()
            player_choice = input("Entrez ici : ")
        player_choice_int = convert_to_int(player_choice)

    return player_choice_int

# Récupère les héros de la BDD et les affiche sous forme de liste
def start_game():
    print("Chargement...")
    heroes_list = []
    # Je me connecte à la BDD pour faire ma requête
    client, game = database_connection()

    # Je cible la collection heroes
    heroes_collection = game["heroes"]

    # Joli affichage pour que le joueur puisse choisir tranquillement
    # Si 0 (false) pas d'affichage, si 1 (true) affichage
    manage_heroes_display = {"_id":0, "nom":1, "type":1, "attaque":1, "defense":1, "pv": 1}

    # On convertit nos données en liste
    heroes_list = list(heroes_collection.find({}, manage_heroes_display))
    display_heroes_list(heroes_list)
    return heroes_list

def display_heroes_list(heroes_list):
    print("Choisissez 3 héros !")
    
    # Afficher les éléments du dictionnaire 1 à 1
    for cle, valeur in heroes_list.items():
        # Clés = nom, type, attaque, defense, pv
        # Valeurs = 
        print(f"[{cle}] {valeur}")


# Main Programme

display_menu()


player_choice_int = player_choice()

if player_choice_int == 1:
    start_game()

if player_choice_int == 3:
    raise SystemExit()
