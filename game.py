from db_init import *
from utils import *


# Fonction de lancement de la partie : start_game()
#     Appeler get_all_heroes() (provenant de db_init.py) pour récupérer la liste des héros
#     Gestion des équipes : Saisie du nom du joueur avant la création d'une équipe
#     while True:
#         Demander avec un input le pseudo du joueur et le stocker dans la variable player_name
#         Appeler la fonction is_valid_name(player_name) (provenant de utils.py) pour faire les différentes vérifs et stocker le résultat (True ou False) dans une variable
#         Si la variable de vérification est True :
#             return le nom du joueur (le return quitte la fonction et la boucle)
#         Sinon :
#             Lancer display_error("invalid_name") (provenant de utils.py)
#     Passer à la création de l'équipe en appelant la fonction create_team(heroes_list) et stocker le résultat
#     Retourner l'équipe et le nom du joueur pour lancer les combats

# Sélection des personnages pour constituer une équipe : fonction create_team(heroes_list)
#     La fonction reçoit la liste des héros disponibles
#     Initialiser un dictionnaire vide player_team pour stocker l'équipe finale du joueur (3 héros max)
#     Initialiser une variable set vide (en utilisant set() et non {}) pour assurer que chaque personnage ne peut être sélectionné qu'une seule fois
#     Boucler tant que l'équipe n'est pas pleine (3 héros) :
#         Afficher un titre ou un séparateur visuel pour indiquer l'étape de création
#         Appeler display_current_team(player_team) (provenant de models.py) pour montrer l'avancement actuel
#         Appeler display_heroes_list(heroes_list) (provenant de models.py) pour l'interface proposant la liste des personnages disponibles
#         Appeler player_choice (provenant de utils.py) en lui passant le nombre maximum de héros de la liste et la fonction display_heroes_list pour gérer les erreurs
#         Récupérer le héros sélectionné dans heroes_list grâce au choix renvoyé (attention à l'index)
#         Vérifier si le nom du héros est déjà présent dans le set des héros sélectionnés :
#             Si présent alors lancer display_error("hero_already_chosen") (provenant de utils.py), puis continue pour forcer un nouveau choix
#         Si absent alors :
#             Ajouter le nom du héros dans le set de suivi d'unicité
#             Ajouter le héros complet (sous forme de dictionnaire avec Nom, Type, Attaque, Défense, PV) dans le dictionnaire player_team
#     Afficher l'équipe finale au joueur (en utilisant display_current_team)
#     Retourner le dictionnaire player_team

# Fonction de traitement et d'affichage du tableau des scores : show_scoreboard()
#     Appeler get_all_scores() (provenant de db_init.py) pour obtenir la liste brute des scores
#     Filtrer les 3 meilleurs :
#         Trier la liste de scores en fonction du nombre de vagues atteintes (la clé waves)
#         Prendre les 3 derniers éléments de la liste triée (les 3 plus hauts scores)
#     Afficher proprement le podium des 3 meilleurs avec leur nom et leur score

# Phase 2 : COMBAT
# Sélectionner un mot aléatoire, fonction qui va être appelée à chaque nouvelle wave : SelectRandomMonster()
# Fonction SelectRandomMonster():
#     Appeler get_all_monsters() (provenant de db_init.py) pour récupérer la liste des monstres
#     Sélectionner un monstre au hasard dans la liste (en important le module random)
#     Retourner le dictionnaire du monstre choisi avec ses caractéristiques propres


def start_game():
    heroes_list = get_all_heroes()

    while True:
        player_name = input("Entrez votre pseudo : ")

        valide_name = is_valid_name(player_name)

        if valide_name == True:
            return player_name
        else:
            display_error("invalid_name")

        player_team = create_team(heroes_list)

        return player_name, player_team


def create_team(heroes_list):
    player_team = {}
    set = {}


i = 1

while i < 3:
    print("-" * 23)
    print("CRÉATION DE L'ÉQUIPE")
    print("-" * 23)

    display_current_team(player_team)