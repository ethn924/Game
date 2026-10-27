# Dictionnaire global pour stocker tous les types d'erreurs explicitement balancées à l'utilisateur : ERRORS
#     "not_a_number": "Veuillez entrer un nombre valide"
#     "out_of_bounds": "Ce choix ne fait pas partie des options disponibles"
#     "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre"

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
