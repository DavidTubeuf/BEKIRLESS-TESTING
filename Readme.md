## Objectif de l'application   

On lance le script python, on nous demande qui on est   
L'utilisateur répond un nom, s'il existe déjà il lui indique sa liste actuelle, sinon il lui dit que c'est un nouvel utilisateur avec une liste vide  
Après ça, on propose à l'utilisateur trois choix :
 - ajouter une quantité d'un article de sa liste
 - supprime une quantité d'un article de sa liste ?
 - afficher sa liste
 - (quitter) ?


## Architecture   

On a deux fichiers principaux pour faire marcher notre programme :  
 - `Query.py`, qui représente une classe contenant toutes les méthodes d'appel à la base SQLite, donc création/modification/suppression de table
 - `Main.py`, qui contient le programme principal, qui va afficher du texte et agir en fonction des réponses de l'utilisateur dans la console

Peut être qu'un item et une personne n'ont pas besoin d'id parce qu'il ne peut y avoir qu'une seul item et qu'une seule personne du même nom

## Comportement dans le code  

**Pour l'authentification :**  
Si on donne un nom d'utilisateur qui n'existe pas encore (on fait un select where name = name), on le crée en base + on le stock dans le while(true) du main   

**Pour les ajouts :**  
Si on donne un nom d'item inexistant, on le crée en base et on l'ajoute à la liste de la personne en cours (pas besoin de le stocker quelque part on le retrouvera avec un select)  
Si on donne un nom d'item existant et pas encore dans la liste, on l'ajoute à la liste de la personne  
Si on donne un nom d'item existant et déjà dans la liste, on indique la quantité déjà présente et la quantité nouvelle  

**Pour les suppressions :**  
Si on donne un nom d'item inexistant ou existant et pas dans la liste, on dit que la liste ne contient pas de cet item  
Si on donne un nom d'item existant et déjà dans la liste, on indique la quantité déjà présente et la quantité nouvelle (si on en retire pas trop)   
Si on donne un nom d'item existant et dans la liste mais qu'on veut trop en retirer, on indique la quantité actuelle et qu'il est impossible d'en retirer autant


# A ajouter
après avoir ajouté un item, afficher sa quantité actuelle (il pouvait déjà être présent donc aurait une quantité pas forcément connue)

## Idées de test

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

## à faire

l'utilisateur peut indiquer son nom :
 - pas un nombre
 - au moins deux caractères
 - au plus 20 caractères (arbitraire)

l'utilisateur peut agir jusqu'à 3 fois par itération :
 - action
 - objet
 - quantité

on teste l'action :
 - entre 1, 2 ,3

on teste l'objet :
 - pas un nombre
 - au moins deux caractères
 - au plus 20 caractères (arbitraire)

on teste la quantité :
- un nombre
- pas négatif ou nul
- au plus 100 

on doit faire une méthode qui print la liste ou "liste vide"

- ajouter les cas extrêmes sur les input reçus (Bekir) => tester, mutation testing 
- tests d'intégration (Tom)
- tests sur les input (sûrement un bash) / fuzzing (Louis)
- tests sur le fonctionnement de la bdd (cohérence, surcharge) sûrement un bash aussi du coup (david)
- 