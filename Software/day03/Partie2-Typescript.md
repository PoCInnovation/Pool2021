# Piscine Software - Jour 3 - Partie 2

✔ Comprendre et utiliser une ORM.

✔ Consolider les concepts des classes.

✔ S'initialiser aux décorateurs.

## Exercice 00 - Setup

Vous avez l'habitude, créer un dossier `day03` (toujours dans le même repo)
Créer une nouvelle application avec `npm init` et `npx eslint --init`

> Aidez-vous des jours précédents si nécessaires.

#### Ressources

- Premier exercice du day01

## Exercice 01 - Poser les bases

Nous allons créer une base de donnée postgres grâce à [TypeORM](https://typeorm.io/#/).
C'est une ORM basé sur des classes couplé à des décorateurs. Vos tables sont modélisées avec des classes, tout est donc typé et réutilisable !

### Setup

Installer TypeOrm et ses dépendances
```typescript
npm i typeorm pg pg-god reflect-metadata tsc --save
```

<Details><Summary><strong>Cliquer sur le toggle pour avoir une explication de chaque dépendances</strong></Summary>
- [Typeorm](https://github.com/typeorm/typeorm): ORM de gestion de base de donnée par classe / décorateurs
- [pg](https://github.com/brianc/node-postgres): Client postgres utiliser par TypeOrm pour gérer les requêtes
- [pg-god](https://github.com/ivawzh/pg-god): Intéragir avec postgres pour créer une base de donnée car TypeOrm ne la créée par nativement
- [reflect-metadata](https://github.com/rbuckton/reflect-metadata): Permet d'utiliser des décorateurs en Typescript.
- [tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html): Compilateur Typescript, permet d'activer les décorateurs sur le projet.
</Details>

Importer `reflect-metadata` dans le fichier `index.ts` pour que TypeORM puisse utiliser les décorateurs.
Copier le fichier `tsconfig.json` présent sur le repos du sujet et coller le fichier la racine de votre projet.

> Nous vous donnons directement le fichier afin de ne pas perdre de temps sur la configuration mais vous pouvez trouver une explication [ici](https://www.typescriptlang.org/tsconfig).

Créer maintenant un dossier `src/models`, c'est ici que nous allons stocker nos entités.

### Contexte

L'objectif du jour est de créer et intéragir avec une base de donnée contenant :
 - Des développeurs travaillant sur des projets
 - La fiche de contact de chaque développeurs
 - Des projets affectés à une équipe de développeurs

Ne vous inquiéter, tout vas se faire étape par étape.

### Let's code

Il est temps de créer votre première table. 
Comme dis précédemment, TypeOrm se base sur des [Classes](https://www.typescriptlang.org/docs/handbook/classes.html). Vous retrouverez donc les mêmes spécificités (héritage, constructeur, méthodes...).

#### Modéliser

Dans le fichier `src/models/Developer`, créer une classe `Developer` avec les propriétés suivantes:
 - `id` : la clé unique de notre table (type : `string`)
 - `name` : le nom du développeur
 - `age` : l'âge du développeur
 - `school` : l'école d'origine
 - `experience` : le nombre d'années d'expérience

> En base de donnée relationnel, chaque table contient un identifiant unique de façon à pouvoir distinguer chaque élément de cette table même si leur données sont les mêmes. Il est commun par sécurité de générer un `uuid` plutôt qu'un simple index.

> Par convention, un fichier définissant une classe portera le nom de celle-ci.

#### Instancier

Une fois votre classe créée, il faut la rendre utilisable par TypeORM.
Pour cela :
 - Votre classe `Developer` doit hériter des propriétés de la classe `BaseEntity`
 - Ajouter le décorateur `@Entity` sur votre classe.
 - Définissez vos attributs comme étant des colonnes grâce aux décorateurs `@Columns`

:warning: L'id est une colonne spéciale dites `Primaire`, utiliser un décorateur spécial qui vas _auto générée_ un `uuid`.

#### Assigner

Votre table est définie, mais n'oubliez pas, son comportement reste celui d'une classe.<br>
Créer un constructeur dans la classe qui vas venir prendre en paramètres les variables nécessaires à la création d'un développeur.<br>
Votre constructeur doit également exécuter la fonction `super` pour hériter des méthodes de la classe `BaseEntity`.

:bulb: L'exercice suivant vous permettra de vérifier si tout fonctionne comme prévu, vous pouvez néanmoins appeler un encadrant pour vérifier votre classe.

**Rendu :** `src/index.ts` et `src/models/Developer.ts`.

#### Ressources
- [Décorateurs](https://typeorm.io/#/decorator-reference)
- [TypeOrm](https://github.com/typeorm/typeorm)
- [Classe](https://www.typescriptlang.org/docs/handbook/classes.html)
- [L'héritage](https://codus.acyclique.com/fr/2017/11/01/classes-et-heritage-en-es6-et-typescript/)
- [UUID vs ID](https://medium.com/@Mareks_082/auto-increment-keys-vs-uuid-a74d81f7476a)

## Exercice 02 - Mise en db 

Vous avez modélisé votre première table, il faut maintenant l'indexer en db. Ce matin, vous avez appris à créer des données à la main, l'ORM vas se charger de cela automatiquement lorsque vous créer une connexion à votre base de donnée.
L'exercice va donc se faire en deux étapes : setup votre base de donnée puis vous y connecter.

### Configuration

Nous allons utiliser une base de donnée [Postgres](https://www.postgresql.org/). Il s'agit de l'une des plus connues et des plus simples à setup.
Pour créer une nouvelle de donnée, il vous suffit de lancer une image [Docker](https://www.docker.com/) de celle-ci.

> Docker est un système de containerisation très utilisé. Contenter vous d'exécuter les lignes que nous vous fournissons, vous verrez plus de détail demain.

Créer un fichier `.envrc` dans lequel vous allez mettre les variables d'environnement relatives à votre db :
 - `DB_USER` : le nom d'utilisateur de votre db
 - `DB_PASS` : le mot de passe
 - `DB_HOST` : l'host pour se connecter (ici : `localhost`)
 - `DB_PORT` : le port d'écoute de votre db
 - `DB_NAME` : le nom de la base de donnée.
 - `DB_URL` : l'url de connection, elle groupe toutes les informations ci-dessus (valeur : `postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME`)
 - `ENTITIES_FOLDER`: le dossier contenant vos tables (ici : `models`)`

> Il est possible de créer plusieurs db dans une seule base postgres, c'est pour cela qu'un nom est donnée à chaque db.
>
> :warning: N'oubliez pas de charger vos variables avec `direnv`.

Dans le fichier `appConfig.ts`, à l'aide de vos connaissances acquises au jour 2 :
 - Récupérer et exporter les variables : `DB_NAME`, `DB_URL` et `ENTITIES_FOLDER`.
 - Vous aurez également besoin d'exporter un objet `db` contenant les variables : `user`, `password`, `host`, `port` et `database`.

> L'objet db vous permettra de créer la db si elle n'existe pas. De plus, `database` correspond au type de la db donc `postgres`.

### Connection

A présent, dans le fichier `src/appDatabase.ts`, exporter une fonction _asynchrone_ `dbInitialize`.
Cette fonction doit :
 - Créer la base de donnée grâce à [pg-god](https://github.com/ivawzh/pg-god#programmatic-invocation)
 - Créer une connection à votre base de donnée.
 - Synchroniser les `models` pour créer les tables dans votre db. 

Appeler cette fonction dans votre `index.ts`
 - Si l'opération réussie, écrivez : `Database <nom de la db> is ready`
 - Si l'opération échoue, écrivez : `Failed to initialize database: <raison de l'échec>`

Ajouter dans votre `package.json` la commande suivante :

```json
"dev:db": "docker run --name ${DB_NAME} -e POSTGRES_PASSWORD=${DB_PASS} -e POSTGRES_USER=${DB_USER} -p ${DB_PORT}:${DB_PORT} -d postgres:alpine",
```

Cette commande vous permet de lancer un `container postgres respectant votre configuration placée dans l'environnement.
Vous avez maintenant une base de donnée lancée sur votre ordinateur.

> Il n'est pas rare d'ajouter le lancement de services externe directement dans votre `package.json`.

Exécuter la commande `npm run dev:db` puis `npm run start`.<br>
Si tout se passe bien, le message de succès devrait apparaître :joy:

> Vous pouvez également vous connecter à votre base de donnée grâce à Datagrip et voir votre table nouvellement créée.

**Rendu :** `src/appConfig.ts`, `src/appDatabase.ts` et `src/index.ts`

#### Ressources
- [Pg-god](https://github.com/ivawzh/pg-god#programmatic-invocation)
- [Docker X PostgreSQL](https://hub.docker.com/_/postgres)
- [Env-var](https://www.npmjs.com/package/env-var)
- [La connection aux db avec TypeOrm](https://typeorm.io/#/connection)
- [PostgreSQL](https://www.postgresql.org/)

## Exercice 03 - Le CRUD avec une ORM

Soyons sincère, une base de donnée vide ne sert à rien :joy:<br>
Il faut maintenant développer les fonctions pour lire, ajouter, modifier et supprimer un `Developer`. Autrement dit, le CRUD de celui-ci.

Vous allez créer un dossier `src/controllers` dans lequel vous allez stocker toutes les fonctions intéragissant avec la base de donnée.
Écrivez les fonctions ci-dessous dans le fichier `src/controllers/developerControllers.ts`.

### C comme Create

Créer une fonction _asynchrone_ `createDeveloper` qui prend en paramètre les attributs du futur développeur :
 - `name`
 - `age`
 - `school`
 - `experience`
La fonction doit créer un nouveau `Developer` et return le développeur une fois indexer en db.

### R comme Read

Créer une fonction _asynchrone_ `getDevelopers` qui renvoie tous les développeurs présents dans la base de donnée.

Créer une fonction _asynchrone `getDeveloper` qui prend en paramètre un `id` et renvoie un développeur si son id match celui donnée en paramètre.

### U comme update

Créer une fonction asynchrone _updateDeveloper qui prend en paramètres :
 - `id` : le développeur à modifier
 - `infos` : les informations du développeur
Elle doit modifier les attributs du développeur, sauvegarder le résultat en db puis le renvoyer.

Il faut pouvoir envoyer à la fonction autant d'attribut que l'on souhaite tant qu'ils sont *valides* et uniques.

Exemple : 
```typescript
updateDeveloper(id, { name: 'newName' }); // Fonctionne
updateDeveloper(id, { name: 'newName', age: 19, school: 'Epitech' }); // Fonctionne aussi
updateDeveloper(id, { name: 'newName', unknowPropertie: 'Unknown' }); // Doesn't work 
```

### D comme Delete

Créer une fonction _asynchrone_ `deleteDeveloper` qui prend en paramètre un `id` et supprime le développeur sélectionné.

**Rendu :** `src/controllers/developerControllers.ts`.

#### Ressources
- [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [BaseEntity](https://typeorm.delightful.studio/classes/_repository_baseentity_.baseentity.html)

## Exercice 04 - Contacter les développeurs

Si vous vous souvenez bien de l'exercice 1, la base de donnée finale doit contenir 3 tables : `Developer`, `Contact` et `Projects`.
Il est temps de créer la table `Contact`.

En base de donnée relationnelle, il existe 3 types de relations :
 - One to One : Une entité reliée à une autre (Exemple : Un développeur n'a qu'une fiche de contact)
 - One to Many : Une entité qui peut être relié à plusieurs exemplaires d'une autre entité (Exemple : Une entreprise à plusieurs employés mais un employé n'a qu'une entreprise)
 - Many to Many : Plusieurs entités relié à plusieurs autres entités d'une autre table (Exemple : Un développeur peuvent avoir des projets et un projet peut avoir plusieurs développeurs)

Vous l'avez compris, vous vous apprêtez à créer une relation du type `One to One`.

### Définir le modèle

Dans le fichier `src/models/Contact.ts`, créer une classe `Contact` à la manière de l'exercice 02 avec les attributs suivant :
 - `id` : l'identifient de la table
 - `email` : l'email du développeur
 - `phone` : le téléphone du développeur
 - `github` : le lien github du développeur
 - `linkedin` : le lien linkedin du développeur.
Vous ajouterez bien sure un `construteur` adapté.

### Créer le contrôleur

Dans le fichier `src/controllers/contactControllers.ts` :
 - Créer une fonction `addContact` qui prend en paramètre :
   - `id` : l'identifiant du développeur à lier
   - `email`, `phone`, `github`, `linkedin`, vous avez compris le concept
   La fonction doit renvoyer une erreur si le développeur n'existe pas.
   Sinon, elle doit créer un contact, l'affecter au développeur et renvoyer le résultat sauvegarder en bd.

  - Créer une fonction `updateContact` qui prend en paramètre :
    - `id` : l'identifiant du développeur à modifier
    - `infos` : l'objet `Contact` avec les nouvelles propriétés
    La fonction doit renvoyer une erreur si le développeur n'existe pas.
    Sinon elle doit modifier le contact et renvoyer le résultat sauvegarder.

> La fonction doit respecter les mêmes contraintes que la fonction `updateDeveloper`.

  - Créer une fonction `deleteContact` qui prend en paramètre l'`id`: l'identifiant du développeur à modifier.
    Renvoyer une erreur si le développeur n'existe pas. Sinon, renvoyer le résultat sauvegarder.

> N'oubliez pas de tester vos fonctions.

**Rendu :** `src/models/Contact.ts` et `src/controllers/contactControllers.ts`.

#### Ressources
- [Les relations dans une base de donnée](https://database.guide/the-3-types-of-relationships-in-database-design/)
- [Les relations dans TypeOrm](https://typeorm.io/#/relations)

> PoC - 2021
