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
*   **Monnaie** : Variable `gold` initialisée à 0. Gain de `waves * 5` par vague gagnée.
*   **Objets** : Dictionnaire global `MARKET_ITEMS` dans `utils.py`. Objets donnant-donnant (ex: +ATK / -DEF).
*   **Affichage** : Fonction `display_market(item, gold)` dans `models.py`.
*   **Logique** : Fonction `apply_item_effect(item, player_team)` dans `utils.py`.

### Chantier 2 : Équilibrage
*   **Soin post-combat** : Fonction `heal_team(player_team)` dans `utils.py`. Applique un soin fixe (+20 PV) aux héros en vie après chaque vague.

### Chantier 3 : Les Boss
*   **Déclencheur** : Toutes les 5 vagues (vagues 5, 10, 15...).
*   **Logique** : Le monstre tiré au hasard subit une modification. Ses PV sont doublés, son attaque augmente de 20 et sa défense de 10. Son nom est préfixé par "BOSS ".
*   **Fonction** : `boost_monster_stats(monster)` dans `utils.py`.
*   **Affichage** : La fonction `display_combat_state` dans `models.py` affiche un avertissement visuel si le nom du monstre contient "BOSS".