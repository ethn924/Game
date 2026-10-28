# Affichage du menu principal : fonction display_menu()
#     Déclarer une config globale : un tableau (liste) contenant des chaînes de caractères nommé MENU
#     Boucler sur chaque élément du tableau MENU en utilisant son index
#         Afficher le numéro de l'élément (index + 1) et le texte de l'élément
MENU = ["Démarrer le jeu", "Afficher le tableau des scores", "Quitter le jeu"]

def display_menu():
    for i in range(len(MENU)):
        print(i + 1, ":", MENU[i])


# Affichage des héros disponibles avec leurs caractéristiques : fonction display_heroes_list(heroes_list)
#     La fonction reçoit la liste des héros récupérée depuis la base de données via db_init.py
#     Afficher un message d'introduction pour la liste des personnages disponibles
#     Boucler sur la liste heroes_list pour extraire chaque héros (chaque héros étant un dictionnaire)
#         Extraire et afficher proprement les caractéristiques du héros : 
#             son nom, son type, son attaque, sa défense et ses pv de manière lisible
def display_heroes_list(heroes_list):
    pass


# Affichage de la composition actuelle de l'équipe du joueur : fonction display_current_team(player_team)
#     La fonction reçoit le dictionnaire player_team contenant les héros déjà sélectionnés
#     Si le dictionnaire player_team est vide alors :
#         Afficher un message indiquant que l'équipe est actuellement vide
#     Sinon :
#         Afficher un message d'introduction indiquant la composition actuelle de l'équipe
#         Boucler sur les éléments du dictionnaire player_team 
#             (utiliser .items() pour récupérer la clé et la valeur) en gardant un index visuel :
#             Afficher le numéro de l'index, le nom du personnage (la clé), 
#                 ainsi que ses statistiques d'attaque, de défense et de pv 
#                 (les valeurs du dictionnaire interne)
def display_current_team(player_team):
    if player_team == {}:
        print("ÉQUIPE ACTUELLE VIDE")
    else:
        print("-" * 23)
        print("Voici votre composition actuelle : ")
        print("-" * 23)

        for i, (nom, stats) in enumerate(player_team.items()):
            print(f"{i + 1}. {nom} - {stats['attaque']} ATK - {stats['defense']} DEF - {stats['pv']} PV")


# Affichage de l'état du combat (pour la phase 2) : display_combat_state(monster, player_team)
#     Afficher le nom du monstre actuel et ses PV restants
#     Afficher l'état des personnages de l'équipe avec leurs PV restants