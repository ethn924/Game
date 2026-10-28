# RPG Game - Python & MongoDB - SlayMon

## Architecture des fichiers

* main.py : Point d'entrée du programme et boucle du menu principal.
* db_init.py : Connexion MongoDB et requêtes de données (héros, monstres, scores).
* game.py : Déroulement de la partie, sélection de l'équipe et logique du combat.
* models.py : Fonctions d'affichage des menus, de la liste des héros et de l'équipe actuelle.
* utils.py : Fonctions utilitaires, conversion de types, calculs et données globales.

## Chantiers

### Chantier 1 : Le Marché et la Monnaie
*   **Déclencheur** : Toutes les 5 vagues. 
*   **Ordre d'exécution** : Le marché doit s'afficher **avant** le combat de boss.
*   **Monnaie** : Variable `gold` initialisée à 0. Gain de `waves * 5` par vague gagnée.
*   **Objets** : Dictionnaire global `MARKET_ITEMS` dans `utils.py`.
*   **Logique** : Fonction `apply_item_effect(item, target_hero)` dans `utils.py`. L'effet ne s'applique plus à toute l'équipe, mais à un seul héros ciblé.

### Chantier 2 : Équilibrage
*   **Soin post-combat** : Fonction `heal_team(player_team)` dans `utils.py`. Applique un soin fixe (+20 PV) aux héros en vie après chaque vague.
*   **Scale des monstres** : Fonction `scale_monster(monster, waves)` dans `utils.py`. Augmente l'attaque, la défense et les PV des monstres en fonction du numéro de la vague pour éviter qu'un héros avec une grosse armure ne soit increvable.

### Chantier 3 : Les Boss
*   **Déclencheur** : Toutes les 5 vagues (vagues 5, 10, 15...).
*   **Ordre d'exécution** : Le boss apparaît **après** que le joueur a eu la possibilité d'acheter des objets au marché.
*   **Logique** : Le monstre tiré au hasard subit une modification. Ses PV sont doublés, son attaque augmente de 20 et sa défense de 10. Son nom est préfixé par "BOSS ".
*   **Fonction** : `boost_monster_stats(monster)` dans `utils.py`.

### Chantier 4 : Choix du héros pour l'objet
*   **Logique** : Quand le joueur achète un objet, le jeu doit lui demander à quel héros de son équipe il souhaite attribuer cet objet.
*   **Fonction** : `choose_hero_for_item(player_team)` dans `game.py`. Elle utilise `player_choice` et retourne le nom du héros ciblé.

### Chantier 5 : Marché avec choix multiple
*   **Logique** : Le marché ne propose plus un seul objet, mais une liste de 2 objets générés aléatoirement.
*   **Fonction** : `generate_market_items()` dans `utils.py`. Elle retourne une liste de 2 objets tirés au hasard.
*   **Affichage** : La fonction `display_market(items, gold)` dans `models.py` doit être modifiée pour afficher les 2 objets, leur prix et leurs effets.