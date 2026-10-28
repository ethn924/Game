import random
import time

from db_init import *
from models import *
from utils import *


# Fonction de validation du pseudo : get_valid_username()
def get_valid_username():
    while True:
        player_name = input("Entrez votre pseudo : ")
        if is_valid_name(player_name):
            return player_name
        display_error("invalid_name")


# Fonction de lancement de la partie : start_game()
def start_game():
    gold = 0
    heroes_list = get_all_heroes()
    player_name = get_valid_username()
    player_team = create_team(heroes_list)
    combat_loop(player_name, player_team, gold)


# Sélection des personnages pour constituer une équipe : create_team(heroes_list)
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

        valid_options = list(range(1, len(heroes_list) + 1))
        choice = player_choice(valid_options, display_heroes_list)

        selected_hero = heroes_list[choice - 1]
        player_team[selected_hero["nom"]] = selected_hero
        heroes_list.pop(choice - 1)
    display_current_team(player_team)
    return player_team


# Fonction de traitement et d'affichage du tableau des scores : show_scoreboard()
def show_scoreboard():
    scoreboard = get_all_scores()
    if len(scoreboard) == 0:
        print("Tableau des scores vide pour l'instant")
        return
    sorted_scoreboard = sorted(scoreboard, key=lambda x: x["waves"], reverse=True)
    best_players = sorted_scoreboard[:3]
    print("Voici les meilleurs joueurs : ")
    for i in range(len(best_players)):
        print(f"{i + 1}. {best_players[i]['player_name']} - {best_players[i]['waves']} vagues")


# Sélectionner un monstre aléatoire : select_random_monster()
def select_random_monster():
    monsters = get_all_monsters()
    random_monster = random.choice(monsters)
    return random_monster


# Phase d'attaque des héros : heroes_attack(player_team, monster)
def heroes_attack(player_team, monster):
    for name, hero_stats in player_team.items():
        if hero_stats["pv"] > 0:
            hero_damage = calculate_damage(hero_stats["attaque"], monster["defense"])
            monster["pv"] = monster["pv"] - hero_damage
            print(f"Dégâts infligés par {name} : {hero_damage}")
            if monster["pv"] <= 0:
                return True
    return False


# Phase d'attaque du monstre : monster_attack(monster, player_team)
def monster_attack(monster, player_team):
    alive_heroes = []
    for name, hero_stats in player_team.items():
        if hero_stats["pv"] > 0:
            alive_heroes.append((name, hero_stats))

    if alive_heroes:
        target_name, target_hero = random.choice(alive_heroes)
        monster_damage = calculate_damage(monster["attaque"], target_hero["defense"])
        target_hero["pv"] = target_hero["pv"] - monster_damage
        print(f"Dégâts infligés par le monstre à {target_name} : {monster_damage}")


# Vérification de la défaite : is_team_dead(player_team)
def is_team_dead(player_team):
    for name, stats in player_team.items():
        if stats["pv"] > 0:
            return False
    return True


# Choix du héros pour attribuer un objet : choose_hero_for_item(player_team)
#     Afficher "À qui souhaitez-vous donner cet objet ?"
#     Appeler display_current_team(player_team)
#     Créer valid_options allant de 1 au nombre de héros dans l'équipe
#     Appeler player_choice(valid_options, lambda: display_current_team(player_team))
#     Récupérer la clé (le nom) du héros choisi dans le dictionnaire player_team
#     Retourner le dictionnaire du héros ciblé
def choose_hero_for_item(player_team):
    pass


# Boucle de combat principale : combat_loop(player_name, player_team, gold)
#     (Code actuel)
#     --- CHANTIER SCALE MONSTER ---
#     Juste après avoir récupéré le monstre avec select_random_monster() :
#         Appeler scale_monster(monster, waves)
#     --- CHANTIER MARCHE ---
#     À la place de la logique actuelle du marché (qui ne gère qu'un seul item) :
#         market_items = generate_market_items()
#         display_market(market_items, gold)
#         valid_choices = [1, 2, 3]  # 1 et 2 pour les items, 3 pour quitter
#         choice = player_choice(valid_choices, lambda: display_market(market_items, gold))
#         Si choice != 3 (le joueur achète un item) :
#             item_choisi = market_items[choice - 1]
#             Si gold >= item_choisi["prix"] :
#                 gold -= item_choisi["prix"]
#                 target_hero = choose_hero_for_item(player_team)
#                 apply_item_effect(item_choisi, target_hero)
#                 print("Achat réussi")
#             Sinon :
#                 print("Or insuffisant")
def combat_loop(player_name, player_team, gold):
    waves = 0
    while True:
        waves += 1
        monster = select_random_monster()

        # Chantier Scale : ajouter scale_monster(monster, waves) ici
        scale_monster(monster, waves)

        if waves % 5 == 0:
            boost_monster_stats(monster)

        display_combat_state(monster, player_team)
        time.sleep(2)

        combat_ongoing = True
        defeat = False

        while combat_ongoing:
            if heroes_attack(player_team, monster):
                combat_ongoing = False
                break

            time.sleep(1)
            monster_attack(monster, player_team)
            time.sleep(1)

            if is_team_dead(player_team):
                combat_ongoing = False
                defeat = True

        if defeat:
            print("TOUS VOS HÉROS SONT MORTS, LES MONSTRES ENVAHISSENT LE ROYAUME")
            print("DÉFAITE !")
            print(f"Score final : {waves - 1}")
            save_score(player_name, waves - 1)
            show_scoreboard()
            break

        if defeat == False:
            gold = gold + (waves * 5)
            heal_team(player_team)
            if waves % 5 == 0:
                # Chantier Marché 2 items : remplacer la logique actuelle par celle décrite plus haut
                item = random.choice(MARKET_ITEMS)
                display_market(item, gold)
                choice = player_choice(
                    valid_choices=[1, 2],
                    error_function=lambda: display_market(item, gold),
                )
                if choice == 1 and gold >= item["prix"]:
                    gold -= item["prix"]
                    apply_item_effect(item, player_team)
                    print("Achat réussi")
                else:
                    print("Or insuffisant ou achat annulé")