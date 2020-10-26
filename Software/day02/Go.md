## Exercice 00 - Setup

Comme hier, vous allez créer un nouveau dossier pour les exercices du jour, intitulé `d02` (dans le même repo qu'hier).

Vous devriez déjà avoir VSCode ou Goland d'installé, il ne vous reste donc plus qu'à initialiser un nouveau module avec `go mod init` cf les exercices 2 et 3 du d01.

## Exercice 01 - Le Hello World du serveur web

Pour créer un server web en Go, vous allez avoir besoin du package `gin`.

```sh
go get -u github.com/gin-gonic/gin
```

Le but de cet exercice est de mettre en place un server qui expose une route `/hello` qui retourne `world` par la méthode **GET**.

- Créer une variable `server` qui vas instancier votre server.
- Lancer le serveur en écoutant sur le port `8080`.
- Définir une route **GET** `/hello` qui renvoie `ẁorld`

> Une pratique basique lorsque vous lancer un serveur est d'afficher un message avec l'adresse du server afin de pouvoir y accéder facilement.

**Rendu :** `src/server.go`

## Exercice 02 - Abuser des bonnes choses

En HTTP, les paramètres de votre demande peuvent être exprimés à différents endroits :

- `body`
- `parameter`
- `query`
- `cookie`
- `header`

Votre app mux devra par la suite utiliser (`use()`) sur ces 2 parsers pour les appliquer.
  
À présent, il ne vous reste plus qu'à créer ces différentes routes :

- Créer une route **GET** `/repeat-my-query`
  - Prend un paramètre query `message`
  - Renvoie le message donné en paramètre
  - Si aucun message est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créer une route **GET** `/repeat-my-param/:message`
  - Prend un paramètre `message`
  - Renvoie le message donné en paramètre

- Créer une route **POST** `/repeat-my-body`
  - Renvoie le `messsage` donné dans le corps de la requête
  - Si le corps est vide
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créer une route **GET** `/repeat-my-header`
  - Cherche un header `X-Message`
  - Renvoie le message écris dans celui-ci
  - Si aucun message est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créer une route **GET** `/repeat-my-cookie`
  - Cherche un cookie `message`
  - Renvoie le message donné en cookie
  - Si aucun message est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

**Rendu :** `src/server.go`.

## Exercice 03 - Toujours penser au scaling

Pour ceux qui ne connaitraient pas, les variables d'environnement sont des variables utilisées par votre système d'exploitation dans de nombreux domaines. Elles sont visibles en tapant `env` dans votre terminal.
Ces variables sont utilisées lors que vous déployez une application en production pour sécuriser des mots de passes et identifiants privés.
Il est donc essentiel de savoir comment les utiliser dans votre code.

Pour cela, nous allons utiliser le package `dotenv` qui permet de charger automatiquement des variables d'environnement depuis un fichier :

```sh
go get github.com/joho/godotenv
```

Par la suite, créez un fichier `.env` qui définira les variables d'environnement suivantes :
  - SERVER_PORT=8080
  - HELLO_MESSAGE=world

Dans le fichier `src/serverConfig.go`, récupérer les deux variables d'environnement et exporter les.

> Il est commun dans une API d'avoir un fichier spécifique à la configuration, il vous permet de garder une architecture propre.

Adaptez le code du serveur express pour utiliser le port défini dans l'environnement de préférence, et si non défini, utilisez le port `8080`.

Enfin, adaptez le code de la route **GET** '/hello' pour utiliser la variable `HELLO_MESSAGE` comme réponse.
  - Si la variable n'est pas présente :
      - Définir le statut 404
      - Renvoyer `No Message Defined`

Si votre `.env` contient des variables privées, il est impératif de ne pas le push sur un repo en temps normal.
La bonne pratique est de créer un fichier `env.example` contenant les différentes variables mais sans leurs valeurs, afin d'indiquer ce qui sera par la suite nécessaire, puis de le remplir et de le renommer en `.env`.

> Il est important de penser depuis le début de l'application à l'intégration de votre serveur dans une architecture Web en plaçant le maximum de variables susceptibles de changer dans l'environnement.

**Rendu :** `src/serverConfig.go` et `src/server.go`.

## Exercice 04 - Les statuts HTTP

Une API REST renvoie de la donnée en fonction de ce qu'un client demande, mais si jamais ce dernier tentait d'accéder à des données qui ne lui appartienne pas, ou qui n'existent pas, notre api ne pourra pas lui envoyer ce qu'il demande.  

Un code HTTP permet de déterminer le résultat d'une requête ou d'indiquer une erreur au client. Ces codes sont essentiels au bon fonctionnement des services communiquant en HTTP. Il est donc tout autant essentiel de bien coder son serveur pour renvoyer les codes adaptés à la situation.

Créer une route **GET** '/health' qui renvoie tout le temps le statut `200`.  

Si jamais lors de vos tests cette route ne fonctionne plus, c'est que votre server n'est pas lancé ou ne fonctionne pas.

Il est commun d'utiliser les constantes des codes HTTP fournies par le module http pour expliciter vos status dans votre code.

Remplacez vos status-code écrits en dur dans votre code par l'enum du package.

**Rendu :** `src/server.go`.

## Exercice 05 - Tester vos routes

Quand on crée des routes, on a envie de pouvoir tester simplement si elles fonctionnent, et si leur implémentation n'a pas cassé les autres routes.
C'est dans ce cas de figure que Postman peut s'avérer très utile.

Vous allez donc créer une collection Postman contenant des tests sur toutes les routes précédemment codées.

> Nous vous recommandons de mettre à jour cette collection pour toutes les routes des exercices suivants.

