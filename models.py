# Affichage du menu principal : fonction display_menu()
#     Déclarer une config globale : un tableau (liste) contenant des chaînes de caractères nommé MENU
#     Boucler sur chaque élément du tableau MENU en utilisant son index
#         Afficher le numéro de l'élément (index + 1) et le texte de l'élément

# Affichage des héros disponibles avec leurs caractéristiques : fonction display_heroes_list(heroes_list)
#     La fonction reçoit la liste des héros récupérée depuis la base de données via db_init.py
#     Afficher un message d'introduction pour la liste des personnages disponibles
#     Boucler sur la liste heroes_list pour extraire chaque héros (chaque héros étant un dictionnaire)
#         Extraire et afficher proprement les caractéristiques du héros : son nom, son type, son attaque, sa défense et ses pv de manière lisible

# Affichage de la composition actuelle de l'équipe du joueur : fonction display_current_team(player_team)
#     La fonction reçoit le dictionnaire player_team contenant les héros déjà sélectionnés
#     Si le dictionnaire player_team est vide alors :
#         Afficher un message indiquant que l'équipe est actuellement vide
#     Sinon :
#         Afficher un message d'introduction indiquant la composition actuelle de l'équipe
#         Boucler sur les éléments du dictionnaire player_team en gardant un index visuel :
#             Afficher le numéro de l'index, le nom du personnage, ainsi que ses statistiques d'attaque, de défense et de pv

# Global configuration
MENU = ["Démarrer le jeu", "Afficher le tableau des scores", "Quitter le jeu"]

def display_menu():
    for i in range(len(MENU)):
        print(i + 1, ":", MENU[i])