## Description de l'application  

L'application est une liste de courses avec une interface en ligne de commandes. On peut ajouter des objets et afficher sa liste, et elle prend en compte plusieurs utilisateurs.  

## Objectif de l'application   

Lorsque nous lançons notre application, on demande le nom de l'utilisateur.  
Si l'utilisateur existe déjà il lui indique sa liste actuelle, sinon il lui crée son compte et lui dit que c'est un nouvel utilisateur avec une liste vide.  
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

Pour lancer les tests sur la base de données :

```
python3 DbTests.py
```

Pour lancer les tests unitaires sur les inputs :

```
python3 InputTests.py
```

Pour lancer les tests de comportement du programme :

```
python3 ParcoursTests.py
```

NB : Il peut être nécessaire d'installer mock avec la commande suivante :

```
pip install mock
```

Pour lancer les tests de fuzzing :

```
python3 fuzzing/fuzzing_action.py
python3 fuzzing/fuzzing_item.py
python3 fuzzing/fuzzing_name.py
python3 fuzzing/fuzzing_quantity.py
```


NB : Il peut être nécessaire d'installer atheris avec la commande suivante :

```
pip3 install atheris
```

## Tests

Concernant les tests, nous avons d'abord choisi de privilégier les tests unitaires sur les vérifications des input reçus, et sur les appels à la base SQLite.  
Puis, nous nous sommes concentrés sur des exemples de parcours utilisateur de l'application, avec des inputs mockés ou sous la forme de fuzzing.

**Tests sur la base de données : DbTests**  
On utilise une base SQLite sur laquelle on fait différentes opérations :
 - on crée les tables si on ne se base pas sur un fichier existant
 - on insère des données, des `personnes`, des `objets` et des `quantités` d'objets dans une liste
 - on vérifie l'existence de ces trois entités
 - on modifie une quantité, en ajoutant à la liste un objet déjà existant
Le fichier `DbTests.py` crée une base SQLite de test, sur laquelle ces méthodes vont être comparées aux requêtes sql qu'elles sont censées reproduire.  

**Tests sur les inputs : InputTests**  
L'interaction avec la base de données étant testée, il faut à présent se concentrer sur l'interaction avec l'utilisateur.  
Celui-ci va, à l'aide du terminal, fournir différents choix durant l'utilisation de l'application, notamment :
 - l'action qu'il veut effectuer
 - indiquer son nom
 - indiquer l'objet qu'il souhaite ajouter
 - indiquer la quantité dont il veut en ajouter  

Ces 4 données doivent respecter certains critères :
 - une quantité doit être un nombre, et a une valeur minimale et maximale
 - un nom et un objet ne peuvent pas être un nombre, et ont une taille minimale et maximale
 - une action se choisit par sa place dans la liste des actions, donc 1, 2 ou 3 et seulement ces trois choix.

Pour chacune de ces données, une méthode s'occupe de sa récupération et de savoir si elle répond à tous les critères.  
Ces méthodes peuvent être testées de manière unitaire en mockant la sortie de la fonction `input`.

**Tests de différents parcours utilisateur : ParcoursTests**  
Nous avons identifier plusieurs "parcours utilisateur type" que nous avons reproduit afin de les tester : 
 - un utilisateur non connu de la base de donnée doit être créé en indiquant son nom
 - un utilisateur non connu de la base de données doit avoir une liste vide une fois celui-ci créé
 - il est possible de quitter l'application avec un CTRL-C, et l'action "3 - quitter le programme" a le même comportement
 - l'ajout d'un objet dans la liste est atomique, si l'actioon n'est pas entièrement validée, ni objet ni quantité ne sont insérés en base
 - l'ajout d'un objet non connu de la base de données dans une liste, crée l'objet en base et la quantité associée
 - un utilisateur connu de la base de données aura sa liste d'affichée à sa connexion

**Tests d'interaction avec l'utilisateur**  

Les méthodes d'interaction avec la base et de filtrage des inputs sont testées, mais il faut s'assurer que l'interaction avec l'utilisateur a le comportement souhaité.  
Pour cela, nous avons pensé à deux façons de faire :

La méthode de `fuzzing testing`, qui consiste à envoyer des inputs aléatoires à l'application, nous permettra de savoir si elle réagit de la bonne manière, ex : si une valeur est incorrecte, elle indique l'erreur et propose d'en renseigner une nouvelle.
Chaque méthode se trouve dans des fichiers différents car un test dure beaucoup de temps.

Tester la cohérence de l'application. Même si la base est locale, l'application stocke plusieurs utilisateurs et peut même être lancée plusieurs fois en même temps avec le même compte. On doit donc s'assurer de la cohérence des données, qu'un changement sur le compte 1 fait par l'utilisateur A se répercute sur le compte 1 utilisé par l'utilisateur B. 

Ces deux méthodes de test n'ont pas encore été implémentées, nous avons souhaité nous concentrer sur les tests techniques en priorité pour s'assurer du bon fonctionnement interne de l'application.  
Nous avons également pensé à renforcer nos tests unitaires avec du `mutation testing`, même si les cas pouvant être mutés sont assez restreints.

## Tests sans Mock  
Les tests sur la vérification des inputs et sur les parcours utilisateur sont faits en mockant les méthodes `input` et `print` de Python. Nous avons trouvé cette manière de faire plus accessible et plus facile pour traiter tous les cas à traiter.  
Sans les mocks, nous pouvions tester "à la main" en lançant l'application et en testant différents inputs, ou différents parcours, mais on perd tout l'intérêt d'automatisation des tests.  
Nous aurions aussi pu créer un script qui appelle et interagit avec notre programme, celui-ci aurait générer les différents inputs, ou simuler les différents parcours utilisateur, et aurait comparé le texte reçu par l'application avec le texte attendu.