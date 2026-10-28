import time

from db_init import *
from game import *
from models import *
from utils import *


# Fonction pour quitter proprement : close_game()
def close_game():
    print("Fermeture du jeu...")
    time.sleep(1)
    raise SystemExit()


# Main Programme
database_connection()
time.sleep(2)

display_menu()
choix = player_choice(valid_choices=[1, 2, 3], error_function=display_menu)

if choix == 1:
    start_game()
elif choix == 2:
    show_scoreboard()
elif choix == 3:
    close_game()