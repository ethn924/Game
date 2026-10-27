# Dictionnaire global pour stocker tous les types d'erreurs explicitement balancées à l'utilisateur : ERRORS
#     "not_a_number": "Veuillez entrer un nombre valide"
#     "out_of_bounds": "Ce choix ne fait pas partie des options disponibles"
#     "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre"
#     "invalid_name": "Le nom choisi n'est pas valide (il ne doit pas être vide ou contenir uniquement des espaces)"

# Fonction de validation du pseudo du joueur : is_valid_name(player_name)
#     Nettoyer les espaces inutiles au début et à la fin du texte avec .strip()
#     Vérifier si la chaîne résultante n'est pas vide
#     Retourner True si le nom est valide, sinon retourner False

# Fonction d'affichage des erreurs : display_error(error_key)
#     Chercher le message associé au mot-clé error_key dans le dictionnaire ERRORS
#     Afficher le message d'erreur récupéré

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

# Dictionnaire d'erreurs
ERRORS = {
    "not_a_number": "Veuillez entrer un nombre valide",
    "out_of_bounds": "Ce choix ne fait pas partie des options disponibles",
    "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre",
    "invalid_name": "Le nom choisi n'est pas valide (il ne doit pas être vide ou contenir uniquement des espaces)"
}

def is_valid_name(player_name):
    player_name.strip()

    if (player_name == ""):  # noqa: SIM103
        return False
    else :
        return True

def display_error(error_key):
    
    message = ERRORS.get(error_key, "Une erreur inconnue est survenue.") # Si problèmes avec les clés
    print(message)
