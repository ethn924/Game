from db_init import *
from utils import *
from models import *

# Fonction de lancement de la partie : start_game()
#     Appeler get_all_heroes() (provenant de db_init.py) pour récupérer la liste des héros
#     Gestion des équipes : Saisie du nom du joueur avant la création d'une équipe
#     while True:
#         Demander avec un input le pseudo du joueur et le stocker dans la variable player_name
#         Appeler la fonction is_valid_name(player_name) (provenant de utils.py) 
#             pour faire les différentes vérifs et stocker le résultat (True ou False) dans une variable
#         Si la variable de vérification est True :
#             break pour sortir de la boucle du pseudo (ne pas faire de return ici, 
#                 sinon l'équipe ne sera jamais créée)
#         Sinon :
#             Lancer display_error("invalid_name") (provenant de utils.py)
#     Passer à la création de l'équipe en appelant la fonction create_team(heroes_list) 
#         et stocker le résultat dans une variable player_team
#     Lancer la boucle de combat (combat_loop) en lui passant player_name et player_team
#     (Le combat_loop gérera la fin de partie et l'enregistrement du score)
def start_game():
    heroes_list = get_all_heroes()

    while True:
        player_name = input("Entrez votre pseudo : ")

        valide_name = is_valid_name(player_name)

        if valide_name == True:
            break
        else:
            display_error("invalid_name")

    player_team = create_team(heroes_list)

    return player_name, player_team


# Sélection des personnages pour constituer une équipe : fonction create_team(heroes_list)
#     La fonction reçoit la liste des héros disponibles
#     Initialiser un dictionnaire vide player_team pour stocker l'équipe finale du joueur (3 héros max)
#     Boucler tant que l'équipe n'est pas pleine (while len(player_team) < 3) :
#         Afficher un titre ou un séparateur visuel pour indiquer l'étape de création
#         Appeler display_current_team(player_team) (provenant de models.py) 
#             pour montrer l'avancement actuel
#         Appeler display_heroes_list(heroes_list) (provenant de models.py) 
#             pour l'interface proposant la liste des personnages disponibles
#         Appeler player_choice (provenant de utils.py) en lui passant 
#             le nombre maximum de héros de la liste (len(heroes_list)) 
#             et la fonction display_heroes_list pour gérer les erreurs. 
#             Stocker le résultat dans une variable choice.
#         Récupérer le héros sélectionné dans heroes_list grâce au choix renvoyé. 
#             Attention à l'index : si le joueur tape 1, il faut récupérer heroes_list[0], 
#             donc utiliser choice - 1. Stocker ce héros dans une variable selected_hero.
#         Ajouter le héros complet dans le dictionnaire player_team 
#             en utilisant son nom comme clé et le dictionnaire de ses stats comme valeur
#         Retirer (supprimer) ce héros de la liste heroes_list avec .pop(index) 
#             pour qu'il ne puisse plus être proposé et sélectionné au prochain tour
#     Afficher l'équipe finale au joueur (en utilisant display_current_team)
#     Retourner le dictionnaire player_team
def create_team(heroes_list):
    player_team = {}

    while len(player_team) < 3:
        print("-" * 23)
        print("CRÉATION DE L'ÉQUIPE")
        print("-" * 23)

        display_current_team(player_team)
        print("-" * 23)
        print("Héros : ")
        display_heroes_list(heroes_list)
        
        choice = player_choice(len(heroes_list), display_heroes_list)
        
        selected_hero = heroes_list[choice - 1] 
        
        # Ajout dans le dictionnaire
        player_team[selected_hero["nom"]] = selected_hero
        
        # Plus simple d'enlever le héros de la liste
        heroes_list.pop(choice - 1)
        
    display_current_team(player_team)
    return player_team


# Fonction de traitement et d'affichage du tableau des scores : show_scoreboard()
#     Appeler get_all_scores() (provenant de db_init.py) pour obtenir la liste brute des scores
#     Filtrer les 3 meilleurs :
#         Trier la liste de scores en fonction du nombre de vagues atteintes (la clé waves)
#         Prendre les 3 derniers éléments de la liste triée (les 3 plus hauts scores)
#     Afficher proprement le podium des 3 meilleurs avec leur nom et leur score
def show_scoreboard():
    get_all_scores()


# Phase 2 : COMBAT
# Sélectionner un monstre aléatoire, fonction qui va être appelée à chaque nouvelle wave : SelectRandomMonster()
# Fonction SelectRandomMonster():
#     Appeler get_all_monsters() (provenant de db_init.py) pour récupérer la liste des monstres
#     Sélectionner un monstre au hasard dans la liste (en important le module random)
#     Retourner le dictionnaire du monstre choisi avec ses caractéristiques propres


# Boucle de combat principale : combat_loop(player_name, player_team)
#     Initialiser le compteur de vagues (waves) à 0
#     while True: (combat infini)
#         Incrémenter le compteur de vagues
#         Appeler SelectRandomMonster() pour récupérer le monstre de la vague
#         Afficher le monstre et ses stats
#         while True: (tour par tour tant que le monstre ou l'équipe est en vie)
#             Les héros attaquent :
#                 Pour chaque héros de l'équipe (s'il a des PV > 0) :
#                     Calculer les dégâts avec calculate_damage(attaque_hero, defense_monstre) (provenant de utils.py)
#                     Soustraire les dégâts aux PV du monstre
#                     Afficher les dégâts infligés
#                     Si les PV du monstre <= 0 : Victoire, break la boucle de combat
#             Si le monstre est mort : break pour passer à la vague suivante
#             Le monstre attaque :
#                 Choisir un héros au hasard parmi ceux en vie (PV > 0)
#                 Calculer les dégâts avec calculate_damage(attaque_monstre, defense_hero)
#                 Soustraire les dégâts aux PV du héros
#                 Afficher les dégâts infligés
#                 Si tous les héros sont morts (PV <= 0) : Défaite, break les deux boucles (while)
#         Si défaite :
#             Afficher le score final (nombre de vagues)
#             Appeler save_score(player_name, waves - 1) (provenant de db_init.py)
#             Appeler show_scoreboard() pour afficher le classement
#             break pour quitter la boucle de combat et retourner au menu principal