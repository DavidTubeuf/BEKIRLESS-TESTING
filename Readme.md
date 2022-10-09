## Objectif de l'application   

Lorsque nous lançons notre application, on demande le nom de l'utilisateur.  
Si l'utilisateur existe déjà il lui indique sa liste actuelle, sinon il lui dit que c'est un nouvel utilisateur avec une liste vide.  
Après ça, on propose à l'utilisateur trois choix :
 - Ajouter une quantité d'un article de sa liste
 - Afficher sa liste
 - Quitter l'application

## Architecture   

On a deux fichiers principaux pour faire marcher notre programme :  
 - `Query.py`, qui représente une classe contenant toutes les méthodes d'appel à la base SQLite, donc création/modification/suppression de table
 - `Main.py`, qui contient le programme principal, qui va afficher du texte et agir en fonction des réponses de l'utilisateur dans la console

## Exécution

Pour exécuter le programme :

```
python3 Main.py
```

Pour exécuter les tests d'intégration :

```
python3 TestsIntegration.py
```

Pour exécuter les tests sur les inputs :

```
python3 TestExtreme.py
```

NB : Il peut être nécessaire d'installer mock avec la commande suivante :

```
pip install mock
```

## Tests

Concernant les tests, nous avons choisi de privilégier les tests d'intégration ainsi que les tests sur les inputs.

Les tests d'intégration testent le bon fonctionnement de chacunes des méthodes en lien avec la base de données.

Concernant les inputs, nous avons mis en place 2 stratégies :

Nous testons dans un premier temps les cas "extrêmes", c'est à dire  xXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

Nous utilisons également la méthode de fuzzing testing, pour tester aléatoirement les inputs de l'application.

Tester si quantité pas numérique, si choix pas numérique
Tester la taille d'un item (nb de caractères) la taille de la quantité aussi
pas forcément besoin de pouvoir se déconnecter
test sur l'input aussi, genre ctrl X est-ce que ça fait ce qu'on veut 
test sur les insert, sur les update (vérifier qu'on veut bien ajouter à la quantité existante )
test de base de données aussi, si on a le droit aux doublons etc
tout ce qui paraît évident doit être testé

fuzzing testing - tous les types d'input (item et nombre)
surcharger la base  
nom vide dans l'input
soit on teste cohérence soit une seule connexion à la fois (plutôt sur la cohérence)
- modif accessible sur l'autre session
- deux modifs "en même temps" ne s'écrasent pas

tests d'intégration sur toutes les méthodes 

on doit faire une méthode qui print la liste ou "liste vide"

- ajouter les cas extrêmes sur les input reçus (Bekir) => tester, mutation testing 
- tests d'intégration (Tom)
- tests sur les input (sûrement un bash) / fuzzing (Louis)
- tests sur le fonctionnement de la bdd (cohérence, surcharge) sûrement un bash aussi du coup (david)
- 