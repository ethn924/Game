# Dictionnaire global pour stocker tous les types d'erreurs explicitement balancées à l'utilisateur : ERRORS
ERRORS = {
    "not_a_number": "Veuillez entrer un nombre valide",
    "out_of_bounds": "Ce choix ne fait pas partie des options disponibles",
    "hero_already_chosen": "Ce héros est déjà dans votre équipe, choisissez-en un autre",
    "invalid_name": "Le nom choisi n'est pas valide (il ne doit pas être vide ou contenir uniquement des espaces)",
}

# Dictionnaire global pour stocker les objets du marché : MARKET_ITEMS
#     Liste de dictionnaires avec les clés : "nom", "prix", "bonus_atk", "bonus_def", "bonus_pv", "description"
MARKET_ITEMS = [
    {
        "nom": "Épée du Berserker", 
        "prix": 50, 
        "bonus_atk": 30, 
        "bonus_def": -10, 
        "bonus_pv": 0,
        "description": "Une lame lourde. (+30 ATK, -10 DEF)"
    },
    {
        "nom": "Armure de Plomb", 
        "prix": 40, 
        "bonus_atk": -5, 
        "bonus_def": 25, 
        "bonus_pv": 0,
        "description": "Lourde mais protectrice. (-5 ATK, +25 DEF)"
    },
    {
        "nom": "Élixir de Vie", 
        "prix": 30, 
        "bonus_atk": 0, 
        "bonus_def": 0, 
        "bonus_pv": 50,
        "description": "Soigne immédiatement. (+50 PV à tous)"
    }
]


# Fonction de validation du pseudo du joueur : is_valid_name(player_name)
def is_valid_name(player_name):
    player_name = player_name.strip()
    if player_name == "":
        return False
    else:
        return True


# Fonction d'affichage des erreurs : display_error(error_key)
def display_error(error_key):
    message = ERRORS.get(error_key, "Une erreur inconnue est survenue.")
    print(message)


# Conversion du choix en int : convert_to_int(player_choice)
def convert_to_int(player_choice):
    return int(player_choice)


# Calcul des dégâts infligés : calculate_damage(attaque, defense)
def calculate_damage(attaque, defense):
    result = attaque - defense
    if result <= 0:
        return 0
    else:
        return result


# Fonction pour soigner l'équipe après un combat : heal_team(player_team)
#     Je boucle sur player_team.items() pour récupérer name et hero_stats
#     Si hero_stats["pv"] > 0 :
#         J'ajoute 20 à hero_stats["pv"]
def heal_team(player_team):
    for name, hero_stats in player_team.items():
        if hero_stats["pv"] > 0:
            hero_stats["pv"] += 20


# Fonction pour générer les objets du marché : generate_market_items()
#     Je crée une liste vide market_selection
#     Je fais une boucle 2 fois :
#         Je pioche un objet au hasard dans MARKET_ITEMS avec random.choice
#         J'ajoute cet objet à market_selection
#     Je retourne market_selection
def generate_market_items():
    pass


# Fonction pour appliquer l'effet d'un objet du marché à un héros ciblé : apply_item_effect(item, target_hero)
#     J'ajoute item["bonus_atk"] à target_hero["attaque"]
#     J'ajoute item["bonus_def"] à target_hero["defense"]
#     J'ajoute item["bonus_pv"] à target_hero["pv"]
def apply_item_effect(item, target_hero):
    pass


# Fonction pour transformer un monstre en Boss : boost_monster_stats(monster)
#     Je modifie monster["nom"] en lui ajoutant "BOSS " devant
#     Je multiplie monster["pv"] par 2
#     J'ajoute 20 à monster["attaque"]
#     J'ajoute 10 à monster["defense"]
#     Je retourne monster modifié
def boost_monster_stats(monster):
    monster["nom"] = "BOSS " + monster["nom"]
    monster["pv"] = monster["pv"] * 2
    monster["attaque"] += 20
    monster["defense"] += 10
    return monster


# Fonction d'équilibrage des monstres selon la vague : scale_monster(monster, waves)
#     Je calcule un multiplicateur basé sur la vague : (1 + waves * 0.1)
#     Je multiplie monster["attaque"] par ce multiplicateur
#     Je multiplie monster["defense"] par ce multiplicateur
#     Je multiplie monster["pv"] par ce multiplicateur
#     Je retourne monster modifié
def scale_monster(monster, waves):
    pass


# Sélection et validation du choix du joueur : player_choice(valid_choices, error_function)
#     La fonction reçoit la liste des choix valides (valid_choices) et la fonction d'affichage d'erreur (error_function).
#     while True:
#         Récupérer le choix utilisateur avec un input
#         Vérifier si le choix est bien un nombre avec la méthode isdigit() (suivie de parenthèses)
#         Si ce n'est pas un nombre (isdigit renvoie False) :
#             Lancer display_error("not_a_number")
#             Appeler error_function() pour réafficher le menu ou l'interface
#             continue pour forcer un nouveau choix
#         Appeler la fonction convert_to_int() pour transformer la chaîne saisie en entier et stocker le résultat
#         Vérifier si l'entier obtenu n'est pas dans la liste valid_choices
#         Si l'entier n'est pas dedans :
#             Lancer display_error("out_of_bounds")
#             Appeler error_function() pour réafficher le menu ou l'interface
#             continue pour forcer un nouveau choix
#         Si le choix est valide :
#             return le choix converti en entier
def player_choice(valid_choices, error_function):
    while True:
        player_choice = input("Faites votre choix : ")
        if not (player_choice.isdigit()):
            display_error("not_a_number")
            error_function()
            continue

        int_choice = convert_to_int(player_choice)

        if int_choice not in valid_choices:
            display_error("out_of_bounds")
            error_function()
            continue
        else:
            return int_choice