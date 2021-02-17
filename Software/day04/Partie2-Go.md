# Piscine Software - Jour 4 - Partie 2

✔ Authentifier vos utilisateurs.

✔ Maîtriser différentes méthodes d'auth.

✔ Connexion avec Google.

# Sommaire

- [0 - Setup](#0---setup)
- [1 - Sessions](#1---sessions)
  - [1. Présentation](#1-présentation)
  - [2. Le concret](#2-le-concret)
- [2 - JWT, ou JSON Web Token](#2---jwt-ou-json-web-token)
  - [1. Présentation](#1-présentation)
  - [2. Le concret](#2-le-concret)
- [3 - OAuth2 et Google](#3---oauth2-et-google)
  - [1. Présentation](#1-présentation)
  - [2. Le concret](#2-le-concret)
- [Bonus](#bonus)


# 0 - Setup

Pour ce jour-ci, nous allons retourner sur nos serveurs Gin ! Vous pouvez repartir du code de votre jour 2 si vous souhaitez, ou initialiser un nouveau server vide, à vous de voir, vous connaissez les commandes.

- À la racine du répo, créez un dossier `Day4`
- Initialisez un module `SoftwareGoDay4`


# 1 - Sessions

## 1. Présentation

Une session est une manière assez simple de gérer l'authentification de vos utilisateurs. Vous allez stocker du coté du server les informations des utilisateurs qui sont connectés. Le server s'occupe d'envoyer un cookie au client qui permettra d'identifier toutes ses requêtes. Si les informations du cookie coincident avec ce qui est stocké dans la session, alors l'utilisateur est bien connecté

## 2. Le concret

Pour mettre tout ça en place, vous devez :

- Ajouter un package pour gérer les sessions avec gin: `go get -u github.com/gin-contrib/sessions`
- Créez une structure `User` qui nous servira de base de donnée simplifiée, stockée en ram

```go
type User struct {
  Email     string
  Password  string
}

var Users := User[]{}
```

- Créez une route **POST** `/signup-session`
  - Prend un `body` contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans la variable `users`
  - Renvoie un `cookie` contenant le body signé reçu
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **POST** `/singin-session`
  - Prend un `body` contenant l'`email` et le `password` de l'utilisateur
  - Si les les identifiants matchent, renvoie un `cookie` contenant le body signé reçu
  - Si aucun message n'est donné ou que les identifiants ne matchent pas
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **GET** `/me-session`
  - Si le header contient un `cookie`
    - Renvoie les informations de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun `cookie` n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

> :warning: N'oubliez pas les `StatusCode` du package `http`


# 2 - JWT, ou JSON Web Token

## 1. Présentation

Les JSON Web Token, d'après wikipedia *permettent l'échange sécurisé de jetons entre plusieurs parties. Cette sécurité de l’échange se traduit par la vérification de l’intégrité des données à l’aide d’une signature numérique. Elle s’effectue par l'algorithme HMAC ou RSA*.

Pour l'expliquer simplement, ces tokens vous permettrons d'identifier vos utilisateurs, qui les stockerons dans un cookies, ou dans le local storage. leur structure en 3 partie garantis que l'information qui transite entre l'utilisateur et le server n'a pas été modifiée. Pour plus d'explications sur leur fonctionnement et leur intérét, rendez vous sur [jwt.io](https://jwt.io/introduction/). Vous pourrez également utiliser un [débuggeur pour visualiser](https://jwt.io/#debugger-io) les différentes parties qui composent un jwt

Le flow sera le suivant:
- vous envoyez à votre api vos identifiants (email, password, etc.)
- votre api va signer ces identifiants avec un code secret
- votre api renvoie un token contenant ces informations
- votre client mettra ce token dans le header de toutes ses requêtes afin de l'identifier

## 2. Le concret

Passons à présent au concret! Créons un flow d'authentification basé sur les JWT, pour cela:

- Ajoutez un package pour générer les JWT: `go get -u github.com/dgrijalva/jwt-go`
- Créez une structure `UserJWT` qui nous servira de base de donnée simplifiée, stockée en ram

```go
type UserJWT struct {
  Email     string
  Password  string
}

var UsersJWT := UserJWT[]{}
```

- Créez une route **POST** `/signup-jwt`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans l'objet `userJWT`
  - Renvoie un token contenant le body signé reçu
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une fonction qui reçoit un token et compare dans la base de donnée si les mots de passe matchent, en renvoyant un bool

- Créez une route **POST** `/singin-jwt`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Si les identifiants matchent, renvoie un token contenant le body signé reçu
  - Si aucun message n'est donné ou que les identifiants ne matchent pas
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **GET** `/me-jwt`
  - Si le header contient un token
    - Renvoie les informations de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun token n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`


# 3 - OAuth2 et Google

## 1. Présentation

OAuth 2.0 est un framework d’autorisation permettant à une application tierce d’accéder à un service web. Vous l'avez obligatoirement déjà vu grace aux fameux boutons "Se connecter avec Google", "se connecter avec Facebook", etc. Concretement, vous allez utiliser des sites externes pour identifier vos utilisateurs.

Le fonctionnement est assez simple :
- Vous créez une application OAuth sur le site que vous souhaitez utiliser (google, facebook, twitter, github, microsoft, etc.)
- vous définissez une URL de redirection qui vous ramène vers votre site une fois les étapes de connexion faites
- Depuis votre server, vous récupérez dans cette url de redirection les identifiants

Ces identifiants sont liés à l'application : un id qui représente votre compte Facebook ne sera pas le même sur votre app et sur celle de votre voisin.

## 2. Le concret

Nous allons passer par google pour cet exercice et nous nous aiderons de passport pour simplifier les démarches:

- Créez une application avec google sur la [console développeurs](https://console.developers.google.com/)
  - vous aurez besoin de bien paramétrer le callback url que vous ferez dans les étapes suivantes

- Ajoutez oauth2 aux dépendances: `go get -u golang.org/x/oauth2`
- Créez un objet `userOAuth` qui nous servira de base de donnée simplifiée, stockée en ram

```go
type UserOAuth struct {
  DisplayName   string
  GoogleId      string
}

var UsersOAuth := UserOAuth[]{}
```

- Mettez en place la `GoogleStrategy` de passport à l'aide de l'id de votre application, son code secret et la callback URL, ainsi que la fonction qui sera appelée une fois que google redirgera l'utilisateur sur votre api

- Créez les différents routes qui vous permettront d'utiliser la stratégie fraichement créée

- Une fois que vous avez récupéré l'id de l'utilisateur connecté, sauvegardez le dans la db et renvoyez un JWT comme dans l'exercice 2 contenant cet id

- Créez une route **GET** `/me-oauth`
  - Si le header contient un token
    - Renvoie le `displayName` de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun token n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

**ATTENTION**: si l'id de l'utilisateur existe déjà en db, vous devez obligatoirement renvoyer ses informations plutôt que créer un nouvel utilisateur avec le même id à chaque fois


> Pour plus d'infos sur le fonctionnement de oauth2 avec google, [voilà comment l'utiliser](https://pkg.go.dev/golang.org/x/oauth2/google)

# Bonus

Maintenant que vous maitrisez plusieurs méthodes pour authentifier vos utilisateurs, vous pouvez:
- Combiner deux méthodes d'authentification, par exemple pouvoir se connecter au même compte via Google ou aussi avec un email et mot de passe
- Implémenter l'authentification avec d'autres sites comme facebook ou github, ce qui se fait assez simplement grâce à passport
- Utiliser une véritable base de donnée, comme vu hier, pour stocker vos utilisateurs
