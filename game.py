# Sélection des personnages pour constituer une équipe : fonction create_team(heroes_list)
#     Initialiser un dictionnaire vide player_team pour stocker l'équipe finale du joueur (3 héros max)
#     Initialiser un ensemble set vide pour assurer que chaque personnage ne peut être sélectionné qu'une seule fois
#     Boucler 3 fois tant que l'équipe n'est pas pleine :
#         Afficher l'état de l'interface de création d'équipe
#         Appeler display_current_team(player_team) pour montrer l'avancement actuel
#         Appeler display_heroes_list(heroes_list) pour l'interface proposant la liste des personnages disponibles
#         Appeler player_choice en lui passant le nombre maximum de héros de la liste et une fonction intermédiaire d'affichage
#         Récupérer le héros sélectionné dans heroes_list grâce au choix renvoyé
#         Vérifier si le nom du héros est déjà présent dans le set des héros sélectionnés :
#             Si présent alors lancer display_error("hero_already_chosen"), puis continue pour forcer un nouveau choix
#         Si absent alors :
#             Ajouter le nom du héros dans le set de suivi d'unicité
#             Ajouter le héros complet (Nom, Type, Attaque, Défense, PV) dans le dictionnaire player_team
#     Afficher l'équipe finale au joueur
#     Retourner le dictionnaire player_team

# Phase 2 : COMBAT
# Sélectionner un mot aléatoire, fonction qui va être appelée à chaque nouvelle wave : SelectRandomMonster()
# Fonction SelectRandomMonster():
#     Connexion à la db avec database_connection()
#     Accéder à la collection monsters
#     Récupérer tous les documents (monstres) avec find
#     Convertir le curseur MongoDB en liste de monstres
#     Sélectionner un monstre au hasard dans la liste
#     Retourner le dictionnaire du monstre choisi avec ses caractéristiques propres
