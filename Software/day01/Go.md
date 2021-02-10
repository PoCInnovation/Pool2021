# PoC Software 2021, Go, Day2

# Sommaire

- [0 - Setup](#0---setup)
- [1 - Hello World](#1---hello-world)
- [2 - Abuser des bonnes choses](#2---abuser-des-bonnes-choses)
- [3 - Toujours penser au scaling](#3---toujours-penser-au-scaling)
- [4 - Tester vos routes](#4---tester-vos-routes)
- [5 - Qui utilise du texte brut ?](#5---qui-utilise-du-texte-brut-)
- [6 - Un peu de logique 🤯](#6---un-peu-de-logique-)
- [7 - Les bodyguards des serveurs](#7---les-bodyguards-des-serveurs)

# 0 - Setup

- À la racine du répo d'hier, créez un dossier Day2
- Initialisez un module `SoftwareGoDay2`


# 1 - Hello World

Afin de créer notre web server, nous allons utilisé le framework [Gin](https://github.com/gin-gonic/gin).
Le but de cet exercice est de mettre en place un server qui expose une route `/hello` qui retourne `world`.

- Créer un package `routes` qui va contenir votre Router & vos controllers.
- Créer une route **GET** `/hello` renvoyant `StatusOK` & `world`.

Voici un example de comment organiser vos routes
  ```go
  package router
  
  import (
  	"github.com/gin-gonic/gin"
  )
  
  func world(c *gin.Context) {
  }
  
  func ApplyRoutes(r *gin.Engine) {
     //r.HttpMethod(route, controller)
  }
  ```

- Créer un package `server` avec:
  - Une structure `Server` (qui contient votre app gin).
  - Une fonction `NewServer()` qui va instancier un nouveau server.
- Créer un main pour lancer votre server.

> Une pratique basique lorsque vous lancer un serveur est d'afficher
> un message avec l'addresse du server afin de pouvoir y accéder facilement.
>
> ex: `Server running here: http://localhost:8080/`


### **Ressources**
- [HTTP Status Code](https://golang.org/pkg/net/http/#pkg-constants)
- [Gin QuickStart](https://github.com/gin-gonic/gin#quick-start)


# 2 - Abuser des bonnes choses

En HTTP, les paramètres de votre demande peuvent être exprimés à différents endroits:
`body`, `parameter`, `query`, `cookie` & `header`

- Créez 5 routes qui prendront un message dans l'endroit que traite la route & le renverront:
  - **GET** `/repeat-my-query`
  - **GET** `/repeat-my-param/:message`
  - **POST** `/repeat-my-body`
  - **GET** `/repeat-my-header`
  - **GET** `/repeat-my-cookie`

> Pour chacune des routes, si le message n'est pas présent renvoyez un StatusBadRequest.

### **Ressources**
- [Gin Examples](https://github.com/gin-gonic/gin#api-examples)


# 3 - Toujours penser au scaling

Pour ceux qui ne connaitraient pas, les variables d'environnement sont utilisées par votre système
d'exploitation ainsi que de nombreux framework & app. Elles sont utilisées lorsque vous déployez une application
en production pour sécuriser des mots de passes et identifiants privés.
Il est donc essentiel de savoir comment les utiliser dans votre code.

Pour cela, nous allons utiliser le package [dotenv](https://github.com/joho/godotenv) qui permet de
charger automatiquement des variables d'environnement depuis un fichier.

- `go get github.com/joho/godotenv`
- Créez un fichier `.env` qui définira les variables suivantes:
  - `PORT=8080`
  - `HELLO_MESSAGE=world`
- Adaptez votre code pour chargez l'env au démarrage.

> Il est commun dans une API d'avoir un fichier spécifique à la configuration,
> il permet de garder une architecture propre.

- Adaptez votre route `/hello` pour utiliser `HELLO_MESSAGE`.

> Si la variable est absente renvoyez StatusNotFound & `no message defined`

### **Ressources**
- [dotenv](https://github.com/joho/godotenv)
- [Environnement in go](https://golang.org/pkg/os/#Getenv)

> Si votre `.env` contient des variables privées, il est impératif de ne pas le push sur un repo en temps normal.
> Une bonne pratique est de créer un `example.env` contenant les variables sans leurs valeurs.

> Il est important de penser depuis le début à l'intégration de votre serveur dans une architecture Web
> en plaçant le maximum de variables susceptibles de changer dans l'environnement.


# 4 - Tester vos routes

Les tests sont partout et le web n'y échappe pas. Il est primordial de tester vos routes avant de déployer
en production.

- Créer une collection Postman testant les routes précédentes.
- Créer une route **GET** '/health' qui renvoie tout le temps le statut `200`.

> Elle permet de savoir immédiatement si le server est up.

### **Ressources**
- [Postman Collections](https://learning.postman.com/docs/sending-requests/intro-to-collections/)
- [Postman Test Suites](https://www.postman.com/use-cases/api-testing-automation/)


# 5 - Qui utilise du texte brut ?

Avoir des formats de données communs & génériques est obligatoire pour faciliter l'utilisation d'une API!.
Vous pouvez renvoyer des informations sous diverses formes. La plus commune étant un tableau d'objet (JSON).

- Créez une route **GET** `/repeat-all-my-queries` qui renvoie un tableau sous ce format:

```json
[
  {
    "Key": "...", // nom d'une query
    "Value": ["..."] // valeurs d'une query
  },
  ...
]
```

> Le retour étant un tableau d'objets, créer une `structure` peut s'avérer adapté.

### **Ressources**
- [Marshall](https://golang.org/pkg/encoding/json/#Marshal)

# 6 - Un peu de logique 🤯

Formatter les données c'est bien, travailler avec c'est mieux!

- Créez une route **POST** `/are-these-palindromes`.
  - Elle prend un tableau JSON de string dans le body.
  - Elle renvoie un tableau d'objets de la forme suivante :

```json
[
  {
    "Input": "",
    "Result": true
  },
  ...
]
```


# 7 - Les bodyguards des serveurs

En web, il est important de savoir quel type de donnée sont envoyés à votre API.
Cela vous permet d'avoir un code stable et sécurisé.

Essayer d'envoyer un body vide à la route précédente, vous devriez obtenir une erreur en retour.
Ce genre d'erreur n'est pas acceptable pour une API

Pour assurer la sécurité d'une API, il existe un système que l'on appelle `Middleware`.

> Les Middleware peut également servir à mettre en place un logger, une gestion des permissions ect...

Nous allons utiliser les middlewares intégrés dans gin !

Voici la structure d'un middleware dans [gin](https://github.com/gin-gonic/gin#custom-middleware) :

```go
func Logger() gin.HandlerFunc {
    return func(c *gin.Context) {
        // before request
        t := time.Now()

		// Set example variable
		c.Set("example", "12345")


		c.Next() // Fonction suivante à executer dans la route

		// after request
		latency := time.Since(t)
		log.Print(latency)

		// access the status we are sending
		status := c.Writer.Status()
		log.Println(status)
	}
}
```

## Écrire le middleware

- Dans un package `middlewares`, créez `CheckPalindrome`
> Si le body est invalide, renvoyer un StatusBadRequest et la raison du refus.

- Ajoutez à la route `/are-these-palindrome`.

### **Ressources**
- [gin Middlewares](https://github.com/gin-gonic/gin#custom-middleware)
