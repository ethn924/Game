from db_init import *


# Fonction de lancement de la partie : start_game()
#     Appeler get_all_heroes() de db_init.py pour récupérer la liste
#     Gestion des équipes : Saisie du nom du joueur avant la création d'une équipe
#     while True:
#         Demander avec un input le pseudo du joueur et le stocker dans la variable player_name
#         Appeler la fonction is_valid_name(player_name) pour faire les différentes vérifs
#         Si is_valid_name renvoie True alors :
#             break pour sortir de la boucle et return le nom du joueur
#         Sinon :
#             Lancer display_error("invalid_name")
#     Passer à la création de l'équipe en appelant la fonction create_team(heroes_list)
#     Retourner cette équipe et le nom du joueur pour lancer les combats

# Sélection des personnages pour constituer une équipe : fonction create_team(heroes_list)
#     Initialiser un dictionnaire vide player_team pour stocker l'équipe finale du joueur (3 héros max)
#     Initialiser un ensemble set vide pour assurer que chaque personnage ne peut être sélectionné qu'une seule fois
#     Boucler 3 fois tant que l'équipe n'est pas pleine :
#         Afficher l'état de l'interface de création d'équipe
#         Appeler display_current_team(player_team) pour montrer l'avancement actuel
#         Appeler display_heroes_list(heroes_list) pour l'interface proposant la liste des personnages disponibles
#         Appeler player_choice en lui passant le nombre maximum de héros de la liste et display_heroes_list
#         Récupérer le héros sélectionné dans heroes_list grâce au choix renvoyé
#         Vérifier si le nom du héros est déjà présent dans le set des héros sélectionnés :
#             Si présent alors lancer display_error("hero_already_chosen"), puis continue pour forcer un nouveau choix
#         Si absent alors :
#             Ajouter le nom du héros dans le set de suivi d'unicité
#             Ajouter le héros complet (Nom, Type, Attaque, Défense, PV) dans le dictionnaire player_team
#     Afficher l'équipe finale au joueur
#     Retourner le dictionnaire player_team

# Fonction de traitement et d'affichage du tableau des scores : show_scoreboard()
#     Appeler get_all_scores() de db_init.py pour obtenir la liste brute
#     Filtrer les 3 meilleurs :
#         Trier le tableau sur element.waves
#         Prendre les 3 derniers éléments du tableau avec mon_array[-3:]
#     Afficher proprement le podium des 3 meilleurs

# Phase 2 : COMBAT
# Sélectionner un mot aléatoire, fonction qui va être appelée à chaque nouvelle wave : SelectRandomMonster()
# Fonction SelectRandomMonster():
#     Appeler get_all_monsters() de db_init.py pour récupérer la liste des monstres
#     Sélectionner un monstre au hasard dans la liste
#     Retourner le dictionnaire du monstre choisi avec ses caractéristiques propres

def start_game():
    get_all_heroes()
    player_name = input("Entrez votre pseudo : ")