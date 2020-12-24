# Piscine Software - Jour 1

✔ Savoir setup un projet Go.

✔ Apprendre les bases du Go.

{

MAYBE<br>
✔ Intégrer les bonnes pratiques du développement web.

✔ Communiquer avec une API.

}

Un des principes fondamentaux du Go est que le language doit être facile d'apprentissage et d'utilisation.

Il est difficile de faire mieux que le [tour du Go](https://tour.golang.org) introduisant aux notions qui vous serviront pour coder en Go.<br>
Il présente aussi le [Go Playground](https://play.golang.org/), un outil très utile pour tester ou partager rapidement du code.

En tant que nouveaux gophers, vous serez très souvent amenés à revenir sur ces deux outils, gardez donc ces ressources à portée de main.<br>
N'hésitez pas à regarder rapidement la documentation donnée par ce tour du go, pour que vous commenciez à vous repérer.<br>
Ce tour servira de fil rouge pour cette journée.

Afin de vous introduire aux principes du Go et de la syntaxe, faites ces deux parties :
  - [Introduction](https://tour.golang.org/welcome/1)
  - [Basics](https://tour.golang.org/basics/1)

(Vous pouvez passer les exercices de ce Go Tour)

<br><br><br>

## Exercice 1 - Fichier Csv / Syntaxe / GoPackages

Le but de cet exercice est de lire un fichier `csv` et stocker les données dans une liste d'int.

### 1. Lire un csv

Un fichier csv (comma separated values) est un type de fichier contenant des lignes de données, séparées par une virgule.<br>
Dans cet exercice, le fichier fourni sera généralement sous cette forme.
```
500,200,300
50,20,30
5000,2000,3000
```

Dans un premier temps, faites une fonction qui prend un chemin (string) en paramètre et qui retourne deux choses
  - une liste de liste de string (type : [][]string)
    - Le premier niveau de liste doit correspondre aux lignes, le second aux colonnes du CSV
  - une erreur représentant l'erreur survenue, s'il y en a une (type : error)
Cette fonction doit lire le fichier en utilisant le package [csv](https://golang.org/pkg/encoding/csv/).

Dès qu'une erreur survient dans l'exécution de votre programme, renvoyez une slice nulle et cette erreur.<br>
C'est une bonne pratique d'utiliser le package [log](https://golang.org/pkg/log/) pour imprimer vos erreurs.


### 2. Traiter les données.

Faites une fonction qui prend en paramètre vos données lues à partir du csv (`[][]string`) et qui renvoie une liste de `int` (`[]int`) et une erreur (`error`).<br>
À partir des données du fichier csv, vous devez transformer les strings en int et les mettre dans une liste.<br>
Il est recommandé d'utiliser le package [strconv](https://golang.org/pkg/strconv/) pour traiter vos données.

Ensuite faite la fonction suivante (respectez le prototype) :
```go
func Exo1(csvPath string) ([]int, error)
```
Elle appellera vos deux fonctions qui lisent le csv et traitent les données pour renvoyer une liste d'int.<br>
Si une erreur survient pendant l'exécution de votre programme, renvoyez une slice nulle et cette erreur.<br>
Si votre liste est vide, renvoyez une [erreur](https://golang.org/pkg/errors/) avec le message "list is empty".

<br><br><br>

## Exercice 3 - Closure Functions


<br><br><br>

## Exercice 4 - Higher-Order Functions

L'objectif de cet exercice est de découvrir le principe des `higher-order functions`.<br>
Ce concept est utilisé en Go et dans de nombreux autres langages.<br>
Une fonction est dite `higher-order` lorsque elle prend en paramètre une autre fonction, appelé `callback`, ou lorsque elle renvoie une nouvelle fonction.

Dans cet exercice, nous allons nous intéresser aux fonctions passées en paramètre.<br>
Pour cela, vous allez implémenter 4 fonctions de manipulation de tableau : `filter`, `map`, `reduce` et `sort`.

### 1 - filter

`filter` prend en paramètre un tableau de `int` et une fonction callback.<br>
Cette fonction callback prend en paramètre un `int` et renvoie un booléen. Cette fonction est dite `predicate`.<br>
`filter` appelle le callback pour chaque élément du tableau, et renvoie un nouveau tableau contenant uniquement les éléments pour lesquels le callback a renvoyé `true`.

Exemple :
```go
func isEven(n int) bool {
    return n % 2 == 0
}

func testFilter() {
    numbers := []int{1, 2, 3, 4, 5}
    
    evenNumbers := Filter(numbers, isEven)
    fmt.Println(evenNumbers)
    // Output : "[2, 4]"
}
```

Ici, on passe `isEven` à `filter` afin de filter uniquement les nombres pairs du tableau `numbers`.

Tips : vous pouvez déclarer une fonction anonyme directement en appelant une fonction :
 - `evenNumbers := Filter(numbers, isEven)`<br>
est équivalent à
 - `evenNumbers := Filter(numbers, func(n int) bool { return n%2 == 0 })`

### 2 - map

`map` est assez similaire à `filter`, sauf que au lieu de prendre en paramètre une fonction booléenne,
`map` prend une fonction renvoyant un `int` et applique cette fonction pour tous les éléments du tableau donné en paramètre.<br>
Les éléments transformés sont stockés dans un nouveau tableau qui est renvoyé par `map`.

Exemple :
```go
func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}

func testMap() {
    numbers := []int{-2, -1, 0, 1, 2}
    
    positiveNumbers := map(numbers, abs)
    fmt.Println(positiveNumbers)
    // Output : "[2, 1, 0, 1, 2]"
}
```

Ici, on passe `abs` à `filter` afin d'obtenir un tableau contenant uniquement des valeurs positives.

### 3 - reduce

`reduce` est plus tordu que les 2 fonctions précédentes.<br>
`reduce` va parcourir un tableau donné en paramètre, et va appeler une fonction callback pour chaque élément.<br>
Le callback renvoie un `int` et prend les paramètres suivants :
  - la valeur de retour du précédent appel du callback, appelé `accumulateur`. Il s'agit donc d'un `int`.
  - Un autre `int`, qui est l'élément courant du tableau.

Quant à `reduce`, elle prend 3 paramètres :
  - le tableau de `int` à traiter.
  - la fonction callback
  - un `int`, qui est la valeur initiale de l'accumulateur.
`reduce` renvoie l'accumulateur, c'est-à-dire la dernière valeur de retour du callback. C'est donc un `int`.

Exemple :
```go
func add(acc, n int) int {
    return acc + int
}

func testReduce() {
    numbers := []{1, 2, 3, 4, 5}
    
    sum := Reduce(numbers, add, 0)
    fmt.Println(sum)
    // Output : "15"
}
```
Ici, on utilise `reduce` afin de calculer la somme d'un tableau de nombres.<br>
Le paramètre `acc` de la fonction `add` étant la valeur de retour de `add` pour le précédent élément du tableau,
additionner `acc` avec l'élément courant permet d'obtenir la somme !

### 4 - sort

Vous allez implémenter une fonction de tri qui prend en paramètre un tableau de `int` et une fonction de comparaison.<br>
Ce callback prend 2 `int ` et renvoie un `bool`.<br>
La fonction `sort` considère que 2 éléments du tableau sont à `swap` uniquement si le callback renvoie `true`.<br>
`sort` ne renvoie rien et tri le tableau passé en paramètre.

Un algorithme de tri performant n'est pas nécessaire, ce n'est pas l'objectif de l'exercice.<br>
Un tri basique suffira amplement.

Exemple :
```go
func ascendingCmp(a, b int) bool {
    return a > b
}

func descendingCmp(a, b int) bool {
    return a < b
}

func testSort() {
    numbers := []int{6, 2, -1, 3, 0}
    
    sort(numbers, ascendingCmp)
    fmt.Println(numbers)

    sort(numbers, descendingCmp)
    fmt.Println(numbers)
    
    // Output : 
    // [-1, 0, 2, 3, 6]
    // [6, 3, 2, 0, -1]
}
```

Ici, on se sert de `sort` afin de trier un tableau de façon croissante puis de façon décroissante.

<br><br><br>

## Exercice 4. Structures - Interfaces - Compositions d'interfaces
Maintenant, il est temps de revenir sur le GoTour. Faites la partie sur les [méthodes et interfaces](https://tour.golang.org/methods/1) .
(Vous pouvez passer les exercices de ce Go Tour)

Une interface en Go est un moyen de définir un comportement sur des structures de données différentes.

Par exemple, la fonction fmt.Println(...) va tester l'existence de la méthode `String() string` sur les arguments qui lui sont donnés.
Si cette méthode n'est pas implémentée, elle va imprimer l'argument du mieux qu'elle peut.
Vous pouvez donc implémenter la méthode `String() string` pour vos propres types afin d'avoir un output plus clair.
Si votre type implémente la méthode `String() string`, on dit donc qu'elle implémente l'interface `Stringer`.

D'autres interfaces sont très utilisées, comme les Reader et Writer. Elles permettent respectivement de lire ou d'écrire sur n'importe quelle type de données (fichier, socket, etc)
Vous pouvez parfois tomber sur l'interface ReadWriter qui est une interface regroupant les deux interfaces Reader et Writer.
Ou dans le même principe WriteCloser qui est une interface regroupant les deux interfaces Writer et Closer.


Les interfaces sont très utilisées en go pour faire des fonctions prenant en paramètre n'importe quel type implémentant cette interface.


### 1. Stringer.
Pour commencer, déclarez les structures suivantes :
```go
type circle struct {
    radius float64
}

type rect struct {
    width, height float64
}

type triangle struct {
    a, b, c float64
}
```

Implémentez l'interface `Stringer` pour ces 3 types (le choix du format est libre).
Testez d'imprimer des variables déclarées avec ces 3 types différents.


### 2. L'interface PerimeterCalculator
Déclarez l'interface `PerimeterCalculator` qui implémente la méthode `perim() float64`.
Implémentez cette méthode pour ces trois types.

Pour finir, faites une fonction nommée `Perim` qui prend comme unique paramètre l'interface `PerimeterCalculator` et qui renvoie le résultat de la méthode `perim() float64`.

Pour rappel, le périmètre est obtenu par les formules suivantes :
  - Rectangle: 2 * width + 2 * height
  - Cercle: 2 * Pi * radius
  - Triangle: a + b + c


### 3. L'interface AreaCalculator
Déclarez l'interface `AreaCalculator` qui implémente la méthode `area() float64`.
Implémentez cette méthode pour ces trois types.

Pour finir, faites une function nommée `Area` qui prend comme unique paramètre l'interface `AreaCalculator` et qui renvoie le résultat de la méthode `area() float64`.

Pour rappel, l'aire est obtenue par les formules suivantes :
  - Rectangle: width * height
  - Cercle: Pi * radius * radius
  - Triangle : \sqrt{s * (s - a) * (s - b) * (s - c)} (avec s = Périmètre / 2)


### 4. L'interface AreaPerimCalculator.
En Go, il est possible de Composer des types à partir d'autres types déjà existants.

Par exemple :
```go
type Person struct {
	Name string
	Age  int
}

func (p Person) Greet() {
	fmt.Println("Hello ", p.Name)
}

type Worker struct {
	Person
	Job string
}

// func (w Worker) Greet() {
// 	fmt.Println("Hello Worker", w.Name)
// }
```
Le type Worker possède tous les champs et les méthodes de Person.
Il possède donc les champs `Name` et `Age` et la méthode `Greet()` qu'il peut choisir de réécrire ou non.
On dit que Worker est composé à partir de Person.

Il est naturellement possible de faire aussi :
```go
type Person struct {
	Name string
	Age  int
}

type Job struct {
	Description  string
	Address      string
}

type Worker struct {
	Person
	Job
}
```
Dans ce cas, les structures Person et Job ne peuvent pas avoir de champs en commun.
Et toutes les méthodes communes aux 2 types doivent être spécifiées.


Le principe est exactement le même pour les interfaces. Comme pour l'interface ReadWriter, il est possible de composer une interface à partir de 2 interfaces plus petites.
C'est pourquoi des nombreuses interfaces en Go ne sont composées que d'une seule méthode (pour respecter le principe de [Single Responsibility](https://en.wikipedia.org/wiki/Single-responsibility_principle)).


Déclarez l'interface `AreaPerimCalculator` qui est composée des 2 interfaces `PerimeterCalculator` et `AreaCalculator`.

Pour finir, faites une function nommée `Area` qui prend comme unique paramètre l'interface `AreaPerimCalculator` et qui renvoie le résultat des fonctions `Area` et `Perim`.

## Exercice 5 - Factory
<!-- TODO: -->

<br><br><br>

## Exercice 6 - Tests
<!-- TODO: -->

<br><br><br>

## Exercice 7 - Csv to Json

Le but de cet exercice est de transformer un fichier `Csv` en `Json`.

Utilisant la fonction pour lire le csv au début du jour et grâce au package.
Dans cet exercice, le fichier fourni sera généralement sous cette forme.
```
Worker1,1,[500,200,300]
Worker2,2,[50,20,30]
Worker3,3,[5000,2000,3000]
```

Déclarez une fonction suivant ce prototype :
```go
func CsvToJson(csvFile, jsonPath string) error
```

À l'aide de la structure suivante et du package [Json](https://golang.org/pkg/encoding/json/), transformez les données du fichier CSV donné en paramètre vers le format Json et écrivez-les dans un nouveau fichier avec le chemin donné en paramètre.
```go
type Worker struct {
	Name string
	Id   int
	Truc []int
}
```

Tips : Google est votre ami.



## Exercice 8 - Go Routine et Channel

Votre objectif dans cet exercice est d'optimiser vos temps de calcul grâce à l'asynchrone.<br>

<!-- TODO: donner une définition de l'asynchrone ou prévoir un talk sur le sujet -->

Vous allez donc utiliser les différents keywords, `go`, `select` et `chan` pour y arriver.<br>
*Prenez 10 minutes pour retourner sur la partie du go tour dédiée à ça.*

Voici un code en go, son temps d'exécution est d'environ 4.5 secondes si on lui donne `0` en entrée, votre objectif est d'obtenir un temps inférieur a 2 secondes.<br>
Bien évidemment, vous ne pouvez modifier que la fonction `Calcul`

```go
func HeavyCalculation(v int) int {
	time.Sleep(450 * time.Millisecond)
	return v + v
}

func GetLoopSlice(v int) []int {
	time.Sleep(1 * time.Second)
	length := ((v / 3) + 2) * 4
	s := make([]int, length)
	for i:=0; i != length; i++ {
		s[i] = i
	}
	return s
}

func Calcul(input int) int {

	slice := GetLoopSlice(input)
	for i, elm := range slice {
		slice[i] = HeavyCalculation(elm)
	}

	res := 0
	for _, elm := range slice {
		res += elm
	}
	return res
}
```

Il vous est fortement conseillé d'utiliser votre `startTimer` fait lors de l'exercice 3 !
Il existe beaucoup de documentation utile sur la concurrency en ligne, jetez y un œil https://devhints.io/go#Concurrency

## Exercice 9 - ???
<!-- TODO: -->

<br><br><br>

## Exercice 10 - Mashup
Dans cet exercice, vous allez devoir créer une fonction qui :
* prend un path vers un fichier json en argument.
* récursivement et de manière asynchrone, passe dans toutes les branches du json.
* ressort la somme de tous les floats qui se trouvent dans le json avec le moins de temps d'exécution possible.

Attention, vous savez gérer des erreurs, votre fonction ne doit pas crash et doit ressortir une erreur claire au besoin.
On vous donne un petit json de test pour celui-ci
> 1.2 + 1.23 + 1.3 + 1 + 2 + 3 + 10 + 12 + 12 + 1 + 11

55.730000000000004
(l'utilisation de float64 ajoute une petite incertitude)

```json
{
  "value": 1.2,
  "object": {
    "v": 1.23,
    "b": {
      "d": 1.3,
      "s": "aaaaaaa"
    },
    "s": [
      1,
      2,
      3
    ]
  },
  "qw": [
    {
      "a": 10
    },
    {
      "v": "ffff",
      "2": 12
    }
  ],
  "aa": [
    12,
    "aaa",
    [
      1,
      {
        "11": 11,
        "12": "haha"
      }
    ]
  ]
}
```