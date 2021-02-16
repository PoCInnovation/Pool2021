# Piscine Software - Jour 4 - Partie 2

✔ Authentifier vos utilisateurs.

✔ Maîtriser différentes méthodes d'auth.

✔ Connexion avec Google.

## Exercice 00 - Setup

Pour cette demi-journée, nous allons retourner sur nos serveurs Express ! Vous pouvez repartir du code de votre jour 2 si vous souhaitez, ou initialiser un nouveau server vide, à vous de voir, vous connaissez la procédure.

Nous allons aujourd'hui voir comment identifier vos utilisateurs sur vos serveurs de manière simplifiée. Les exercices sont là pour vous faire comprendre les bases de l'authentification mais ne reflètent pas les standars de sécurité.

Nous vous recommandons une nouvelle fois de passer par **Postman** pour tester vos routes, surtout pour les 3 premiers exercices

## Exercice 01 - Les Cookies

### Présentation

Les cookies sont une manière de stocker des information au niveau de votre navigateur. Ces informations peuvent être par la suite utilisée pour identifier votre navigateur auprès du seveur. Il s'agit souvent d'id chiffrés et/ou signés que le serveur va vérifier afin de déterminer quel utilisateur lui fait une requête. Ces informations authentification sont envoyées dans le header de vos requêtes.

### Le concret

Pour mettre tout ça en place, vous devez:

- Ajouter un package pour gérer les cookies avec express:
```
npm i cookie-parser @types/cookie-parser
```

- Créez un objet `user` qui nous servira de base de donnée simplifiée, stockée en ram
```ts
interface User {
  email: string;
  password: string;
}

let users: User[] = []
```

- Créez une route **POST** `/cookies/register`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans l'objet `users`
  - Renvoie un cookie *httpOnly* contenant l'email reçu *signé*
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **POST** `/cookies/login`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Si les les identifiants matchent avec ceux contenus dans `users`, renvoie un cookie *httpOnly* contenant l'email reçu *signé*
  - Si aucun message n'est donné ou que les identifiants ne matchent pas
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **GET** `/cookies/me`
  - Si le header contient un cookie
    - Renvoie les informations de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun cookie n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

> les cookies signés se trouvent dans le champ `signedCookies` de la requête

#### Ressources :
- [Envoyer des cookies avec Express](https://expressjs.com/fr/api.html#res.cookie)

## Exercice 02 - Les JWT, ou JSON Web Token

### Présentation

Les JSON Web Token, d'après wikipedia *permettent l'échange sécurisé de jetons entre plusieurs parties. Cette sécurité de l’échange se traduit par la vérification de l’intégrité des données à l’aide d’une signature numérique. Elle s’effectue par l'algorithme HMAC ou RSA*.

Pour l'expliquer simplement, ces tokens vous permettront d'identifier vos utilisateurs, qui les stockerons dans un cookies, ou dans le local storage. Leur structure en 3 parties garantit que l'information qui transite entre l'utilisateur et le server n'a pas été modifiée. Pour plus d'explications sur leur fonctionnement et leur intérêt, rendez vous sur [jwt.io](https://jwt.io/introduction/). Vous pourrez également utiliser un [débuggeur pour visualiser](https://jwt.io/#debugger-io) les différentes parties qui composent un jwt.

Le flow sera le suivant:
- vous envoyez à votre api vos identifiants (email, password etc.)
- votre api va signer ces identifiants avec un code secret
- votre api renvoie un token contenant ces informations
- votre client mettra ce token dans le header de toutes ses requêtes afin de l'identifier

### Le concret

Passons à présent au concret ! Créons un flow d'authentification basé sur les JWT, pour cela:

- Ré-utilisez l'objet user de l'exercice précédent
- Ajoutez un package pour générer les JWT:
```
npm i jsonwebtoken @types/jsonwebtoken
```

- Créez une route **POST** `/jwt/register`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans l'objet `users`
  - Renvoie un token contenant l'email reçu *signé*
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **POST** `/jwt/login`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Si les les identifiants matchent, renvoie un token contenant l'email reçu *signé*
  - Si aucun message n'est donné ou que les identifiants ne matchent pas
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **GET** `/jwt/me`
  - Si le header contient un token
    - Renvoie les informations de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun token n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

> les JWT doivent se mettre dans le champ `authorization` des header sous la forme `Bearer VOTRE_JWT`

#### Ressources :
- [Le site de référence pour les JSON Web Token](https://jwt.io/introduction/)
- [Décoder de JWT en ligne](https://jwt.io/#debugger-io)

## Exercice 03 - Hash de mots de passe

Sauvegarder des utilisateurs, c'est bien, mais si vous voulez qu'ils vous fassent confiance, vous ne devez pas laisser leurs données sensibles lisibles. Nous allons donc *hash* leur mot de passe afin que même nous, nous ne puissions pas le lire.

Pour cela, nous allons utiliser la librairie de hash [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt). Il existe des implémentation dans de nombreux langages, notamment JS/TS

```bash
npm i bcrypt @types/bcrypt
```

Mettez à jour vos routes afin de hash le mot de passe lors de la création d'un utilisateur, puis utilisez les fonctions de bcrypt pour comparer le mot de passe reçu lors du login et voir s'ils matchent bien.

#### Ressources :
- [Page wikipedia de Bcrypt](https://en.wikipedia.org/wiki/Bcrypt)

## Exercice 04 - Oauth 2 et Google

### Présentation

OAuth 2.0 est un framework d’autorisation permettant à une application tierce d’accéder à un service web. Vous l'avez obligatoirement déjà vu grâce aux fameux boutons "Se connecter avec Google", "se connecter avec Facebook", etc. Concrètement, vous allez utiliser des sites/services externes pour identifier vos utilisateurs.

Le fonctionnement complexe mais vous vous y habituerez:
- Vous créez une application OAuth sur le site que vous souhaitez utiliser (google, facebook, twitter, github, microsoft etc.)
- vous définissez une URL de redirection qui vous ramène vers votre site une fois les étapes de connexion faites
- Depuis votre server, vous récupérez dans cette url de redirection un token
- Ce tokens vous permettront par la suite de récupérer les informations de l'utilisateur (id, email, nom et prénom... la quantité d'information désirées est paramétrable)

Ces informations sont liés à l'application: un id qui représente votre compte Google ne sera pas le même sur votre app et sur celle de votre voisin.

### Le concret

Nous allons passer par google pour cet exercice et nous nous aiderons de [passport](https://github.com/jaredhanson/passport) pour simplifier les démarches:

- Créez une application avec google sur la [console developpeurs](https://console.developers.google.com/)
    - vous aurez besoin de bien paramétrer la callback url que vous ferez dans les étapes suivantes

- Ajoutez passport aux dépendances:
```
npm i passport passport-google-oauth20 @types/passport @types/passport-google-oauth20
```

- Créez un objet `userOAuth` qui nous servira de base de donnée simplifiée, stockée en ram
```ts
interface UserOAuth {
  displayName: string;
  googleId: string;
}

let userOAuth: UserOAuth[] = []
```

- Mettez en place la `GoogleStrategy` de passport à l'aide de l'id de votre application, son code secret et la callback URL, ainsi que la fonction qui sera appelée une fois que google redirigera l'utilisateur sur votre api.

- Vous aurez besoin de créer 2 routes (référez vous au lien de documentation indiqué un peu plus bas).
  - Une route qui va vous rediriger vers le service d'oauth de google
  - Une route sur laquelle google va vous rediriger une fois l'authentification validée (il s'agit de la *callback url*). Les informations renvoyées par google seront accessibles dans cette route grâce à passport.
  - Une fois que vous avez récupéré l'id de l'utilisateur connecté, sauvegardez le dans la db et renvoyez soit un JWT, soit un cookie, comme vous préférez, contenant cet id

- Créez une route **GET** `/oauth/me`
  - Si le header contient un token/cookie
    - Renvoie le `displayName` de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun token/cookie n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

**ATTENTION**: si l'id de l'utilisateur existe déjà en db, vous devez obligatoirement renvoyer ses informations plutôt que de créer un nouvel utilisateur avec le même id à chaque fois


> Pour plus d'infos sur le fonctionnement de passport avec google, [voilà comment l'utiliser](http://www.passportjs.org/packages/passport-google-oauth20/)

#### Ressources :
- [Passport](https://github.com/jaredhanson/passport)
- [Créer une application Oauth2 Google](https://console.developers.google.com)
- [Utiliser Passport avec Google](http://www.passportjs.org/packages/passport-google-oauth20)

## Bonus

Maintenant que vous maîtrisez plusieurs méthodes pour authentifier vos utilisateurs, vous pouvez:
- Combiner deux méthodes d'authentification, par exemple pouvoir se connecter au même compte via Google ou aussi avec un email et mot de passe
- Implémenter l'authentification avec d'autres sites comme facebook ou github, ce qui se fait assez simplement grâce à passport
- Utiliser une véritable base de donnée, comme vu hier, pour stocker vos utilisateurs

> PoC - 2021
