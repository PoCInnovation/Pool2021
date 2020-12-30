# Piscine Software - Jour 1

✔ Savoir setup un projet NodeJS.

✔ Apprendre les bases du Typescript.

✔ Intégrer les bonnes pratiques du développement web.

✔ Communiquer avec une API.

## Exercice 00 - Prérequis

- [NodeJS](https://nodejs.org/en/) >= 10 ([installation](https://lmgtfy.com/?q=how+to+install+nodejs))
- [npm](https://www.npmjs.com/) (généralement installé avec NodeJS)

Nous vous demanderons d'effectuer vos rendus sur GitHub, dans un dépôt public. Nommez le `POC_SoftwarePool2021` et créez le dossier `day01`.

Envoyez-nous un message sur Discord avec le lien de votre dépôt pour que l'on puisse suivre l'avancée de votre travail et, possiblement, faire passer des tests automatisés.

De plus, vous devrez utiliser `VSCode` ou `WebStorm` pour cette piscine car emacs sera trop limité pour ce que nous allons voir.

#### Ressources
- [NodeJS](https://nodejs.org/en/)
- [Npm](https://www.npmjs.com/)
- [Installer Webstorm](https://console.bocal.org/)

## Exercice 01 - Hello World

<!-- TODO leur apprendre à installer node avec nvm et spécifier une version -->

- Créer une application NodeJS basique avc `npm init`.
- Installer TypeScript avec `npm install -D typescript ts-node eslint @types/node`.
- Créer le dossier `src` et le fichier `index.ts` dans ce dernier.
- Dans le fichier `index.ts`, écrivez une fonction qui permettra d'afficher `Hello World`.
- Ajouter une règle `start` dans le `package.json`:
  - Elle execute `ts-node src/index.ts`

> Se documenter sur la structure basique d'une application NodeJS, à quoi servent les fichiers `package.json`, `package.lock.json` ?
>
> Si tout se passe bien `npm start` devrait lancer votre application et afficher dans le terminal `Hello World`.

#### Ressources
- [Typescript pour les débutants](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)

## Exercice 02 - Coder bien pour soi et pour les autres

Il est important d'avoir une norme commune au sein d'un projet. C'est pour ca qu'il est intéressant d'intégrer [ESLint](https://eslint.org/) a votre projet.

- Ajouter ESLint à votre `package.js`:
```sh
npx eslint --init
```
<Details><Summary><strong>Suivez ces options lors du paramétrage de ESlint</strong></Summary>
<pre>
? How would you like to use ESLint? <b>To check syntax, find problems, and enforce code style</b>
? What type of modules does your project use? <b>JavaScript modules (import/export)</b>
? Which framework does your project use? <b>None of these</b>
? Does your project use TypeScript? <b>Yes</b>
? Where does your code run? <b>Node</b>
? How would you like to define a style for your project? <b>Use a popular style guide</b>
? Which style guide do you want to follow? <b>Airbnb: https://github.com/airbnb/javascript</b>
? What format do you want your config file to be in? <b>JavaScript</b>
Checking peerDependencies of eslint-config-airbnb-base@latest
The config that you've selected requires the following dependencies:

@typescript-eslint/eslint-plugin@latest eslint-config-airbnb-base@latest eslint@^5.16.0 || ^6.8.0 || ^7.2.0 eslint-plugin-import@^2.21.2 @typescript-eslint/parser@latest
? Would you like to install them now with npm? <b>Yes</b>
</pre>
</Details>

- Ajouter dans votre `package.json` la règle 'lint' qui exécute `eslint src/**/*`
- Ajouter dans votre `package.json` la règle 'lint:format' qui exécute `eslint --fix src/**/*`

Ces étapes viennent de paramétrer ESlint pour qu'il suive une norme spécifique, celle d'AirBnB. 
Si vous exécutez les deux règles que vous venez de créer sur votre fichier `index.ts`, vous verrez qu'il trouvera surement des erreurs de syntaxe, puis qu'il les corrigera tout seul !

Vous pouvez installer l'extension Eslint pour votre IDE afin d'avoir les erreurs visibles directement sur votre code.

> :bulb: Il existe aussi un module spécial nommé [Prettier](https://prettier.io/) qui vous permet de configurer le formatage de votre code.

#### Ressources
- [ESlint](https://eslint.org/)
- [ESlint sur Webstorm](https://www.jetbrains.com/help/webstorm/eslint.html)
- [ESlint sur VSCode](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

## Exercice 03 - Super Computer

Rentrons maintenant dans le vif du sujet ! 
Un groupe d'ingénieur travaillant pour les programme spatiaux du monde entier se préparent à envoyer un certain nombre d'astronautes en mission. Pour cela, il leur faudra un super calculateur capable d'effectuer des opérations variées.

- Créer une fonction `superComputer` avec le prototype suivant consommant 4 paramètres :
  - Le premier nombre
  - Le symbole opératoire
  - Le second nombre
  - Une fonction où envoyer le résultat (et possiblement l'erreur survenue)

> :bulb: Il peut être utile de définir vos symboles opératoires dans une [énumération](https://www.typescriptlang.org/docs/handbook/enums.html).

Votre callback auras le type suivant :
```ts
type Callback = {(err: Error, result?: undefined): Error, (err: null, result: number): number};
```

> L'utilisation du type `any` est interdite

> Prendre en paramètre une fonction où envoyer le résultat est une pratique courante en JavaScript. Ce sont des `callbacks` (pour `appel retour`). Nous vous laissons vous renseigner à ce sujet.

> L'opération peut échouer. Auquel cas nous vous demandons de nous envoyer en premier paramètre de la fonction l'erreur survenue.

> Prêtez attention à la note précédente. Relisez-la.

- Mettre en place une gestion d'erreur :
  - Opérateur invalide (`Bad operator`)
  - Division par 0 (`Division by 0`)
  - _Something else?_

**Rendu :** `src/superComputer.ts`.

#### Ressources
- [Types](https://www.typescriptlang.org/docs/handbook/basic-types.html)
- [Callback](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)
- [Gestion d'erreur](https://basarat.gitbook.io/typescript/type-system/exceptions)

## Exercice 04 - Un homme s'élève

Votre super calculateur est terminé !
Il vous faut à présent les hommes pour envoyer votre programme. Quoi de mieux que des cosmonautes ?

- Créez une `interface` "Cosmonaut" dans laquelle vous allez définir les attributs de celui-ci:
  - Un `name`
  - Une `mission`
  - Un `country`

> Copiez le fichier `types.ts` présent sur le repo du sujet dans votre dossier `src`, vous trouverez des énumérations des missions et pays alloués.

- Écrivez une fonction `createCosmonaut` qui prend en paramètres :
  - Un nom
  - Un pays
  - Une mission

Elle renverra un objet du type `Cosmonaut`.

**Rendu :** `src/createCosmonaut.ts`

#### Ressources
- [Objets](https://www.typescriptlang.org/docs/handbook/2/objects.html)
- [Interface](https://www.typescriptlang.org/docs/handbook/interfaces.html)

## Exercice 05 - Testing time

- Installer [jest](https://jestjs.io/): `npm install -D jest ts-jest @jest/globals @types/jest`
- Dans votre `package.json`
    - Ajouter la règle 'test' qui exécute `jest tests --env=node`
    - Ajouter la règle 'test:cov' qui exécute `jest --coverage tests --env=node`
    - Ajouter la règle 'test:watch' qui exécute `jest --watchAll tests --env=node`

<Details><Summary><strong>Il faut également créer un fichier `jest.config.js` avec les règles suivantes:</strong></Summary>
	
```js
module.exports = {
	roots: ['<rootDir>'],
	transform: {
		'^.+\\.tsx?$': 'ts-jest',
	},
	testMatch: ['**/tests/**/*.ts?()'],
	moduleFileExtensions: ['ts', 'js'],
};
```

</Details>

Créer des tests pour `superComputer` et `createCosmonaut` dans le dossier `tests` (qu'il faut créer)

<Details><Summary><strong>Exemple d'utilisation de Jest:</strong></Summary>
	
Supposons que vous vouliez tester la fonction suivante:
```ts
// sum.ts
/**
 * Simply do an addition
 *
 * @param nbOne first number to compute
 * @param nbTwo second number to compute
 * @return result of nbOne + nbTwo
 */
export default (nbOne: number, nbTwo: number): number => {
	return nbOne + nbTwo;
};
```

Votre fichier de test donnera :

```ts
// sum.tests.ts
import { describe, it, expect } from '@jest/globals';
import sum from '../src/sum';

/**
 * Test sum function
 * Compute some number to verify if sum is working well
 */
describe('Test sum function', () => {
	it('Simply 1 + 1', () => {
		expect(sum(1, 1)).toBe(2);
	});

	it('The answers of the Universe !', () => {
		const result: number = sum(21, 21);
		expect(result).toBe(42);
	});
});
```

</Details>

> La convention veut que vous nommiez vos fichiers de test de la façon suivante : <fichier_testé>.tests.ts
>
> Exemple : `superComputer.tests.ts`

**Rendu :** `tests/`

#### Ressources
- [Jest](https://jestjs.io/)
- [JestConfig](https://jestjs.io/docs/en/configuration)

## Exercice 06 - Vous m'avez dit JSON ?

Il existe un formatage de donnée très utilisé en programmation : le `JSON`

Nos cosmonautes étaient enregistrés dans ce format, suite à un flash solaire intense, nous avons perdu nos données.

C'est à vous de sauver le coup.

- Écrivez le JSON d'un cosmonaute dans le fichier `cosmonaut.json`.
- Créez la fonction `getCosmonaut` qui prend en paramètres :
  - Le `path` du JSON
  - Et qui renvoie un objet `Cosmonaut` grâce aux fonctions précédentes.

**Rendu :** `src/getCosmonaut.ts` et `src/cosmonaut.json`

#### Ressources
- [Le JSON pour les débutants](https://www.w3schools.com/whatis/whatis_json.asp)
- [Importer du JSON en Typescript](https://hackernoon.com/import-json-into-typescript-8d465beded79)

## Exercice 07 - Touch the moon
   
Vous allez maintenant envoyer des requêtes à la station afin de récupérer les cosmonautes déjà présents !
C'est une simple API rest sur laquelle vous pouvez envoyer des requêtes http.

<!-- TODO définir ici ou pendant un talk ce qu'est HTTP et une API Rest -->

Pour communiquer avec celle-ci, il vous faudra installer la dépendance [axios](https://www.npmjs.com/package/axios). C'est un client http.

L'objectif est simple : 
- Faites une fonction `selectCosmonaut`qui prend en paramètres :
  - Une `mission`
  - Un `pays`

Elle devra renvoyer un `Array` de tous les cosmonautes présents sur la station respectant les critères envoyés en paramètre.

:warning: L'appel à l'API se fait de manière `asynchrone`, vous devrez donc utiliser une `Promise` pour englober le tout.

Les promesses sont une notion assez complexe du JavaScript, donc si vous bloquez trop longtemps sur l'exercice, écrivez plutôt une fonction `asyncSelectCosmonaut` dans laquelle vous avez le droit d'utiliser le couple `async/await`.

> L'adresse de l'api est `http://localhost:7600`
>
> Une documentation de l'API est disponible à l'adresse : `http://localhost:8000`
>
> Que se passe-t-il si l'API ne vous répond pas ?

**Rendu :** `src/selectCosmonaut.ts`

#### Ressources
- [Asynchronicité](https://eloquentjavascript.net/11_async.html)
- [Méthode d'un tableau](https://www.tutorialsteacher.com/typescript/typescript-array)
- [Promesse](https://basarat.gitbook.io/typescript/future-javascript/promise)

## Exercice 08 - Direction l'espace

Il est temps d'envoyer votre cosmonaute sur PoCSpace.

Faites une fonction `sendCosmonaut` qui prend en paramètre 
  - Un `name`
  - Une `mission`
  - Un `country`

Elle devra créer un cosmonaute à partir des arguments puis envoyer le cosmonaute à l'API à travers une requête. Vous renverrez le résultat de celle-ci.

> L'utilisation du couple `async/await` est permise.

> Attention à la méthode de votre requête.

**Rendu :** `src/sendCosmonaut.ts`.

#### Ressources
- [Les méthodes http](https://developer.mozilla.org/fr/docs/Web/HTTP/M%C3%A9thode)
- [Le couple async / await](https://blog.logrocket.com/async-await-in-typescript/)

## Exercice 09 - Un petit pas pour l'homme

Comme vous avez pu le remarquer, votre cosmonaute est resté bloqué sur Terre.

En effet, il vous faut équiper une combinaison. Celle-ci étant composée de plusieurs parties, vous devrez faire plusieurs fonctions.

### Les composants

L'objectif est de faire une chaîne d'assemblage, vous devrez donc pour chaque pièce listée, faire une fonction recevant en paramètre :
  - La combinaison en cours de fabrication
  - Les différents paramètres nécessaires à la construction de la pièce
  - Une fonction `callback`

La callback devra être appelée en cas de succès avec la combinaison mais aussi en cas d'échec avec l'erreur.

Souvenez-vous de l'exercice `03`. Le concept des callbacks reste le même.

Voici les différentes parties de la combinaison :
  - Helmet (via `createHelmet`), nécessitant une `color` et le `body` d'équipé
  - Body (via `createBody`) nécessitant une `color` et un `kind`
  - Gloves (via `createGloves`) nécessitant une `color` et le `helmet` d'équipé
  - Boots (via `createBoots`) nécessitant une `color`

Chaque pièce viendra s'intégrer à votre combinaison. Vous devez donc dans un premier temps écrire une `interface` contenant l'ensemble de vos pièces avec leur propriété.
Voici un exemple possible d'interface :

```ts
interface Suit {
  helmet?: {
     color: Color;
   }
   // ...
}
```

> Toujours dans le fichier `types.ts`, vous trouverez des énumérations des couleurs allouées.

> Demandez-vous à quoi sert le `?` après la déclaration du `helmet` dans l'interface.

### L'assemblage

Une fois vos 4 fonctions écrites (et testées :joy:). Il vous faut créer la véritable chaîne d'assemblage.

- Créez une fonction `conveyorBelt` prenant en paramètre une combinaison, la liste de fonctions à appeler `consumers` ainsi qu'une callback à appeler à la fin de l'assemblage de la combinaison.

Les `consumers` prennent deux paramètres : la combinaison ainsi que la fonction `callback` après avoir ajouté la pièce.

> :warning: Utilisez la récursivité est conseillée
>
> :warning: Le type `any` est interdit, n'hésitez pas à demander de l'aide sur le typage.

Voici un exemple d'utilisation de la fonction `conveyorBelt`, vous trouverez aussi le type de la callback à utiliser :

```ts
type Callback = {(err: Error, result?: undefined): Error, (err: null, result: Suit): Suit};

conveyorBelt({}, [
   (suit: Suit, cb: Callback) => createBoots(suit, Color.RED, cb),
], callback);
```

Une fois la conveyorBelt terminée, écrivez une fonction `equipCosmonaut` qui prend en paramètres :
   - Un `cosmonaut`
   - Une `combinaison`

Elle devra renvoyer un object contenant `cosmonaut` avec un champ `suit` contenant la combinaison.

> N'oubliez pas de typer vos retours de fonction afin d'être plus explicite.
>
> :warning: Vos fonctions doivent être testées.
>
> Cet exercice est difficile. Prenez le temps et n'hésitez pas à demander de l'aide.

**Rendu :** `src/equipCosmonaut.ts`

#### Ressources
- [Overload](https://www.typescriptlang.org/docs/handbook/functions.html)
- [Interface](https://www.typescriptlang.org/docs/handbook/interfaces.html)

## Exercice 10 - Un grand pas pour l'humanité

Vous avez un cosmonaute équipé ! Il peut enfin quitter le plancher des vaches pour rejoindre ses collègues sur l'ISS

- Créez une fonction __asynchrone__ `sendSuit` qui prend en paramètre une `combinaison` et l'`id` de votre cosmonaute, elle devra envoyer une requête à l'API pour équiper le cosmonaute.

- Créez une fonction __asynchrone__ `flyCosmonaut` qui va envoyer une requête sur la route `fly` avec en paramètre la mission ISS.
  - La fonction devra prendre en paramètre l'`id` du cosmonaut et la `mission`.

> Vous avez compris le concept, trouvez les bons endpoints dans la documentation. Attention aux méthodes des requêtes envoyées.
>
> Demandez-vous quel est le type de l'identifiant ? N'hésitez pas à utiliser les autres routes de l'API pour récupérer des informations. [Postman](https://www.postman.com/) peut vous être utile.

Si tout se passe bien, votre cosmonaute est maintenant en mission sur l'ISS, félicitation vous avez terminé le jour 1 de la piscine Software !

Vous pouvez passer au bonus si vous souhaitez apprendre la programmation orientée objet en Typescript.

**Rendu :** `src/sendSuit.ts` et `src/flyCosmonaut.ts`

## Bonus

// TODO: Refaire tous les exercices mais en orienté objet (road map à écrire)

##### Ressources
- [L'orienté object](https://codaholic.sillo.org/2016/04/05/typescript-poo-et-espaces-de-noms/)
- [Classe](https://www.typescriptlang.org/docs/handbook/classes.html)

## Ressources complémentaires :
- [Compiler du Typescript](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
- [Théorie des types appliqué au Typescript](https://medium.com/better-programming/understanding-typescripts-type-system-a3cdec8e95ae)
- [Les décorateurs](https://www.typescriptlang.org/docs/handbook/decorators.html)
- [Les décorateurs - Partie 2](https://medium.com/@simonb90/comprendre-et-utiliser-les-d%C3%A9corateurs-avec-typescript-3c6cf8d38065)
- [Le Templating](https://refactoring.guru/design-patterns/template-method/typescript/example)
- [Contribuer au Typescript](https://github.com/microsoft/TypeScript)
- [Contribuer au typage du Javascript](https://github.com/DefinitelyTyped/DefinitelyTyped)

> Poc - 2021
