# Piscine Software - Jour 3 - Partie 2

✔ Comprendre et utiliser une ORM.

✔ Consolider les concepts des classes.

✔ Découvrir les décorateurs.

## Exercice 00 - Setup

Vous avez l'habitude, créer un dossier `day03` (toujours dans le même repo).
Créer une nouvelle application avec `npm init` et `npx eslint --init`

> Aidez-vous des jours précédents si nécessaire.

#### Ressources

- Premier exercice du day01

## Exercice 01 - Poser les bases

Nous allons créer une base de données postgres grâce à [TypeORM](https://typeorm.io/#/).
C'est un ORM basé sur des classes couplé à des décorateurs. Vos tables sont modélisées avec des classes, tout est donc typé et réutilisable !

### Setup

Installez TypeOrm et ses dépendances
```typescript
npm i typeorm pg pg-god reflect-metadata tsc --save
```

<Details><Summary><strong>Cliquez sur le toggle pour avoir une explication de chaque dépendance</strong></Summary>

- [Typeorm](https://github.com/typeorm/typeorm) : ORM de gestion de base de données par classe / décorateurs
- [pg](https://github.com/brianc/node-postgres) : Client postgres utilisé par TypeOrm pour gérer les requêtes
- [pg-god](https://github.com/ivawzh/pg-god) : Interagir avec postgres pour créer une base de données car TypeOrm ne la créée par nativement
- [reflect-metadata](https://github.com/rbuckton/reflect-metadata) : Permet d'utiliser des décorateurs en Typescript.
- [tsc](https://www.typescriptlang.org/docs/handbook/compiler-options.html) : Compilateur Typescript, permet d'activer les décorateurs sur le projet.

</Details>

Importez `reflect-metadata` dans le fichier `index.ts` pour que TypeORM puisse utiliser les décorateurs.
Copiez le fichier `tsconfig.json` présent sur le repo du sujet et coller le fichier à la racine de votre projet.

> Nous vous donnons directement le fichier afin de ne pas perdre de temps sur la configuration mais vous pouvez trouver une explication [ici](https://www.typescriptlang.org/tsconfig).

Créez maintenant un dossier `src/entities`, c'est ici que nous allons stocker nos entités.

### Contexte

L'objectif du jour est de créer et intéragir avec une base de données contenant :
 - Des développeurs travaillant sur des projets
 - La fiche de contact de chaque développeur
 - Des projets affectés à une équipe de développeurs

Ne vous inquiétez pas, tout va se faire étape par étape.

### Let's code

Il est temps de créer votre première table. 
Comme dit précédemment, TypeOrm se base sur des [Classes](https://www.typescriptlang.org/docs/handbook/classes.html). Vous retrouverez donc les mêmes spécificités (héritage, constructeur, méthodes...).

#### Modéliser

Dans le fichier `src/entities/Developer`, créez une classe `Developer` avec les propriétés suivantes :
 - `id` : la clé unique de notre table (type : `string`)
 - `name` : le nom du développeur
 - `age` : l'âge du développeur
 - `school` : l'école d'origine
 - `experience` : le nombre d'années d'expérience

> En base de données relationnelle, chaque table contient un identifiant unique de façon à pouvoir distinguer chaque élément de cette table même si leurs données sont les mêmes. Il est commun par sécurité de générer un `uuid` plutôt qu'un simple index.

> Par convention, un fichier définissant une classe portera le nom de celle-ci.

#### Instancier

Une fois votre classe créée, il faut la rendre utilisable par TypeORM.
Pour cela :
 - Votre classe `Developer` doit hériter des propriétés de la classe `BaseEntity`
 - Ajoutez le décorateur `@Entity` sur votre classe.
 - Définissez vos attributs comme étant des colonnes grâce aux décorateurs `@Columns`

:warning: L'id est une colonne spéciale dite `Primaire`, utilisez un décorateur spécial qui va _auto générer_ un `uuid`.

#### Assigner

Votre table est définie, mais n'oubliez pas, son comportement reste celui d'une classe.<br>
Créee un constructeur dans la classe qui va venir prendre en paramètres les variables nécessaires à la création d'un développeur.<br>
Votre constructeur doit également exécuter la fonction `super` pour hériter des méthodes de la classe `BaseEntity`.

:bulb: L'exercice suivant vous permettra de vérifier si tout fonctionne comme prévu, vous pouvez néanmoins appeler un encadrant pour vérifier votre classe.

**Rendu :** `src/index.ts` et `src/entities/Developer.ts`.

#### Ressources
- [Décorateurs](https://typeorm.io/#/decorator-reference)
- [TypeOrm](https://github.com/typeorm/typeorm)
- [Classe](https://www.typescriptlang.org/docs/handbook/classes.html)
- [L'héritage](https://codus.acyclique.com/fr/2017/11/01/classes-et-heritage-en-es6-et-typescript/)
- [UUID vs ID](https://medium.com/@Mareks_082/auto-increment-keys-vs-uuid-a74d81f7476a)

## Exercice 02 - Mise en db 

Vous avez modélisé votre première table, il faut maintenant l'indexer en db. Vous avez appris à créer des données à la main, l'ORM vas se charger de cela automatiquement lorsque vous créez une connexion à votre base de données.
L'exercice va donc se faire en deux étapes : setup votre base de données puis vous y connecter.

### Configuration

Nous allons utiliser une base de données [Postgres](https://www.postgresql.org/). Il s'agit de l'une des plus connues et des plus simples à mettre en place.
Pour créer une nouvelle base de données, il vous suffit de lancer l'image [Docker](https://www.docker.com/) de celle-ci.

> Docker est un système de containerisation très utilisé. Contentez-vous d'exécuter les commandes que nous vous fournissons, vous verrez plus de détails demain.

Créer un fichier `.envrc` dans lequel vous allez mettre les variables d'environnement relatives à votre db :
 - `DB_USER` : le nom d'utilisateur de votre db
 - `DB_PASS` : le mot de passe
 - `DB_HOST` : l'host pour se connecter (ici : `localhost`)
 - `DB_PORT` : le port d'écoute de votre db
 - `DB_NAME` : le nom de la base de données.
 - `DB_URL` : l'url de connexion, elle groupe toutes les informations ci-dessus (valeur : `postgresql://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME`)
 - `ENTITIES_FOLDER`: le dossier contenant vos tables (ici : `entities`)`

> Il est possible de créer plusieurs db dans une seule base postgres, c'est pour cela qu'un nom est donné à chaque db.
>
> :warning: N'oubliez pas de charger vos variables avec `direnv`.

Dans le fichier `appConfig.ts`, à l'aide de vos connaissances acquises au jour 2 :
 - Récupérez et exportez les variables : `DB_NAME`, `DB_URL` et `ENTITIES_FOLDER`.
 - Vous aurez également besoin d'exporter un objet `db` contenant les variables : `user`, `password`, `host`, `port` et `database`.

> L'objet db vous permettra de créer la db si elle n'existe pas. De plus, `database` correspond au type de la db donc `postgres`.

### Connexion

À présent, dans le fichier `src/appDatabase.ts`, exportez une fonction _asynchrone_ `dbInitialize`.
Cette fonction doit :
 - Créer une connection à votre base de données.
 - Synchroniser les `entities` pour créer les tables dans votre db. 

Appelez cette fonction dans votre `index.ts`
 - Si l'opération réussie, écrivez : `Database <nom de la db> is ready`
 - Si l'opération échoue, écrivez : `Failed to initialize database: <raison de l'échec>`

Ajoutez dans votre `package.json` la commande suivante :

```json
"dev:db": "docker run --name ${DB_NAME} -e POSTGRES_PASSWORD=${DB_PASS} -e POSTGRES_USER=${DB_USER} -e POSTGRES_DB=${DB_NAME} -p ${DB_PORT}:${DB_PORT} -d postgres:alpine",
```

Cette commande vous permet de lancer un conteneur postgres respectant votre configuration placée dans l'environnement.
Vous avez maintenant une base de données lancée sur votre ordinateur.

> Il n'est pas rare d'ajouter le lancement de services externes directement dans votre `package.json`.

Exécutez la commande `npm run dev:db` puis `npm run start`.<br>
Si tout se passe bien, le message de succès devrait apparaître :joy:

> Vous pouvez également vous connecter à votre base de données grâce à Datagrip et voir votre table nouvellement créée.

**Rendu :** `src/appConfig.ts`, `src/appDatabase.ts` et `src/index.ts`

#### Ressources
- [Pg-god](https://github.com/ivawzh/pg-god#programmatic-invocation)
- [Docker X PostgreSQL](https://hub.docker.com/_/postgres)
- [Env-var](https://www.npmjs.com/package/env-var)
- [La connection aux db avec TypeOrm](https://typeorm.io/#/connection)
- [PostgreSQL](https://www.postgresql.org/)

## Exercice 03 - Le CRUD avec un ORM

Il faut maintenant développer les fonctions pour lire, ajouter, modifier et supprimer un `Developer`. Autrement dit, le CRUD de celui-ci.

Vous allez créer un dossier `src/models` dans lequel vous allez stocker toutes les fonctions interagissant avec la base de données.
Écrivez les fonctions ci-dessous dans le fichier `src/models/developerModels.ts`.

### C comme Create

Créez une fonction _asynchrone_ `createDeveloper` qui prend en paramètres les attributs du futur développeur :
 - `name`
 - `age`
 - `school`
 - `experience`
 
La fonction doit créer un nouveau `Developer` et retourner le développeur une fois indexé en db.

### R comme Read

Créez une fonction _asynchrone_ `getDevelopers` qui renvoie tous les développeurs présents dans la base de données.

Créez une fonction _asynchrone_ `getDeveloper` qui prend en paramètre un `id` et renvoie un développeur si son id correspond à celui donné en paramètre.

### U comme update

Créez une fonction asynchrone `updateDeveloper` qui prend en paramètres :
 - `id` : le développeur à modifier
 - `infos` : les informations du développeur
 
Elle doit modifier les attributs du développeur, sauvegarder le résultat en db puis le renvoyer.

:warning: Il faut pouvoir envoyer à la fonction autant d'attributs que l'on souhaite tant qu'ils sont *valides* et uniques.

Exemple : 
```typescript
updateDeveloper(id, { name: 'newName' }); // Fonctionne
updateDeveloper(id, { name: 'newName', age: 19, school: 'Epitech' }); // Fonctionne aussi
updateDeveloper(id, { name: 'newName', unknowProperty: 'Unknown' }); // Doesn't work 
```

### D comme Delete

Créez une fonction _asynchrone_ `deleteDeveloper` qui prend en paramètre un `id` et supprime le développeur sélectionné.

**Rendu :** `src/models/developerModels.ts`.

#### Ressources
- [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
- [BaseEntity](https://typeorm.delightful.studio/classes/_repository_baseentity_.baseentity.html)

## Exercice 04 - Contacter les développeurs

Si vous vous souvenez bien de l'exercice 1, la base de données finale doit contenir 3 tables : `Developer`, `Contact` et `Projects`.
Il est temps de créer la table `Contact`.

En base de données relationnelle, il existe 3 types de relations :
 - One to One : Une entité reliée à une autre (Exemple : Un développeur n'a qu'une fiche de contact)
 - One to Many : Une entité qui peut être reliée à plusieurs exemplaires d'une autre entité (Exemple : Une entreprise a plusieurs employés mais un employé n'a qu'une entreprise)
 - Many to Many : Plusieurs entités reliées à plusieurs autres entités d'une autre table (Exemple : Un développeur peut avoir des projets et un projet peut avoir plusieurs développeurs)

Vous l'avez compris, vous vous apprêtez à créer une relation du type `One to One`.

### Définir le modèle

Dans le fichier `src/entities/Contact.ts`, créez une classe `Contact` à la manière de l'exercice 02 avec les attributs suivant :
 - `id` : l'identifiant de la table
 - `email` : l'email du développeur
 - `phone` : le téléphone du développeur
 - `github` : le lien GitHub du développeur
 - `linkedin` : le lien LinkedIn du développeur.
 
Vous ajouterez bien sûr un `construteur` adapté.

### Lier les tables

Il faut maintenant définir la relation entre ces tables.<br>
Dans le fichier `src/entities/Developer.ts`:
 - Ajoutez un attribut *optionnel* `contact` du type `Contact` à votre classe.
 - Placez les *2* décorateurs adaptés pour créer votre liaison

:warning: Si un développeur est supprimé, sa fiche de contact doit l'être également, on appelle cela une `cascade`.

### Créez le contrôleur

Dans le fichier `src/models/contactModels.ts` :
 - Créez une fonction `addContact` qui prend en paramètres :
   - `id` : l'identifiant du développeur à lier
   - `email`, `phone`, `github`, `linkedin`, vous avez compris le concept
   
La fonction doit renvoyer une erreur si le développeur n'existe pas.<br>
Sinon, elle doit créer un contact, l'affecter au développeur et renvoyer le résultat sauvegardé en db.

 - Créez une fonction `updateContact` qui prend en paramètres :
   - `id` : l'identifiant du développeur à modifier
   - `infos` : l'objet `Contact` avec les nouvelles propriétés

La fonction doit renvoyer une erreur si le développeur n'existe pas.<br>
Sinon elle doit modifier le contact et renvoyer le résultat sauvegardé.

> La fonction doit respecter les mêmes contraintes que la fonction `updateDeveloper`.

 - Créez une fonction `deleteContact` qui prend en paramètre l'`id`: l'identifiant du développeur à modifier.
 
Renvoyez une erreur si le développeur n'existe pas. Sinon, renvoyez le résultat sauvegardé.

> N'oubliez pas de tester vos fonctions.

**Rendu :** `src/entities/Contact.ts` et `src/models/contactModels.ts`.

#### Ressources
- [Les relations dans une base de donnée](https://database.guide/the-3-types-of-relationships-in-database-design/)
- [Les relations dans TypeOrm](https://typeorm.io/#/relations)

## Exercice 05 - Des développeurs compétents

Vous pouvez contacter vos développeurs, mais il serait peut-être appréciable d'avoir un peu plus d'informations sur eux avant ?<br>
Un étendu de leurs compétences par exemple ?

Vous allez mettre en place une relation `One to Many` entre la table `Developer` et la table `Competences`.

Ajoutez un fichier `src/entities/Competence` dans lequel vous allez exporter une classe `Compenence` contenant les champs suivants :
 - `id` : L'identifiant de la table
 - `name` : Nom de la compétence
 - `level` : Le niveau de maîtrise (entre 0 et 10)
 
Le `constructeur` n'est toujours pas en option.

Liez la table `Developer` à votre nouvelle table en `One to Many` et n'oubliez pas d'activer le mode `cascade` (au bon endroit).

> :bulb: La liaison est spéciale, vous devrez sûrement modifier votre classe Competence pour pouvoir la réaliser.<br>

Créez un fichier `competenceModels.ts` dans votre dossier `src/models` dans lequel vous allez écrire les trois fonctions habituelles pour intéragir avec vos tables :
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
Sinon, renvoyer le développeur mis à jour.

> La fonction doit respecter les mêmes contraintes que la fonction `updateDeveloper`.

- `deleteCompetence` qui prend en paramètres :
  - `devId` : Identifiant du développeur
  - `competenceId` : Identifiant de la compétence
  
Renvoyer une erreur si l'un des deux identifient est inconnu, sinon renvoyer le développeur mis à jour.

> N'oubliez pas de modifier les `models` de `Developer` pour ajouter les compétences.

**Rendu :** `src/entities/Compentence`, `src/entities/Developer` et `src/models/competenceModels.ts` 

#### Ressources
 - [One to Many](https://orkhan.gitbook.io/typeorm/docs/many-to-one-one-to-many-relations)
 - [One to Many (seconde source)](https://typeorm.io/#/many-to-one-one-to-many-relations)
 
## Exercice 06 - Des développeurs actifs

Il est temps de passer à l'étape finale : les projets.
L'exercice est volontairement moins guidé, vous avez appris tout le nécessaire sur le fonctionnement de TypeOrm pour vous documenter seul et réaliser l'exercice.

Votre modèle `Project` doit avoir les propriétés suivantes :
  - `id`: Identifiant de le table
  - `name`: Nom du projet
  - `deadline`: La date de rendu du projet
  - `type`: Le type de projet (du type ProjectType que vous trouverez dans le fichier `type.ts` sur le repo)
  - `developers`: Les développeurs sur le projet
  
Vous allez créer une relation `Many to Many` entre les développeurs et les projets.

> Documentez-vous bien sur la manière de faire et les décorateurs à utiliser.

Vous devrez ensuite écrire 6 models :
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

**Rendu :** `src/entities/Project`, `src/models/projectModels.ts` et `src/entities/Developer.ts`.

#### Ressources
 - [Many to Many](https://typeorm.io/#/many-to-many-relations) 

## Bonus

Voici un _petit_ bonus pratique et utile pour consolider vos connaissances :

Vous avez actuellement des modèles et des models, c'est un bon début pour une API avec une architecture MVC n'est-ce pas ?

> La structure MVC, Modèle, Vue, Controlleur est une architecture basique dans le développeur back-end.

L'objectif est de créer un serveur express avec les routes nécessaires pour créer, modifier, afficher vos différentes entitées.<br>
Vous pouvez bien évidemment utiliser les entitées actuellement définis, mais aussi en rajouter.

Basez-vous sur vos acquis pour terminer ce bonus.<br>
Bon courage !

## Ressources complémentaires

Si vous souhaitez en apprendre plus sur les bases de données, voici quelques liens intéressants :
 - [Prisma, l'ORM du futur](https://github.com/prisma/prisma)
 - [Les bases de données graph](https://medium.com/wiidii/pourquoi-sint%C3%A9resser-aux-bases-de-donn%C3%A9es-orient%C3%A9es-graphe-e650f0395951)
 - [Neo4Js](https://www.google.com/search?channel=fs&client=ubuntu&q=neo4j)
 - [DGraph](https://dgraph.io/)
 - [Prisma X Graphql](https://blog.geographer.fr/prisma-graphql-api)
 - [MongoDB](https://www.mongodb.com/fr)
 - [MikroORM](https://github.com/mikro-orm/mikro-orm/issues)
 
> PoC - 2021
