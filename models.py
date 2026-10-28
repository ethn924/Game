# Affichage du menu principal : display_menu()
MENU = ["Démarrer le jeu", "Afficher le tableau des scores", "Quitter le jeu"]


def display_menu():
    for i in range(len(MENU)):
        print(f"{i + 1} : {MENU[i]}")


# Affichage des héros disponibles : display_heroes_list(heroes_list)
def display_heroes_list(heroes_list):
    print("Héros disponibles :")
    for i in range(len(heroes_list)):
        print(
            f"{i + 1}. {heroes_list[i]['nom']} ({heroes_list[i]['type']}) | "
            f"{heroes_list[i]['attaque']} ATK | {heroes_list[i]['defense']} DEF | {heroes_list[i]['pv']} PV"
        )


# Affichage de la composition actuelle de l'équipe du joueur : display_current_team(player_team)
def display_current_team(player_team):
    if player_team == {}:
        print("ÉQUIPE ACTUELLE VIDE")
    else:
        print("-" * 23)
        print("Voici votre composition actuelle :")
        print("-" * 23)
        for i, (nom, stats) in enumerate(player_team.items()):
            print(
                f"{i + 1}. {nom} - {stats['attaque']} ATK - {stats['defense']} DEF - {stats['pv']} PV"
            )


# Affichage de l'état du combat : display_combat_state(monster, player_team)
def display_combat_state(monster, player_team):
    print("=== ÉTAT DU COMBAT ===")
    if "BOSS" in monster["nom"]:
        print("!!! ATTENTION BOSS !!!")
    print(f"{monster['nom']} - {monster['pv']} PV")
    print("=" * 23)
    print("Votre équipe :")

    for i, (nom, stats) in enumerate(player_team.items()):
        if stats["pv"] <= 0:
            print(f"{i + 1}. {nom} - K.O.")
        else:
            print(f"{i + 1}. {nom} - {stats['pv']} PV restants")


# Affichage du marché : display_market(items, gold)
#     J'affiche "=== MARCHÉ NOIR ==="
#     J'affiche "Votre or actuel : ", gold
#     Je boucle sur la liste items avec un index (commençant à 1) :
#         J'affiche le numéro de l'item, son nom, son prix et sa description
#     J'affiche "3. Quitter le marché"
def display_market(items, gold):
    pass