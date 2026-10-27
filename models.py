# Affichage du menu : fonction display_menu()
#     config globale : tableau contenant des string : MENU = ["Démarrer le jeu", "Afficher le tableau des scores", "Quitter le jeu"]
#     Boucle sur tout élément de MENU
#         Afficher numéro élément et texte élément

# Affichage des héros disponibles avec leurs caractéristiques : fonction display_heroes_list(heroes_list)
#     Reçoit la liste retournée par start_game()
#     Afficher la liste des personnages disponibles pour le choix
#     Boucle sur la liste pour extraire chaque héros
#         Extraire et afficher proprement les caractéristiques nom, type, attaque, defense, pv de manière lisible

# Affichage de la composition actuelle de l'équipe du joueur : fonction display_current_team(player_team)
#     Si le dictionnaire player_team est vide alors :
#         Afficher Votre équipe est actuellement vide.
#     Sinon :
#         Afficher Composition actuelle de votre équipe :
#         Boucle sur les éléments de player_team avec un index visuel :
#             Afficher [Numéro] Nom du personnage - X ATK - X DEF - X PV
