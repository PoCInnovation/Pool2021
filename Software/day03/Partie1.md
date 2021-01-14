# Piscine Software - Jour 3 - Partie 1

✔ Envoyer des requêtes SQL simples.

✔ Apprendre les bases de l'IDE Datagrip ou de SQL Online.

✔ Comprendre les fondamentaux des bases de données relationnelles.

## Exercice 00 - Setup

Vous avez deux possibilités, [Datagrip](https://www.jetbrains.com/fr-fr/datagrip/) ou [Sql IDE Online](https://sqliteonline.com/).

> Il est fortement conseillé d'utiliser Datagrip car c'est l'outil de gestion de base de donnée par excellence.

Vous trouverez le fichier `database_poc.sql` dans le dossier `resources` du day03. C'est un fichier sql vous permettant de générer une base de donnée contenant les membres de PoC et leurs différents projets.

### Datagrip 

Il vous faut d'abord installer Datagrip, vous pouvez télécharger cela grâce à la [Jetbrains ToolBox](https://www.jetbrains.com/toolbox-app/)

Vous allez d'abord lancer une base de donnée **postgresql** avec la commande suivante :

```sh
docker run  --name my_database -e POSTGRES_PASSWORD=password -e POSTGRES_USER=root -e POSTGRES_DB=my_database -p 5432:5432 -v "$(pwd)"/database_poc.sql:/docker-entrypoint-initdb.d/init.sql -d postgres:alpine
```

> :bulb: Ne vous inquiétez pas, vous comprendrez enfin la magie des commandes docker demain !

Connectez-vous à la base de donnée sur Datagrip.

Voici les informations à remplir :
- Base de donnée: `database`
- Username: `root`
- Password: `password`
- Host: `localhost`
- Port: `5432`

Vous devriez obtenir le résultat suivant :

![Database example on datagrip](https://github.com/PoCInnovation/Pool2021/blob/master/.github/assets/software-day3-database-example.png)

### SQL IDE Online

Connectez-vous à la base de donnée postgresql puis dans la catégorie `File`, ouvrez le fichier `database_poc.sql` et exécutez le fichier.

Vous devriez obtenir le résultat suivant :

![sql ide online](https://github.com/PoCInnovation/Pool2021/blob/master/.github/assets/software-day3-sql-ide.png)

### Let's code

Vous pouvez maintenant passer à la suite des exercises.

Appelez un encadrant pour vérifier vos requêtes après chaque exercice.

#### Ressources
- [Datagrip](https://www.jetbrains.com/fr-fr/datagrip/)
- [SQL IDE Online](https://sqliteonline.com/)

## Exercice 01 - La base des bases

Votre base de donnée est fin prête à accueillir vos premières requêtes.

L'objectif de cet exercice est de récupérer des informations sur la table `members`.

Vous allez faire 3 requêtes :

- Récupérer toutes les informations de la table `members`.
- Récupérer uniquement les noms et les rôles des membres.
- Récupérer la liste des membres ayant pour rôle `manager`.

#### Ressources
- [SELECT façon SQL](https://sql.sh/cours/select)
- [SELECT façon Postgres](https://www.postgresql.org/docs/9.5/sql-select.html)

## Exercice 02 - Joignez-vous à la fête

Vous avez récupéré les informations d'une table, il est temps de mettre en relations ses données. 

Vous allez écrire 3 nouvelles requêtes :
- Récupérer les noms des membres et des projets présents dans les tables `members` et `projects`. Vous devrez expliciter le nom des colonnes contenant des noms en `members_name` et `projects_name`.
- Récupérer tous les membres du projet `Researchshare`. 
- Récupérer tous les projets du responsable `petit.lucas@epitech.eu`. Les résultats devront être triés par pôle.

#### Ressources
- [Les jointures en SQL](https://sql.sh/cours/jointures)
- [Trier des données en SQL](https://docs.postgresql.fr/9.2/queries-order.html)

## Exercice 03 - Le CRUD

Lire des informations, c'est bien, mais il est primordial de pouvoir modifier sa base de donnée.

Vous allez écrire 3 requêtes :
- Ajouter un nouveau `membre`. Son `id` doit avoir la valeur `100`.
- Supprimer tous les projets ayant le status `done`.
- Ajouter le membre créé précédemment au projet `PoCZero`.

> :warning: N'oubliez pas, les membres et les projets sont reliés grâce à une table de relation, vous devrez peut-être faire votre suppression en deux temps. 

#### Ressources
- [Supprimer des éléments en SQL](https://sql.sh/cours/delete)
- [Ajouter des éléments en SQL](https://sql.sh/cours/insert-into)

## Exercice 04 - Les "count" sont bons

Vous allez maintenant voir les fonctions de pre-processing du SQL.

Vous allez vous servir d'outils d'agrégations pour relever des chiffres sur la base de donnée.

Pour cela, écrivez les 3 requêtes suivantes capables de :
- Compter le nombre de membres.
- Compter le nombre de projets par pôle.
- Compter le nombre de membres répartis sur les projets en les triant par pôle. Le résultat doit être trié dans l'ordre croissant.

> :warning: Faites attention aux doublons sur le dernier exercice.

#### Ressources
- [COUNT en SQL](https://sql.sh/fonctions/agregation/count)

## Exercice 05 - La famille Martin

Vous avez sûrement remarqué, il y a un nombre important de `xxxxxxx.martin@epitech.eu` parmi les membres de PoC.

La famille Martin aimerait organiser une petite fête, elle a besoin de vous pour dresser la liste des invités !

Faites une requête dans la base de donnée qui va renvoyer tous les membres de la famille Martin dans l'ordre alphabétique.

#### Ressources 
- [Manipuler des strings en SQL](https://sql.sh/fonctions/chaines-de-caracteres)

> PoC - 2021
