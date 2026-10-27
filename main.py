# Selon choix du joueur : si démarrer jeu (1) alors appel fonction start_game()
# Fonction start_game():
#     Se connecter à la BDD pour faire la requête avec database_connection()
#     Gestion des équipes : Saisie du nom du joueur avant la création d'une équipe
#     Demander avec un input le pseudo du joueur et le stocker dans la variable player_name
#     Cible la collection heroes
#     Effectuer un find en appliquant un filtre pour enlever le _id
#     Convertir le curseur MongoDB en liste heroes_list
#     Passer à la création de l'équipe en appelant la fonction create_team(heroes_list)
#     Retourner cette équipe et le nom du joueur pour la suite de la partie

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
