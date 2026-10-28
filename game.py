from db_init import *
from utils import *
from models import *
import random
import time


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

    combat_loop(player_name, player_team)


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
    scoreboard = get_all_scores()
    if len(scoreboard) == 0:
        print("Tableau des scores vide pour l'instant")
        return
    sorted_scoreboard = sorted(scoreboard, key=lambda x: x["waves"])
    best_players = sorted_scoreboard[-3:]
    print("Voici les meilleurs joueurs : ")
    for i in range(len(best_players)):
        print(
            i + 1,
            ".",
            best_players[i]["player_name"],
            "-",
            best_players[i]["waves"],
            "vagues",
        )


# Phase 2 : COMBAT
# Sélectionner un monstre aléatoire, fonction qui va être appelée à chaque nouvelle wave : select_random_monster()
# Fonction select_random_monster():
#     Appeler get_all_monsters() (provenant de db_init.py) pour récupérer la liste des monstres
#     Sélectionner un monstre au hasard dans la liste (en important le module random)
#     Retourner le dictionnaire du monstre choisi avec ses caractéristiques propres
def select_random_monster():
    monsters = get_all_monsters()
    random_monster = random.choice(monsters)  # choice à add sinon ça plantait
    return random_monster


# Boucle de combat principale : combat_loop(player_name, player_team)
#     Initialiser le compteur de vagues (waves) à 0
#     Initialiser la variable defeat à False
#     while True: (combat infini)
#         Incrémenter le compteur de vagues
#         Appeler select_random_monster() et stocker le résultat dans monster
#         Appeler display_combat_state(monster, player_team) pour afficher l'état
#         Initialiser combat_ongoing à True
#         while combat_ongoing: (tour par tour)
#             PHASE D'ATTAQUE DES HÉROS
#             Pour chaque héros de l'équipe :
#                 Si les PV du héros sont > 0 :
#                     Calculer les dégâts infligés au monstre
#                     Soustraire les dégâts aux PV du monstre
#                     Afficher les dégâts
#                     Si les PV du monstre sont <= 0 : combat_ongoing passe à False et break
#             Si combat_ongoing est False : break pour passer à la vague suivante
#             PHASE D'ATTAQUE DU MONSTRE
#             Créer une liste alive_heroes des héros avec PV > 0
#             Choisir un héros au hasard dans alive_heroes
#             Calculer les dégâts du monstre sur ce héros
#             Soustraire les dégâts aux PV du héros
#             Afficher les dégâts
#             VÉRIFICATION DE LA DÉFAITE
#             Compter le nombre de héros en vie
#             Si aucun héros n'est en vie : defeat passe à True et break
#         Si defeat est True :
#             Afficher le message de défaite
#             Afficher le score final (nombre de vagues)
#             Appeler save_score(player_name, waves - 1)
#             Appeler show_scoreboard()
#             break pour quitter la boucle de combat
def combat_loop(player_name, player_team):
    waves = 0
    defeat = False
    while True:
        waves += 1
        monster = select_random_monster()
        display_combat_state(monster, player_team)
        time.sleep(2) # Pause pour que ça soit agréable le combat

        combat_ongoing = True

        while combat_ongoing:
            for name, hero_stats in player_team.items():
                if hero_stats["pv"] > 0:
                    hero_damage = calculate_damage(
                        hero_stats["attaque"], monster["defense"]
                    )
                    monster["pv"] = monster["pv"] - hero_damage
                    print("Dégâts infligés par", name, ":", hero_damage)
                    if monster["pv"] <= 0:
                        combat_ongoing = False
                        break

            if not combat_ongoing:
                break

            time.sleep(1) # Pause après l'attaque des héros

            alive_heroes = []

            for name, hero_stats in player_team.items():
                if hero_stats["pv"] > 0:
                    alive_heroes.append((name, hero_stats))

            target_name, target_hero = random.choice(alive_heroes)
            monster_damage = calculate_damage(
                monster["attaque"], target_hero["defense"]
            )
            target_hero["pv"] = target_hero["pv"] - monster_damage
            print("Dégâts infligés par le monstre à", target_name, ":", monster_damage)

            time.sleep(1) # Pause après l'attaque du monstre

            heroes_alive = 0
            for name, stats in player_team.items():
                if stats["pv"] > 0:
                    heroes_alive += 1

            if heroes_alive == 0:
                defeat = True
                break

        if defeat == True:
            print("TOUS VOS HÉROS SONT MORTS, LES MONSTRES ENVAHISSENT LE ROYAUME")
            print("DÉFAITE !")
            print("Score final : ", waves - 1)
            save_score(player_name, waves - 1)
            show_scoreboard()
            break