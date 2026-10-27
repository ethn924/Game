# Fonction pour quitter proprement : close_game()
#     Afficher un message de fermeture
#     Quitter proprement avec raise SystemExit()

# Main Programme
# Établir ou vérifier la connexion initiale à la BDD avec database_connection()
# Afficher le menu principal une première fois avec display_menu()
# Récupérer le choix initial du joueur avec player_choice en lui passant max_options=3 et error_function=display_menu
# Si choix égal 1 alors :
#     Appel start_game() de game.py
# Si choix égal 2 alors :
#     Appel show_scoreboard() de game.py
# Si choix égal 3 alors :
#     Appel close_game()