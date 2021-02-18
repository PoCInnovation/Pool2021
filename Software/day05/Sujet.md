# Piscine Software - Frontend avec React

✔ Utiliser un framework de développement front moderne.

✔ Comprendre les concepts du web front-end.

✔ Découvrir l'UX et l'UI.

## Exercice 00 - Setup

L'objectif de cette journée est de créer une application de message avec un système de salon en [React](https://fr.reactjs.org/).

Vous allez d'abord initialiser votre WebApp React avec les commandes suivantes :

```sh
# Créer un projet react
npx create-react-app my-app --template typescript

# Avance dans le nouveau projet
cd my-app

# Lance la WebApp
npm start
```

Si votre navigateur lance une page web avec le logo React, tout est parfait.

Vous allez maintenant retirer toutes les parties inutiles de l'application.

Supprimez tous les fichiers dans `src` sauf `index.css` et `index.tsx`. Supprimez tout le contenu de `index.css` et changez le contenu de `index.tsx` par:

```tsx
import React from "Software/day05/Subject";
import ReactDOM from "react-dom";
import "./index.css";

ReactDOM.render(
  <React.StrictMode></React.StrictMode>,
  document.getElementById("root")
);
```

Créez un nouveau dossier appelé `components` dans votre dossier `src`. C'est là où vous allez regrouper tous vos composants.

> Nous allons uniquement faire des [functional components](https://www.robinwieruch.de/react-function-component).

#### Ressources

- [Les components](https://fr.reactjs.org/docs/components-and-props.html)
- [Créer une WebApp React en Typescript](https://create-react-app.dev/docs/adding-typescript/)

## Exercice 01 - Les messages

Vous allez maintenant créer votre premier composant, il s'agira du composant `Message`, il représentera un simple message.

Tout d'abord, créez un nouveau dossier `message` dans lequel vous allez faire un fichier `index.tsx` où vous définirez votre composant et fichier `index.css` qui se chargera de le styliser.

> :bulb: Le `x` de `.tsx` permet d'identifier les fichiers qui sont spécialement des composants react.

Dans le fichier `index.tsx`, créer un composant fonctionnel appelé `Message` avec les propriétés suivantes :

- `imgProfileUrl` : L'URL de l'image, elle servira à afficher la photo de profil de la personne ayant envoyé un message.
- `messageId`: L'Id du message, celui-ci ne sera pas utilisé ici
- `senderName` : Le nom de la personne qui a envoyé le message.
- `messageText` : Le contenu du message.

> :bulb: Il est commun de définir une interface regroupant l'ensemble de vos propriétés à envoyer.

Créez votre composant et testez-le en l'important dans `src/index.tsx` (attention, c'est uniquement pour tester et voir que tout marche !), voici un exemple de comment le tester dans `src/index.tsx`:

```tsx
import Message from "./components/message";

ReactDOM.render(
  <React.StrictMode>
    <Message
      messageId={1}
      imgProfileUrl="https://i.ibb.co/Npv3bk7/image-2021-02-18-164910.png"
      senderName="Pepe"
      messageText="Life sucks, is banana a bread, gonna kill a ship later"
    />
  </React.StrictMode>,
  document.getElementById("root")
);
```

Pour créer ce composant, récupérez vos `props` et retournez vos valeurs entre des balises. Pour le moment affichez simplement les differents éléments les uns après les autres.

Vous pouvez maintenant afficher votre composant sur la WebApp. Vous devriez voir le contenu du message, son expéditeur et sa photo de profil.

Néanmoins votre composant doit maintenant être stylisé grâce au css. Rendez le design avec un bel arrière-plan, une photo de profil arrondie, une jolie police d'écriture, vous pouvez vous inspirer de Discord par exemple :).

Pour ajouter du CSS, codez dans votre fichier `src/message/index.css` et regardez comment l'importer dans votre fichier `src/message/index.tsx` en vous inspirant de `src.index.tsx`

> Le mode d'affichage `flex` peut être très utile pour organiser proprement vos composants.

Une fois que vous serez satisfait du design de votre composant, passez à l'exercice suivant.

#### Ressources

- [Jolie CSS](https://www.alticreation.com/blog/8-regles-organiser-code-css/)
- [Flex](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

## Exercice 02 - Les salons

Il est temps de créer un nouveau composant : la `ChatRoom`. L'architecture reste la même que sur le composant `Message`.

L'objectif est d'afficher les messages spécifiques à un salon.

La `ChatRoom` n'a pas besoin de props.

Pour le moment, ce composant ne va pas faire grand-chose, il vous sera très utile sur les futurs exercices !

Vous pouvez néanmoins prendre de l'avance et préparer votre composant. Par exemple, écrivez quelques faux messages et essayer de les afficher proprement dans le salon. Ajoutez du css pour faire un fond, mettre des espaces entre les messages, ect.

#### Ressources

- [L'intérêt des mocks](https://www.fierdecoder.fr/2015/11/mock-ou-pas-mock/)

## Exercice 03 - La connection à l'API

Vous allez maintenant communiquer avec une [API](./resources) afin de récupérer différents messages. Pour cela, utilisez-le package `axios`.

> :bulb: L'API se trouve dans le dossier ressources, lisez la [documentation](./resources/README.md) pour apprendre à l'utiliser.
>
> N'hésitez pas à tester l'API avec Postman afin de comprendre son comportement. 

**Attention ! Quand vous envoyer une requête à l'API, assurez-vous d'avoir bien mis en host `127.0.0.1` dans l'url de votre requête, si vous passez par `localhost`, votre navigateur ne pourra pas set les cookies.**

Créez un nouveau composant appelé `Home` vide. Il va permettre à l'utilisateur de se connecter puis créer / rejoindre des salons. Créer aussi un composant `Login` vide pour permettre aussi à l'utilisateur de se connecter.

### L'arborescence

Une webApp peut parfois être dites `monopage` lorsqu'elle n'a qu'une seule page, cependant, il vous faudra plusieurs pages pour séparer les différentes parties.

Installer le package `react-router-dom` pour gérer votre arborescence.

Insérez le système de root dans le fichier `src/index.tsx`.
le root `/` doit nous afficher simplement le composant `Login`, voici un exemple de comment vous pourriez le mettre en place:

```tsx
<BrowserRouter>
  <Switch>
    <Route exact path="/">
      <Login />
    </Route>
  </Switch>
</BrowserRouter>
```

Pensé à aussi rajouter un chemin vers le component `Home` !

### La connection

Il faut maintenant setup le système de connection dans votre `Login`.

Créez un `form` de connection prenant un nom de compte et un mot de passe, ils devront être envoyés à l'API afin de connecter votre utilisateur.

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

Si l'API renvoie une erreur, il faudra demander à l'utilisateur de réessayer en effaçant ces précédentes entrées, dans le cas d'un succès il faudra rediriger l'utilisateur vers le chemin affichant le composant `Home`. (utilisez history et history.push de `react-router-dom`)

Aussi, créez un bouton qui permettrait la création de nouveau compte. Il faudrait pouvoir facilement passer du mode connection au mode création de compte (et vis-versa) avec de plus un indicateur visuel pour savoir dans quel mode on est.

Il faudra faire en sorte que quand on passe d'un mode à un autre, le `form` ne change pas, seule la fonction appelée change pour interagir avec l'API. (Il faudra néanmoins rajouter une case au form pour saisir l'url de la photo de profil)

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

Pensez à toujours vérifier la réussite ou non de la connection avec l'API, dans le cas de la création de compte, un message d'erreur pourrait être apprécié.

### Le home

Une fois connecté et après avoir été redirigé vers le chemin pour le composant `Home`, il faut proposer à l'utilisateur soit de rejoindre un salon, soit d'en créer un nouveau.

Vous allez donc créer deux éléments :

- `joinRoom`
- `createRoom`

`joinRoom` est un `form` prenant l'ID du salon que l'utilisateur voudra rejoindre, une fois le `form` rempli, une requête sur l'API à la route `<host>/api/room/join` devra être faites afin de savoir si ce salon existe.

Si l'API renvoie une erreur, il faudra l'afficher, dans le cas où celle-ci existe bien, il faudra renvoyer l'utilisateur sur un nouveau chemin qu'il faudra créer : `/chatRoom/${roomId}`, un chemin contenant le composant `ChatRoom`.
Il faudra ensuite récupérer `roomId` dans le composant `ChatRoom`. (Regardez `useParams`)

`createRoom` est semblable à `joinRoom`, à l'exception que ce n'est pas un `form`, ce sera simplement un bouton qui feras un appel à l'API pour créer une room.

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

Celui-ci renverra l'ID d'un nouveau salon, il faudra rediriger l'utilisateur sur ce salon.

#### Ressources

- [Gérer plusieurs pages grâce au React](https://reactrouter.com/web/guides/quick-start)
- [Les hooks en React](https://fr.reactjs.org/docs/hooks-effect.html)

## Exercice 04 - Récupérer les messages

Nous pouvons maintenant retourner à notre `ChatRoom` !

Maintenant que vous savez intéragir avec le backend et que vous avez un identifiant de salon, vous pouvez facilement récupérer la liste des messages envoyés sur le salon.

Vous pouvez maintenant créer un tableau vide de `Message` dans un `useState` (il vous faudra créer une interface pour indiquer ce que contient un message). Il servira à contenir tous les messages. Bien sur, il est vide pour le moment.

En React, il existe une superbe fonctionnalité appelée `useEffect hook`.

> :bulb: Les `hooks` sont des morceaux de codes servant à mettre à jour un composant selon des paramètres (la modification d'une variable par exemple). Si le composant n'a pas de dépendance, il sera mis à jour lorsque le composant sera rendu.

Votre `hook` va permettre de récupérer les messages, les indexer dans le tableau puis les afficher. Pour récupérer les données des messages, faite un appel à l'API.

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

#### Ressources

- [Les hooks en React](https://fr.reactjs.org/docs/hooks-effect.html)

## Exercice 05 - Envoyer des messages

Pour envoyer un message, vous devez simplement créer un formulaire à l'intérieur du composant `ChatRoom`.

Ce nouveau sous-composant va envoyer une requête au backend avec le message lorsque l'utilisateur va valider son formulaire. Vous devrez bien sure envoyer une requête à l'API pour créer le message.

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

:warning: Vous allez tout de même être face à un problème ! Même si le message est enregistré sur le serveur, il ne sera pas affiché côté front.

Trouvez un moyen de mettre à jour votre salon grâce à des `hooks` quand vous envoyez un nouveau message.

#### Ressources

- [Les hooks en React](https://fr.reactjs.org/docs/hooks-effect.html)

## Exercice 06 - Récupérer les messages en temps réel

Actuellement on peut rafraichir la liste des messages que l'on reçoit quand on envoie des messages, mais il n'est pas possible de mettre à jour notre liste de messages sans envoyer de messages, on doit trouver une solution à cela !

Normalement pour mettre à jour notre liste de messages on devrait utiliser les websocket.

Comme cela est plutôt long à mettre en place, nous allons plutôt faire autrement.

Créez un bouton "refresh", qui, au click, rafraichit notre liste de messages, et ce même si on n'a pas envoyé de nouveau message !

:bulb: Vous pouvez même passer à la vitesse supérieure et rafraichir votre page toute les X secondes avec un autre bouton !
Vous aurez pour cela besoin d'utiliser une fonctionnalité de TypeScript: `interval`.

#### Ressources

- [Les intervals](https://www.w3schools.com/jsref/met_win_setinterval.asp)

## Exercice 07 - interagissez avec vos messages

Dans votre composant `Message`, ajouter à chaque message un bouton permettant de supprimer les messages.

Pour supprimer les messages, au click du bouton, faites une requête à l'API:

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

Vous pouvez aussi créé un bouton "modifier" qui permettrait à l'utilisateur de modifier son message en remplissant un `form` (pour le nouveau message)

> Lisez la documentation de l'API pour trouver la route et les informations à envoyer.

Il faudra bien faire attention au retour de l'API, en effet, celle-ci renverra une erreur si vous n'êtes pas le propriétaire du message que vous essayez de modifier, il faudra alors afficher cette erreur.

## Bonus

Si tout est fonctionnel, vous pourriez rajouter quelques fonctionnalités :

- Rajouter des animations
- Faire une version mobile de votre app
- Pouvoir afficher dans un salon des images envoyées (un system d'incorporation de fichier, comme dans Discord par exemple)

#### Ressources complémentaires

- [React](https://fr.reactjs.org/)
- [CSS](https://developer.mozilla.org/fr/docs/Web/CSS)
- [TS](https://www.typescriptlang.org/)
