from db_init import *
from game import *
from models import *
from utils import *

# Fonction pour quitter proprement : close_game()
#     Afficher un message de fermeture
#     Quitter proprement avec raise SystemExit()

# Main Programme
# Établir ou vérifier la connexion initiale à la BDD avec database_connection() (provenant de db_init.py)
# Afficher le menu principal une première fois avec display_menu() (provenant de models.py)
# Récupérer le choix initial du joueur avec player_choice() (provenant de utils.py) en lui passant max_options=3 et error_function=display_menu
# Si choix égal 1 alors :
#     Appel start_game() (provenant de game.py)
# Si choix égal 2 alors :
#     Appel show_scoreboard() (provenant de game.py)
# Si choix égal 3 alors :
#     Appel close_game()


def close_game():
    print("Fermeture du jeu...")
    raise SystemExit()  # On sort du programme


# Établissement ou vérification de la connexion avec BDD Game
database_connection()
# Affichage du menu
display_menu()
# Récupération du choix du joueur, pour l'instant que 3 options disponibles
choix = player_choice(max_options=3, error_function=display_menu)

if choix == 1:
    start_game()
elif choix == 2:
    show_scoreboard()
elif choix == 3:
    close_game()