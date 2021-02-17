# PoC Software 2021 - Go - Day3, part2

✔ Comprendre et utiliser une ORM.

✔ Consolider les concepts des classes.

# Sommaire

- [0 - Setup](#0---setup)
- [1 - Poser les bases](#1---poser-les-bases)
- [2 - Mise en DB](#2---mise-en-db)
  - [1. Configuration](#1-configuration)
  - [2. Connexion](#2-connexion)
- [3 - Le CRUD avec un ORM](#3---le-crud-avec-un-orm)
  - [1. C comme Create](#1-c-comme-create)
  - [2. R comme Read](#2-r-comme-read)
  - [3. U comme Update](#3-u-comme-update)
  - [4. D comme Delete](#4-d-comme-delete)
- [4 - Contacter les développeurs](#4---contacter-les-développeurs)
  - [1. Définir le model](#1-définir-le-model)
  - [2. Lier les tables](#2-lier-les-tables)
  - [3. Créez le contrôleur](#3-créez-le-contrôleur)
- [5 - Des développeurs compétents](#5---des-développeurs-compétents)
- [6 - Des développeurs actifs](#6---des-développeurs-actifs)
- [Bonus](#bonus)

# 0 - Setup

- À la racine du répo, créez un dossier Day3.
- Initialisez un module SoftwareGoDay3.


# 1 - Poser les bases

L'objectif du jour est de créer et interagir avec une base de données contenant:
- Des développeurs travaillant sur des projets.
- La fiche de contact de chaque développeur.
- Des projets affectés à une équipe de développeurs.

Ne vous inquiétez pas, tout va se faire étape par étape.

Pour cela, nous allons utiliser PostgreSQL via [GORM](https://gorm.io/) (`go get -u gorm.io/gorm`).
GORM se base sur des [models](https://gorm.io/docs/models.html).
Vous retrouverez donc les mêmes spécificités (structure embedded, méthodes...).

> Nous utilisons GORM car il est plus facile à prendre en main cependant sa documentation est peu fournie
> et il a quelques bugs inexpliqué ce n'est donc pas un très bon choix pour un projet conséquent avec des
> intéractions DB complexes.
>
> Si vous êtes déjà à l'aise avec les bases de données, vous pouvez utiliser [Ent](https://entgo.io/) à la place.

- Créer un package `models`, nous y déclarerons nos entités.
- Créer un fichier `Developer.go` & une structure `Developer` dont les champs sont les suivants:
  - `ID` (clef unique de notre table), un `Name`, `Age`, `School` & `Experience`.

> Dans une DB relationnelle, chaque table contient un identifiant unique, de façon à pouvoir distinguer
> chaque élément de cette table même si leurs données sont les mêmes.
>
> GORM, dans [son model de base](https://gorm.io/docs/models.html#gorm-Model), fournit un certain nombre
> de champs avec lesquels le modèle peut travailler plus facilement.

> Il est aussi commun par sécurité de générer un `uuid` plutôt qu'un simple index.

> Par convention, un fichier définissant un model portera le nom de celle-ci.

### **Ressources**
- [gorm.Model](https://gorm.io/docs/models.html#gorm-Model)


# 2 - Mise en DB

Vous avez modélisé votre première table, il faut maintenant l'indexer en db. Vous avez appris à créer des bases de données
à la main, l'ORM vas se charger de cela automatiquement lorsque vous créez une connexion à votre base de données.
L'exercice va donc se faire en deux étapes:
- Setup votre base de données.
- Vous y connecter.

## 1. Configuration

Nous allons utiliser une base de données [Postgres](https://www.postgresql.org/). Il s'agit de l'une des plus connues
et des plus simples à mettre en place. Pour créer une nouvelle base de données, il vous suffit de lancer
l'image [Docker](https://www.docker.com/) de celle-ci.

> Docker est un système de containerisation très utilisé.
> Contentez-vous d'exécuter les commandes que nous vous fournissons, vous verrez plus de détails demain.

Créer un fichier `.env` dans lequel vous allez mettre les variables d'environnement relatives à votre db:

[comment]: <> (- `DB_DRIVER` : le type de database utilisé &#40;ici : `postgres` mais peut être Mysql, Sqlite, ...&#41;)
- `DB_USER` le nom d'utilisateur de votre db.
- `DB_PASS` le mot de votre utilisateur pour votre db.
- `DB_HOST` l'host pour se connecter (ici : `localhost`)
- `DB_PORT` le port d'écoute de votre db
- `DB_NAME` le nom de la base de données.
- `DB_URL` l'url de connexion, elle groupe toutes les informations ci-dessus (valeur : `postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME`)
- `ENTITIES_FOLDER` le dossier contenant vos tables (ici : `models`)

> Il est possible de créer plusieurs db dans une seule base postgres, c'est pour cela qu'un nom est donné
> à chaque db.
>
> :warning: N'oubliez pas de charger vos variables.


> L'objet DB vous permettra de créer la DB si elle n'existe pas. De plus, `database` correspond au type de la DB donc `postgres`.

## 2. Connexion

- Créer un package `database`, nous y gérerons notre connexion et nos appels à notre DB.
- Créer un fichier `Database.go` & une struct `Database` avec les champs suivants:
  - `DB`, un pointeur va une db GORM.
  - Les variables nécessaire à la configuration de votre db.

> Il vous faudra garder aussi les informations sur la DB contenue dans votre fichier `.env`, récupérées depuis l'environnement.

> Gorm étant capable de gérer plusieurs types de Database différentes (Postgres, MySql, ...) et que ces
> database peuvent travailler un nombre de variables de config différentes, il serait intéressant de n'avoir
> qu'un seul champ contenant toutes les informations.
>
> Quel serait le type qui n'a pas encore été abordé dans cette piscine qui serait le plus adapté ?
>
> De la même manière, il serait intéressant de se base sur une variable d'environnement `DB_DRIVER` pour pouvoir
> changer de Database facilement, notamment pour pouvoir run vos tests unitaires (avec sqlite3).

- Créer une méthode `Init()` sur la structure `Database`.
  - Elle crée la DB grâce à [GORM](https://gorm.io/docs/connecting_to_the_database.html) et initialise la connection.
  - Elle synchronisee les `models` pour créer les tables dans votre db.

- Appeler cette méthode dans votre main.
  - Si l'opération réussie, écrivez : `Database <nom de la db> is ready`.
  - Si l'opération échoue, écrivez : `Failed to initialize database: <raison de l'échec>`.

TODO: Faire le docker-compose ??

> Vous pouvez également vous connecter à votre base de données grâce à Datagrip et voir votre table nouvellement créée.

### **Ressources**
- [Docker X PostgreSQL](https://hub.docker.com/_/postgres)
- [Env](https://github.com/joho/godotenv)
- [La connection aux db avec Gorm](https://gorm.io/docs/connecting_to_the_database.html)
- [PostgreSQL](https://www.postgresql.org/)


# 3 - Le CRUD avec un ORM

Il faut maintenant développer les fonctions pour lire, ajouter, modifier et supprimer un `Developer`. Autrement dit, le CRUD de celui-ci.
Vous allez créer un package `controllers` dans lequel vous allez stocker toutes les fonctions interagissant avec la base de données.

Écrivez les fonctions ci-dessous dans le fichier `Developer.go`.

## 1. C comme Create

Créez une fonction `CreateDeveloper` qui prend en paramètres les attributs du futur développeur :
- `name`
- `age`
- `school`
- `experience`

La fonction doit créer un nouveau `Developer` et retourner le développeur une fois indexé en db.

> Il serait utile de faire une méthode Create() sur le model `developer` pour indexer le developer en Db.

## 2. R comme Read

Créez une fonction `GetDevelopers` qui renvoie tous les développeurs présents dans la base de données.

Créez une fonction `GetDeveloper` qui prend en paramètre un `id` et renvoie un développeur si son id correspond à celui donné en paramètre.

> Il serait utile de faire une méthode GetByID() sur le model `developer` pour chercher le developer en Db.

## 3. U comme Update

Créez une fonction `updateDeveloper` qui prend en paramètres :
- `id` : l'identifiant du développeur à modifier
- les informations du développeur (sous la forme que vous voulez, vous pouvez regarder la doc de Gorm pour voir vos possibilités)

Elle doit modifier les attributs du développeur, sauvegarder le résultat en db puis le renvoyer.

> Il serait utile de faire une méthode Update() sur le model `developer` pour update le developer en Db.

## 4. D comme Delete

Créez une fonction `deleteDeveloper` qui prend en paramètre un `id` et supprime le développeur sélectionné.

> Il serait utile de faire une méthode Delete() sur le model `developer` pour chercher le developer en Db.


> Dans le même esprit que l'exercice 2, un des principes fondamentaux que vous devez garder à l'esprit en tant que développeur, c'est que les outils/packages qui vont servir vos besoins pendant 6 mois ne pourront plus convenir un jour.
> Si vous êtes en entreprise ou sur un grand projet, vous devrez alors réécrire des milliers de lignes de codes et/ou changer énormément l'architecture de votre programme.
>
> Ce n'est pas une bonne pratique. Il faut pouvoir `encapsuler` le comportement de vos dépendances et ainsi pouvoir changer de package facilement.
>
> Par example Gorm vous fourni le type gorm.DB qui permet de gérer n'importe qu'elle base de données supportée par Gorm. Si vous devez changer de Postgres à Sqlite (par exemple pour faire des tests unitaires), la seule chose qui changera, c'est la fonction utilisée pour initialiser la connexion à votre Database.
>
> Il serait donc une bonne pratique de pouvoir passer de Gorm à un autre ORM sans avoir à changer vos controllers.
>
> Il serait donc intéressant que les méthodes de vos modèles prennent en paramètre le pointeur vers la database `*gorm.DB`. Si vous devez un jour changer d'ORM, vous devrez donc réécrire un peu la Database et vos models, mais pas vos controllers.
>
> Pour l'instant cela suffira, mais cette réflexion peut-être menée beaucoup plus loin, et le Go vous fourni des outils adaptés.

> N'oubliez pas de tester vos fonctions.

### **Ressources**
- [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [CRUD with Gorm](https://gorm.io/docs/create.html)


# 4 - Contacter les développeurs

Si vous vous souvenez bien de l'exercice 1, la base de données finale doit contenir 3 tables : `Developer`, `Contact` et `Projects`.
Il est temps de créer la table `Contact`.

En base de données relationnelle, il existe 3 types de relations :
- One to One : Une entité reliée à une autre (Exemple : Un développeur n'a qu'une fiche de contact)
- One to Many : Une entité qui peut être reliée à plusieurs exemplaires d'une autre entité (Exemple : Une entreprise a plusieurs employés mais un employé n'a qu'une entreprise)
- Many to Many : Plusieurs entités reliées à plusieurs autres entités d'une autre table (Exemple : Un développeur peut avoir des projets et un projet peut avoir plusieurs développeurs)

Vous l'avez compris, vous vous apprêtez à créer une relation du type `One to One`.

## 1. Définir le model

Dans le fichier `models/Contact.go`, créer une structure `Contact` à la manière de l'exercice 02 avec les attributs suivant :
- `id` : l'identifiant de la table
- `email` : l'email du développeur
- `phone` : le téléphone du développeur
- `github` : le lien GitHub du développeur
- `linkedin` : le lien LinkedIn du développeur.

Vous ajouterez bien sûr les méthodes adaptées.

## 2. Lier les tables

Il faut maintenant définir la relation entre ces tables.<br>
Dans le fichier `models/Developer.go`:, ajoutez un attribut *optionnel* `contact` du type `Contact` à votre classe.

:warning: Si un développeur est supprimé, sa fiche de contact doit l'être également, on appelle cela une `cascade`.

## 3. Créez le contrôleur

Dans le fichier `controllers/Contact.go` :
- Créez une fonction `addContact` qui prend en paramètres :
  - `id` : l'identifiant du développeur à lier
  - `email`, `phone`, `github`, `linkedin`, vous avez compris le concept

La fonction doit renvoyer une erreur si le développeur n'existe pas.<br>
Sinon, elle doit créer un contact, l'affecter au développeur et renvoyer le résultat sauvegardé en db.

- Créez une fonction `updateContact` qui prend en paramètres :
  - `id` : l'identifiant du développeur à modifier
  - `infos` : les nouvelles propriétés, encore une fois sous la forme que vous préférez.

La fonction doit renvoyer une erreur si le développeur n'existe pas.<br>
Sinon elle doit modifier le contact et renvoyer le résultat sauvegardé.

> La fonction doit respecter les mêmes contraintes que la fonction `updateDeveloper`.

- Créez une fonction `deleteContact` qui prend en paramètre l'`id`: l'identifiant du Contact à supprimer.

Renvoyez une erreur si le développeur n'existe pas. Sinon, renvoyez le résultat sauvegardé.

> N'oubliez pas de tester vos fonctions.

### **Ressources**
- [One to One Gorm](https://gorm.io/docs/has_one.html)
- [Association](https://gorm.io/docs/associations.html#Delete-with-Select)

# 5 - Des développeurs compétents

Vous pouvez contacter vos développeurs, mais il serait peut-être appréciable d'avoir un peu plus d'informations sur eux avant ?<br>
Un étendu de leurs compétences par exemple ?

Vous allez mettre en place une relation `One to Many` entre la table `Developer` et la table `Competences`.

Ajoutez un fichier `models/Competence.go` dans lequel vous allez faire une structure `Competence` contenant les champs suivants :
- `id` : L'identifiant de la table
- `name` : Nom de la compétence
- `level` : Le niveau de maîtrise (entre 0 et 10)

Liez la table `Developer` à votre nouvelle table en `One to Many` et n'oubliez pas d'activer le mode `cascade` (au(x) bon(s) endroit(s)).

Créez un fichier `Competence` dans votre dossier `controllers` dans lequel vous allez écrire les trois fonctions habituelles pour intéragir avec vos tables :
- `addCompetence` qui prend en paramètres :
  - `id` : Identifiant du développeur
  - `name`: Nom de la compétence
  - `level`: Le niveau de la compétence

La fonction doit renvoyer une erreur si le développeur n'existe pas ou si le niveau de la compétence est invalide.<br>
Sinon, elle doit renvoyer le développeur modifié avec la nouvelle compétence.

- `updateCompetence` qui attend les paramètres :
  - `devId` : Identifiant du développeur
  - `competenceId`: Identifiant de la compétence
  - `infos` : L'objet `Competence` avec les nouvelles propriétés.

La fonction doit bien sûr renvoyer une erreur si le développeur ou la compétence n'existe pas.<br>
Sinon, renvoyer la compétence mise à jour.

> La fonction doit respecter les mêmes contraintes que la fonction `updateDeveloper`.

- `deleteCompetence` qui prend en paramètres :
  - `devId` : Identifiant du développeur
  - `competenceId` : Identifiant de la compétence

Renvoyer une erreur si l'un des deux identifient est inconnu, sinon renvoyer le développeur mis à jour.

> N'oubliez pas de modifier les `controllers` de `Developer` pour ajouter les compétences.

### Ressources
- [One to Many](https://gorm.io/docs/has_many.html)

# 6 - Des développeurs actifs

Il est temps de passer à l'étape finale : les projets.
L'exercice est volontairement moins guidé, vous avez appris tout le nécessaire sur le fonctionnement de Gorm pour vous documenter seul et réaliser l'exercice.

Votre modèle `Project` doit avoir les propriétés suivantes :
- `id`: Identifiant de la table
- `name`: Nom du projet
- `deadline`: La date de rendu du projet
- `type`: Le type de projet (du type ProjectType que vous trouverez dans le fichier `type.go` sur le repo)
- `developers`: Les développeurs sur le projet

Vous allez créer une relation `Many to Many` entre les développeurs et les projets.

> Documentez-vous bien sur la manière de faire et les décorateurs à utiliser.

Vous devrez ensuite écrire 6 controllers :
- `getProjects` qui renvoie tous les projets avec les développeurs associés.
- `createProject` qui prend en paramètres :
  - `name` : Nom du projet
  - `deadline` : Date limite du projet
  - `type` : Type du projet

Renvoyer le projet nouvellement créé.

> :warning: Attention à bien gérer les erreurs potentielles, une date *impossible* par exemple ?

- `updateProject` qui prend en paramètres :
  - `id` : Identifiant du projet
  - `infos` : Les infos à modifier

Renvoie le projet mise à jour

- `deleteProject` qui prend en paramètre l'id du projet à supprimer
- `addDevToProject` qui prend en paramètres :
  - `projectId` : Identifiant du projet
  - `devId` : Identifiant du développeur

Ajouter le projet au développeur donné

- `deleteDevFromProject` qui prend en paramètres :
  - `projectId` : Identifiant du projet
  - `devId` : Identifiant du développeur

Retirer le projet au développeur donné

> N'oubliez pas de gérer les erreurs en cas de projet ou développeur inconnu.

> Les tests sont toujours de rigueur :wink:

### Ressources
- [Many to Many](https://gorm.io/docs/many_to_many.html)

# Bonus

Voici un _petit_ bonus pratique et utile pour consolider vos connaissances :

Vous avez actuellement des modèles et des controllers, c'est un bon début pour une API avec une architecture MVC n'est-ce pas ?

> La structure MVC, Modèle, Vue, Controller est une architecture basique dans le développeur back-end.

L'objectif est de créer un serveur gin avec les routes nécessaires pour créer, modifier, afficher vos différents modèles.<br>
Vous pouvez bien évidemment utiliser les controllers, mais aussi en rajouter.

Basez-vous sur vos acquis pour terminer ce bonus.<br>
Bon courage !

## Ressources complémentaires

Si vous souhaitez en apprendre plus sur les bases de données, voici quelques liens intéressants :
- [Ent, un meilleur ORM](https://entgo.io/)
- [Les bases de données graph](https://medium.com/wiidii/pourquoi-sint%C3%A9resser-aux-bases-de-donn%C3%A9es-orient%C3%A9es-graphe-e650f0395951)
- [DGraph](https://dgraph.io/)
- [MongoDB](https://www.mongodb.com/fr)
