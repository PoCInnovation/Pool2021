# Piscine Software - Jour 4 - Partie 2

✔ Authentifier vos utilisateurs.

✔ Maîtriser différentes methodes d'auth.

✔ Connexion avec Google.

## Exercice 00 - Setup

Pour ce jour-ci, nous allons retourner sur nos serveurs Express ! Vous pouvez repartir du code de votre jour 2 si vous souhaitez, ou initialiser un nouveau server vide, à vous de voir, vous connaissez les commandes.

## Exercice 01 - Les Sessions

### Présentation

Une session est une manière assez simple de gérer l'authentification de vos utilisateurs. Vous allez stocker du coté du server les informations des utilisateurs qui sont connectés. Le server s'occupe d'envoyer un cookie au client qui permettra d'identifier toutes ses requêtes. Si les informations du cookie coincident avec ce qui est stoqué dans la session, alors l'utilisateur est bien connecté

### Le concret

Pour mettre tout ça en place, vous devez:

- Ajouter un package pour gérer les sessions avec express:
```
npm i express-session @types/express-session
```

- Créez un objet `user` qui nous servira de base de donnée simplifiée, stockée en ram
```ts
interface User {
  email: string;
  password: string;
}

let user: User[] = []
```

- Créez une route **POST** `/signin-session`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans l'objet `user`
  - Renvoie un cookie contenant le body signé reçu
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **POST** `/singup-session`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Si les les identifiants matchent, renvoie un cookie contenant le body signé reçu
  - Si aucun message n'est donné ou que les identifiants ne matchent pas
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une route **GET** `/me-session`
  - Si le header contient un cookie
    - Renvoie les informations de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun cookie n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

## Exercice 02 - Les JWT, ou JSON Web Token

### Présentation

Les JSON Web Token, d'après wikipedia *permetent l'échange sécurisé de jetons entre plusieurs parties. Cette sécurité de l’échange se traduit par la vérification de l’intégrité des données à l’aide d’une signature numérique. Elle s’effectue par l'algorithme HMAC ou RSA*.

Pour l'expliquer simplement, ces tokens vous permettrons d'identifier vos utilisateurs, qui les stockerons dans un cookies, ou dans le local storage. leur structure en 3 partie garantis que l'information qui transite entre l'utilisateur et le server n'a pas été modifiée. Pour plus d'explications sur leur fonctionnement et leur intérét, rendez vous sur [jwt.io](https://jwt.io/introduction/). Vous pourrez également utiliser un [débuggeur pour visualiser](https://jwt.io/#debugger-io) les différentes parties qui composent un jwt

Le flow sera le suivant:
- vous envoyez à votre api vos identifiants (email, password etc.)
- votre api va signer ces identifiants avec un code secret
- votre api renvoie un token contenant ces informations
- votre client mettra ce token dans le header de toutes ses requêtes afin de l'identifier

### Le concret

Passons à présent au concret ! Créons un flow d'authentification basé sur les JWT, pour cela:

- Ajoutez un package pour générer les JWT:
```
npm i jsonwebtoken
```

- Créez un objet `userJWT` qui nous servira de base de donnée simplifiée, stockée en ram
```ts
interface UserJWT {
  email: string;
  password: string;
}

let userJWT: UserJWT[] = []
```

- Créez une route **POST** `/signin-jwt`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Enregistre l'utilisateur dans l'objet `userJWT`
  - Renvoie un token contenant le body signé reçu
  - Si aucun message n'est donné
    - Définir le statut 400
    - Renvoyer `Bad Request`

- Créez une fonction qui recoit un token et comapre dans la base de donnée si les mots de passe matchent, en renvoyant un bool

- Créez une route **POST** `/singup-jwt`
  - Prend un body contenant l'`email` et le `password` de l'utilisateur
  - Si les les identifiants matchent, renvoie un token contenant le body signé reçu
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

## Exercice 03 - Oauth 2 et Google

### Présentation

OAuth 2.0 est un framework d’autorisation permettant à une application tierce d’accéder à un service web. Vous l'avez obligatoirement déjà vu grace aux fameux boutons "Se connecter avec Google", "se connecter avec Facebook", etc. Concretement, vous allez utiliser des sites externes pour identifier vos utilisateurs.

Le fonctionnement est assez simple:
- Vous créez une application OAuth sur le site que vous souhaitez utiliser (google, facebook, twitter, github, microsoft etc.)
- vous definissez une URL de redirection qui vous ramène vers votre site une fois les étapes de connexion faites
- Depuis votre server, vous récuperez dans cette url de redicrection les identifiants

Ces identifiants sont liés à l'application: un id qui represente votre compte Facebook ne sera pas le même sur votre app et sur celle de votre voisin.

### Le concret

Nous allons passer par google pour cet exercice et nous nous aiderons de passport pour simplifier les démarches:

- Créez une application avec google sur la [console developpeurs](https://console.developers.google.com/)
  - vous aurez besoin de bien parametrer la callback url que vous ferez dans les étapes suivantes

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

- Mettez en place la `GoogleStrategy` de passport à l'aide de l'id de votre application, son code secret et la callback URL, ainsi que la fonction qui sera appellée une fois que google redirgera l'utilisateur sur votre api

- Créez les différents routes qui vous permettrons d'utiliser la statégie fraichement créee

- Une fois que vous avez récupéré l'id de l'utilisateur connecté, sauvegardez le dans la db et renvoyez un JWT comme dans l'exercice 2 contenant cet id

- Créez une route **GET** `/me-oauth`
  - Si le header contient un token
    - Renvoie le `displayName` de l'utilisateur authentifié s'il existe en db
    - Renvoie le status 401 et le message `Unauthorized` dans le cas contraire
  - Si aucun token n'est donné
    - Définir le statut 403
    - Renvoyer `Forbidden`

**ATTENTION**: si l'id de l'utilisateur existe déjà en db, vous devez obligatoirement renvoyer ses informations plutot que créer un nouvel utilisateur avec le même id à chaque fois


> Pour plus d'infos sur le fonctionnement de passport avec google, [voilà comment l'utiliser](http://www.passportjs.org/packages/passport-google-oauth20/)

## Bonus

Maintenant que vous maitrisez plusieurs methodes pour authentifier vos utilisateurs, vous pouvez:
- Combiner deux methodes d'autentification, par exemple pouvoir se connecter au même compte via Google ou aussi avec un email et mot de passe
- Implémenter l'authentification avec d'autres sites comme facebook ou github, ce qui se fait assez simplement grâce à passport
- Utiliser une véritable base de donnée, comme vu hier, pour stocker vos utilisateurs