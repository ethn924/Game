# Dictionnaire global pour stocker tous les types d'erreurs explicitement balancées à l'utilisateur : ERRORS
#     "not_a_number": "Veuillez entrer un nombre valide"
#     "out_of_bounds": "Ce choix ne fait pas partie des options disponibles"
#     "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre"
#     "invalid_name": "Le nom choisi n'est pas valide (il ne doit pas être vide ou contenir uniquement des espaces)"
ERRORS = {
    "not_a_number": "Veuillez entrer un nombre valide",
    "out_of_bounds": "Ce choix ne fait pas partie des options disponibles",
    "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre",
    "invalid_name": "Le nom choisi n'est pas valide (il ne doit pas être vide ou contenir uniquement des espaces)",
}


# Fonction de validation du pseudo du joueur : is_valid_name(player_name)
#     Nettoyer les espaces inutiles au début et à la fin du texte avec .strip()
#     Vérifier si la chaîne résultante n'est pas vide
#     Retourner True si le nom est valide, sinon retourner False
def is_valid_name(player_name):
    player_name = player_name.strip()

    if player_name == "":  # noqa: SIM103
        return False
    else:
        return True


# Fonction d'affichage des erreurs : display_error(error_key)
#     Chercher le message associé au mot-clé error_key dans le dictionnaire ERRORS
#     Afficher le message d'erreur récupéré
def display_error(error_key):
    message = ERRORS.get(
        error_key, "Une erreur inconnue est survenue."
    )  # Si clé absente ou problèmes
    print(message)


# Conversion du choix en int : fonction convert_to_int(player_choice)
#     Convertir la chaîne reçue en entier int
#     Retourner l'entier obtenu
def convert_to_int(player_choice):
    player_choice_int = int(player_choice)

    return player_choice_int


# Calcul des dégâts infligés (pour le combat) : calculate_damage(attaque, defense)
#     L'énoncé stipule que la défense réduit les dégâts.
#     Calculer les dégâts : attaque - defense
#     Si le résultat est inférieur ou égal à 0, retourner 0 (pour éviter de soigner l'adversaire)
#     Sinon, retourner le résultat


# Sélection et validation du choix du joueur : fonction player_choice(max_options, error_function)
#     La fonction reçoit deux paramètres : max_options (le nombre maximum de choix possibles) 
#         et error_function (la fonction d'affichage à rappeler en cas d'erreur, 
#         provenant du fichier models.py).
#     while True:
#         Récupérer le choix utilisateur avec un input
#         Vérifier si le choix est bien un nombre avec la méthode isdigit() 
#             (qui doit être suivie de parenthèses)
#         Si ce n'est pas un nombre (isdigit renvoie False) :
#             Lancer display_error("not_a_number")
#             Appeler error_function() pour réafficher le menu ou l'interface
#             continue pour forcer un nouveau choix
#         Appeler la fonction convert_to_int() pour transformer la chaîne saisie en entier 
#             et stocker le résultat
#         Vérifier si l'entier obtenu n'est pas compris entre 1 et max_options
#         Si l'entier est hors des bornes :
#             Lancer display_error("out_of_bounds")
#             Appeler error_function() pour réafficher le menu ou l'interface
#             continue pour forcer un nouveau choix
#         Si le choix est valide :
#             return le choix converti en entier
def player_choice(max_options, error_function):
    while True:
        player_choice = input("Faites votre choix : ")

        if not (player_choice.isdigit()):
            display_error("not_a_number")
            error_function()
            continue

        int_choice = convert_to_int(player_choice)

        if int_choice < 1 or int_choice > max_options:
            display_error("out_of_bounds")
            error_function()
            continue
        else:
            return int_choice