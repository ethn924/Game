# Tout d'abord je dois me connecter à ma BDD
# Définition des variables de connexion
# db_url = "mongodb://localhost:27017/"  Ma connection string
# db_name = "Game"  Nom de ma BDD

# Fonction pour me connecter à la BDD : database_connection()
#     Se connecter au client MongoClient avec db_url
#     Accéder à la BDD avec db_name
#     Afficher Connexion OK !
#     Retourner le client et la BDD game

# Dictionnaire global pour stocker tous les types d'erreurs explicitement balancées à l'utilisateur : ERRORS
#     "not_a_number": "Veuillez entrer un nombre valide"
#     "out_of_bounds": "Ce choix ne fait pas partie des options disponibles"

# Fonction d'affichage des erreurs : display_error(error_key)
#     Chercher le message associé au mot-clé error_key dans le dictionnaire ERRORS
#     Afficher le message d'erreur récupéré

# Affichage du menu : fonction display_menu()
#     config globale : tableau contenant des string : MENU = ["Démarrer le jeu", "Afficher le tableau des scores", "Quitter le jeu"]
#     Boucle sur tout élément de MENU
#         Afficher numéro élément et texte élément

# Affichage des héros : fonction display_heroes_list(heroes_list)
#     Reçoit la liste retournée par start_game()
#     Afficher Choisissez 3 héros !
#     Boucle sur la liste pour extraire chaque héros
#         Extraire et afficher proprement les caractéristiques nom, type, attaque, defense, pv de manière lisible

# Conversion du choix en int : fonction convert_to_int(player_choice)
#     Convertir la chaîne reçue en entier int
#     Retourner l'entier obtenu

# Menu affiché, ensuite, sélection du joueur : fonction player_choice(max_options, error_function)
#     while True:
#         Récupérer choix utilisateur avec un input
#         Vérifier si choix est valide
#         Si choix pas un nombre avec isdigit() alors :
#             Lancer display_error("not_a_number")
#             Lancer error_function()
#             continue
#         Conversion du choix avec la fonction convert_to_int
#         Si choix exprimé en int pas entre 1 et max_options alors :
#             Lancer display_error("out_of_bounds")
#             Lancer error_function()
#             continue
#         Si valide alors :
#             return le choix converti en entier

# Selon choix du joueur : si démarrer jeu (1) alors appel fonction start_game()
# Fonction start_game():
#     Se connecter à la BDD pour faire la requête avec database_connection()
#     Cible la collection heroes
#     Effectuer un find en appliquant un filtre pour enlever le _id
#     Convertir le curseur MongoDB en liste heroes_list
#     Appeler la fonction display_heroes_list(heroes_list)
#     Passer à la création de l'équipe avec create_team(heroes_list)
#     Retourner cette liste

# Fonction pour créer l'équipe du joueur : create_team(heroes_list)
#     Initialiser une liste vide pour l'équipe du joueur, équipe de 3 max
#     Boucler 3 fois tant que l'équipe n'est pas pleine :
#         Appeler player_choice en lui passant le nombre maximum de héros disponibles et la fonction display_heroes_list
#         Récupérer le héros sélectionné dans heroes_list grâce au choix renvoyé
#         Ajouter le héros à l'équipe du joueur
#     Afficher ou retourner l'équipe finale

# Si afficher les scores (2) alors appel de la fonction show_scoreboard()
# Fonction show_scoreboard():
#     Se connecter à la BDD avec database_connection()
#     Accéder à la collection scores
#     Récupérer tous les documents avec find
#     Filtrer les 3 meilleurs :
#         Trier le tableau sur element.waves
#         Prendre les 3 derniers éléments du tableau avec mon_array[-3:]
#     Afficher les 3 meilleurs

# Si quitter le jeu (3) alors appel de la fonction close_game()
# Fonction close_game():
#     Afficher un message de fermeture
#     Quitter proprement avec raise SystemExit()

# Main Programme
# Établir ou vérifier la connexion initiale à la BDD
# Afficher le menu principal une première fois avec display_menu()
# Récupérer le choix initial du joueur avec player_choice en lui passant max_options=3 et error_function=display_menu
# Si choix égal 1 alors :
#     Appel start_game()
# Si choix égal 2 alors :
#     Appel show_scoreboard()
# Si choix égal 3 alors :
#     Appel close_game()