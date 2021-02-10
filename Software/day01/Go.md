# PoC Software 2021, Go, Day1

# Sommaire

- [Requirements](#requirements)
- [Synopsis](#synopsis)
- [0 - Setup](#0---setup)
- [1 - Les cosmonautes sont d'abord des Humains!](#1---les-cosmonautes-sont-dabord-des-humains)
  * [1. Lire un fichier](#1-lire-un-fichier)
  * [2. Traiter les données](#2-traiter-les-données)
  * [3. Créer la vie](#3-créer-la-vie)
- [2 - Vous avez dit JSON?](#2---vous-avez-dit-json)
- [3 - Coder proprement pour soi & pour les autres (gofmt)](#3---coder-proprement-pour-soi-et-pour-les-autres-gofmt)
- [4 - Tester, ce n'est pas douter (go test)](#4---tester-ce-nest-pas-douter-go-test)
- [5 - Créez vos pilotes](#5---créez-vos-pilotes)
  * [1. Types](#1-types)
  * [2. Interfaces](#2-interfaces)
  * [3. Votre première interface](#3-votre-première-interface)
- [6 - Préparez vos pilotes](#6---prparez-vos-pilotes)
  * [1. Arguments variadiques](#1-arguments-variadiques)
  * [2. Composition d'interface](#2-composition-dinterface)
- [7 - Un équipage pour des missions](#7---un-équipage-pour-des-missions)
- [8 - Préparer votre mission](#8---préparer-votre-mission)
  * [1. L'API](#1-lapi)
  * [2. Destination Finale](#2-destination-finale)
  * [3. Votre Équipage](#3-votre-équipage)
- [9 - Functions are citizen too](#9---functions-are-citizen-too)
  * [1. Closure](#1-closure)
  * [2. Higher-Order Functions](#2-higher-order-functions)
    + [1. Filter](#1-filter)
    + [2. Map](#2-map)
    + [3. Reduce](#3-reduce)
    + [4. Sort](#4-sort)
- [10 - Concurrency](#10---concurrency)
- [11 - Concurrency v2](#11---concurrency-v2)

# Requirements

Un des principes fondamentaux du Go est que le language doit être facile d'apprentissage et d'utilisation.

Il est difficile de faire mieux que le [tour du Go](https://tour.golang.org) introduisant aux notions qui vous serviront
pour coder en Go. Il présente aussi le [Go Playground](https://play.golang.org/), un outil très utile pour tester ou
partager rapidement du code.

En tant que nouveaux gophers, vous serez très souvent amenés à revenir sur ces deux outils, gardez donc ces ressources à
portée de main. N'hésitez pas à regarder rapidement la documentation donnée par ce tour du go, pour que vous commenciez
à vous repérer. Ce tour servira parfois de fil rouge pour cette journée (vous pouvez passer les exercices).

Afin de vous introduire aux principes du Go et de la syntaxe, il est vivement recommendé de regarder:

- [Introduction](https://tour.golang.org/welcome/1)
- [Basics](https://tour.golang.org/basics/1)
- [Go Tour](https://tour.golang.org)
- [Go Docs](https://golang.org/doc/)
- [Go Playground](https://play.golang.org/)

Finalement, prenez le temps de lire les exercices. Des ressources sont fournies,
notamment des packages qui peuvent vous facilitez la vie.

# Synopsis

Le/La COVID-19 est en train de décimer le monde. La survie de l'humanité (rien que ça) ne repose que sur vos épaules.
L'Agence Spatiale Internationale a décrétée l'exode de la population restante vers l'espace.
Votre rôle est d'envoyer des colons sur de nouvelles planètes afin de prévenir l'extinction de l'humanité.

Vous devrez pour cela organiser des missions en lançant une mission spatiale dans laquelle se trouve un
équipage composé de pilotes, de techniciens et de passagers.

# 0 - Setup

Pour commencer votre mission, il vous faut un moyen de sauvegarder et partager votre code.

- Créez un Repo Github en public nommé POC_SoftwarePool2021_Go et clonez le.
- Créez un dossier Day1. Tous vos exercices du jour se trouveront à l'intérieur.
- Initialisez un module go avec la commande `go mod init SofwareGoDay1`

# 1 - Les cosmonautes sont d'abord des Humains!

Pour emmener vos colons vers d'autres planètes dans votre navette spatiale, il vous faut d'abord des pilotes.
Chaque pays a mis a disposition de l'Agence Spatiale Internationale la liste des personnes qui vont constituer votre
équipage.
Vous devez tout d'abord apprendre à traiter ces données.

Le but de cet exercice est de lire un fichier contenant des données qui sont regroupées sous format
**csv** ([comma separated values](https://en.wikipedia.org/wiki/Comma-separated_values))

```	
Jason,25,USA
Jean-Luc,55,France
...
Rodriguo,34,Spain
```

Puis stocker ces données dans une liste de structures.

## 1. Lire un fichier

- Dans un package `data`, créez un fichier `csv.go`.

> :warning: Ce package va être utilisé comme "fourre-tout", c'est une très mauvaise pratique.
> Si plus tard vous êtes amenés à faire des packages qui ont des noms si vague (eg: utils, data, ...)
> et/ou qui servent de fourre-tout, c'est une "code smell". :warning:

- Créez une fonction qui prend un chemin en paramètre et qui retourne deux choses:

  - le contenu de votre fichier sous forme d'une liste de ligne.
  - une erreur, s'il y en a une.

```go
func ReadFile(path string) ([]string, error)
```

> Dès qu'une erreur survient dans l'exécution de votre fonction, renvoyez une slice nulle et cette erreur.
> C'est une bonne pratique d'utiliser le package [log](https://golang.org/pkg/log/) pour imprimer vos erreurs,
> ainsi qu'utiliser [fmt.Errorf](https://golang.org/pkg/fmt/#Errorf) pour ajouter du context aux erreurs que vous remontez.

## 2. Traiter les données

- Faites une fonction qui créer va séparer une string à chaque virgule (comma).
  Elle returnera aussi une erreur si la ligne ne respecte pas le format ci-dessus.

```go
func LineToCSV(line string) ([]string, error)
```

## 3. Créer la vie

- Dans un package `humanity`, créez `Human.go`.
- Créez une structure `Human`. Un humain est décris par son `Name`, son `Age` et son `Country`.
- Créez une fonction `NewHumanFromCSV`, le csv reçu sera toujours valide.

```go
func NewHumanFromCSV(csv []string) (*Human, error)
```

- Créez une fonction `NewHumansFromCsvFile`, vous devez évidemment utiliser les fonctions précédentes.

```go
func NewHumansFromCsvFile(path string) ([]*Human, error)
```

> Si une erreur survient renvoyez une slice nulle & l'erreur.
> Une liste vide sera considérée comme une erreur.

### **Ressources**

- [fmt package](https://golang.org/pkg/fmt/)
- [log package](https://golang.org/pkg/log/)
- [error package](https://golang.org/pkg/errors/)
- [strconv package](https://golang.org/pkg/strconv/)


# 2 - Vous avez dit JSON?

Pour chaque mission, l'ASI essaie de composer un équipage de pilotes issus de plusieurs nationalités afin d'éviter les
accusations de favoritisme et un retard dans le lancement des missions.

Le format CSV n'ayant pas une grande flexibilité, l'équipage vous est communiqué via le format [JSON](https://en.wikipedia.org/wiki/JSON)

```json
[
  {
    "Name": "Jason",
    "Age": 25,
    "Country": "USA"
  },
  {
    "Name": "Jean-Luc",
    "Age": 55,
    "Country": "France"
  },
  ...
  {
    "Name": "Jason",
    "Age": 34,
    "Country": "Spain"
  }
]
```
> Dans le monde du Web (et surtout les API), les données sont généralement transmises sous ce format.

Dans votre fichier `Human.go`, créez une nouvelle fonction `NewHumansFromJsonFile`.

```go
func NewHumansFromJsonFile(path string) ([]*Human, error)
```

### **Ressources**

- [JSON pour débutants](https://www.w3schools.com/whatis/whatis_json.asp)
- [JSON package](https://golang.org/pkg/encoding/json/)

# 3 - Coder proprement pour soi et pour les autres (gofmt)

Quand vous installer golang, avec le compilateur, vous avez à votre disposition un certain nombre d'outils, les
commandes, qui facilitent votre travail.

L'un de ces outils est le `gofmt` (à ne pas confondre avec le package fmt). Il permet de rapidement formatter les
fichiers selon certaines règles du coding style go.

Attention, cela ne vous dispense pas de suivre les principes du [SOLID Design](https://en.wikipedia.org/wiki/SOLID).
Cet outil ne fait pas tout pour vous.

Comment s'en servir ?
- Shell `go fmt .`
- Goland
  - Fichier `ctrl+alt+l`
  - Projet `ctrl+alt+shift+p`
- VSCode `ctrl+shift+i` (plugin go requis)

N'oubliez pas de le faire régulièrement !

### **Ressources**

- [gofmt](https://golang.org/cmd/gofmt/)
- [goland](https://www.jetbrains.com/help/go/integration-with-go-tools.html#gofmt)
- [VSCode Extension](https://code.visualstudio.com/docs/languages/go#_formatting)


# 4 - Tester, ce n'est pas douter (go test)

Un peu de [culture](https://raygun.com/blog/costly-software-errors-history/).

Si vous êtes un développeur qui ne teste pas son programme, vous n'allez pas empêcher l'extinction de l'humanité et vous ne méritez pas d'échapper à cette extinction.

Avec le compilateur du Go, vous avez à votre disposition un outil de test intégré.

### Exemple pour `ReadLine`

Dans: **data/csv_test.go**
```go
package data

import "testing"

func TestLineToCSV(t *testing.T) {
    tests := []struct {
        in string
        out []string
        err bool
    }{
        {
            in: "jean,34,france",
            out: []string{"jean", "34", "france"},
            err: false,
        },
        {
            in: "j,j,j,j",
            out: nil,
            err: true,
        },
        {
            in: "j",
            out: nil,
            err: true,
        },
    }

    for _, test :=range tests {
        csv, err := LineToCSV(test.in)
        if test.err && err != nil {
            continue
        }
        if err != nil {
            t.Errorf("Error when converting line [%s]: %v", test.in, err)
            continue
        }
        for i, v := range test.out {
            if v != csv[i] {
                t.Errorf("Error when converting line [%s]:\n(exp)%v != (got)%v", test.in, test.out, csv)
            }
        }
    }
}
```

- Faites la commande `go test SofwareGoDay1/data`, vous devriez avoir ceci `ok gopool/data 0.002s`

### À votre tour

Faites des tests pour

- `ReadFile`
- `NewHumanFromCSV`
- `NewHumansFromCsvFile`
- `NewHumansFromJsonFile`

> Courage, cela peut être rapide si vous ne faites pas des tests redondants :)

# 5 - Créez vos pilotes

Maintenant que vous pouvez parser les données fournies par les autres pays, vous allez devoir préparer vos
Pilots.

Il est vivement conseillé de revenir au tour du Go pour faire la partie
sur [les méthodes et interfaces](https://tour.golang.org/methods/1)

## 1. Types

- Dans un nouveau fichier nommé `Pilot.go`, créez un type `Pilot` qui sera pour
  le moment une structure `Human` embedded.

```go
package humanity

type Pilot struct {
	*Human
}
```

- Faites une variable de type `Pilot` et printez là.

```go
package main
import "fmt"

func main() {
    fmt.Println(&Pilot{&Human{"Jason", 10, "Fr"}})
}
```


## 2. Interfaces

- Créez une méthode `String()` qui return `Human` sous forme de string.
  Le format de la string est le suivant: `Name, Age years old from Country`

```go
func (h *Human) String() string
```

Félicitation, vos humains implémentent leur premières interface! (`fmt.Stringer`)

- Printez à nouveau votre pilot et faites le parallèle avec ce qui vous est expliqué dans le tour du go sur
  l'interface Stringer.

## 3. Votre première interface

- Ajoutez un champ `Ready` de type `bool` dans votre type `Human`.

- Dans un fichier `Interfaces.go`, définissez une interface `Preparer` qui implémente la méthode Prepare().

```go
type Preparer interface {
       Prepare() error
}
```

- Implémentez l'interface `Preparer` pour votre type `Human`

```go
func (h *Human) Prepare() error
```

> Cette méthode donne la valeur `true` à votre champ `ready` et renvoie une erreur nulle.
> Elle imprimera aussi si votre humain est prêt, par exemple : `Human: Jason, 25 years old from USA is ready !`.

### **FAIRE DES TESTS**
### **Ressources**

- [Gotour: méthodes et interfaces](https://tour.golang.org/methods/1)
- [embedding](https://golang.org/doc/effective_go.html#embedding)

# 6 - Préparez vos pilotes

## 1. Arguments variadiques

- Dans `Interfaces.go`, créez une fonction `prepareMissionPart`  qui appelle `Prepare()` sur chaque argument.

```go
func PrepareMissionPart(objs ...Preparer) error
```

> En go, un argument variadique est représenté sous la forme d'une slice du type de ces arguments.

> Si une erreur survient pendant l'exécution de votre fonction, renvoyez cette erreur.


Pour tester votre fonction, vous pouvez déclarer une liste d'interface `Preparer` (`[]Preparer`).

```go
pilotList := []Preparer{
    &Pilot{
        Human: Human{
            Name:    "Jason",
            Age:     25,
            Country: "USA",
            Ready:   false,
        },
    },
    &Pilot{
        Human: Human{
          Name:    "Jean-René",
          Age:     77,
          Country: "France",
          Ready:   false,
        },
    },
}
```

## 2. Composition d'interface

- Dans `Interfaces.go`, définissez une nouvelle interface `Checker` qui implémente la méthode Check().

```go
type Checker interface {
    Check() bool
}
```

- Implémentez l'interface `Check` pour votre type `Human`. Elle return le champ `ready` d'un `Human`.

```go
func (h *Human) Check() bool
```

>

- Créez une fonction `CheckMissionPart` appelle `Check()` sur chaque argument.

```go
func CheckMissionPart(objs ...Checker) bool
```

- Dans `Interfaces.go`, définissez une nouvelle interface `PrepareChecker` qui sera composée de`Preparer` et `Checker`.

```go
type PrepareChecker interface {
    Preparer
    Checker
}
```

- Créez une fonction `PrepareAndCheckMissionPart`. Elle appelle Prepare() et Check() sur chaque argument.

```go
func PrepareAndCheckMissionPart(objs ...PrepareChecker) bool
```

> Si une erreur survient pendant l'exécution de votre fonction, renvoyez cette erreur.

> Si l'un de vos objet n'est pas prêt, renvoyez une erreur (ex: `Jason, 25 years old from USA is not ready!`)

### **FAIRE DES TESTS**
### **Ressources :**

- [embedding](https://golang.org/doc/effective_go.html#embedding)
- [Variadic Arguments](https://gobyexample.com/variadic-functions)
- [fmt.Errorf()](https://golang.org/pkg/fmt/#Errorf)


# 7 - Un équipage pour des missions

Maintenant que vous avez vos pilotes, vous devez accueillir des passagers pour leur faire quitter la Terre.

- Dans Passenger.go, créez un type `Passenger` qui est une redéfinition du type `Human`

```go
package humanity

type Passenger Human
```

- Implémentez les interfaces `Stringer`, `Preparer` et `Checker` qui seront les mêmes que celles des Humains.

- Définissez une structure `Mission` contenant les champs `Pilots` & `Passengers`.

- Créez une méthode `getCrew()` qui renvoie une liste de `PrepareChecker` composée de la liste des `Pilots` et des `Passengers`.

Avant de lancer votre mission, vous devez préparer votre équipage, et vérifier si chaque membre de votre équipage est prêt.

- Implémentez l'interface `Preparer` sur votre type `Mission` qui méthode `getCrew()` et de la fonction variadique `PrepareMissionPart`.

- Implémentez l'interface `Checker` sur votre type `Mission` qui méthode `getCrew()` et de la fonction variadique `CheckMissionPart`.

- Si vous avez compris le principe des arguments variadiques, vous êtes dorénavant capable de préparer et vérifier l'ensemble de votre mission avec un seul appel de fonction.

> Vous pouvez dorénavant rajouter à votre type Mission autant de type que vous voulez, il suffira juste d'implémenter l'interface `PrepareChecker` sur ce type et/ou de modifier la méthode `getCrew`.

> Exemple: Technicians, Scientists, ...

# 8 - Préparer votre mission


## 1. L'API

Vous vous souvenez de la liste de Pilot sous format JSON que l'ASI vous fourni ? Eh bien l'ASI a mis à disposition
une API que vous allez devoir interroger pour composer l'équipage de vos missions.

- Dans un fichier `api.go`, créez une fonction `MakeGetRequestAndGetBody()`.
  Comme son nom l'indique, elle va faire une requête **GET** sur son paramètre.
  Elle renvoie le body de la réponse en cas de succès.

```go
package data

func MakeGetRequestAndGetBody(url string) (io.ReadCloser, error)
```

> [http package](https://golang.org/pkg/net/http/)

## 2. Destination Finale

Pour envoyer votre mission dans l'espace, vous devez maintenant avoir une destination.

- Ajoutez une string `Destination` à votre type Mission

- Créez une méthode `fetchDestination()`, elle **GET** `51.158.67.226:7000/getDestination`

  > En cas de succès, une string correspondant à la destination est renvoyée dans le body de la réponse.

Modifiez la méthode `Prepare()` de votre type `Mission` pour qu'elle appelle aussi la méthode `fetchDestination()` et qu'elle stocke la destination reçue.

## 3. Votre Équipage

- Créez une méthode `fetchPassengers()`, elle **GET** `51.158.67.226:7000/getPassengers`

  > En cas de succès, une liste de `Passenger` est renvoyée sous format JSON dans le body de la réponse.

Modifiez la méthode `Prepare()` de votre type `Mission` pour qu'elle appelle aussi la méthode `fetchPassengers()`.

- Créez une méthode `fetchPilots()`, elle **GET** `51.158.67.226:7000/getPassengers`

  > En cas de succès, une liste de `Pilot` est renvoyée sous format JSON dans le body de la réponse.

Modifiez la méthode `Prepare()` de votre type `Mission` pour qu'elle appelle aussi la méthode `fetchPilots()`.

> :warning: Souvenez vous de l'exercice 2 !

### **Ressources :**

- [http](https://golang.org/pkg/net/http/)


# 9 - Functions are citizen too

[First class citizen](https://en.wikipedia.org/wiki/First-class_citizen)

## 1. Closure

[Closure (GoTour)](https://tour.golang.org/moretypes/25)

```go
func StartTimer(name string) func() {
	t := time.Now()
	log.Println(name, "started")
	return func() {
		d := time.Since(t)
		log.Println(name, "took", d)
	}
}
```

- Dans `Human.go`, créez une fonction `isCsvOK()`.

```go
func isCvsOK(csv []string) error
```

- Revenez sur votre fonction `LineToCSV`, modifiez votre fonction pour qu'elle prenne
  un second argument: `validator func([]string) error`.
- Modifiez vos tests et essayer d'autres formats de csv et validator.

## 2. Higher-Order Functions

L'objectif de cet exercice est de découvrir le principe des `higher-order functions`. Ce concept est utilisé en Go
et dans de nombreux autres langages. Une fonction est dite `higher-order` lorsque elle prend en paramètre
une autre fonction ou lorsque elle renvoie une nouvelle fonction, appelé `callback`. Par ailleurs, ces fonctions
sont souvent utilisées avec des closures.

Dans cet exercice, nous allons nous intéresser aux fonctions passées en paramètre.
Pour cela, dans un fichier `func.go` dans le package `data`  vous allez implémenter 4 fonctions de manipulation de tableau : `filter`, `map`, `reduce`, `sort`.

### 1. Filter

`Filter` va créer un tableau d'int à partir d'un autre en fonction d'un `callback` qui prend un int et renvoie un bool,
aka un `predicate`.

Exemple:
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

> On passe `isEven` à `filter` afin d'avoir uniquement les nombres pairs de `numbers`.

### 2. Map

`Map` va créer un nouveau tableau d'int en appliquant un `callback` à tout les éléments d'un autre tableau.

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

> On passe `abs` à `filter` afin d'obtenir un tableau contenant uniquement des valeurs postives.

### 3. Reduce

`Reduce` va "compresser" un tableau dans un accumulateur (une variable du type que contient le tableau)
via un `callback`. Elle renvoie l'accumulateur.

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

> On utilise `reduce` afin de calculer la somme d'un tableau de nombres.

### 4. Sort

`Sort` va trier un tableau d'int à l'aide d'un `callback` permettant de comparer 2 int. Si le callback renvoie `true`,
swappez les deux éléments.

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

> On se sert de `sort` afin de trier un tableau de façon croissante puis de façon décroissante.
>
> Il n'est pas nécessaire d'implémenter un algorithme performant.

> Map, Filter & Reduce sont plus typiquement des fonctions utilisées dans un [code fonctionnel](https://en.wikipedia.org/wiki/Functional_programming),
> et donc peu (voir pas) utilisées en Go.

# 10 - Concurrency

Votre objectif dans cet exercice est d'optimiser vos temps de calcul grace a l'asynchrone.
Prenez 10 minutes pour retourner sur la partie du [go tour](https://tour.golang.org/concurrency) dediée à la concurency

Voici un code en go, son temps d'éxecution est d'environ 4.5 secondes si on lui donne `0` en entree,

- Dans un fichier `concurrency.go`, modifiez `Calcul` pour avoir un temps d'execution inférieur à 2 seconde.

```go
package data

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

> Il vous est conseillé d'utiliser la fonction `startTimer` vue à l'exercice précédent.

> Il existe beaucoup de doc utile sur la concurrency en ligne : [jetez y un oeil](https://devhints.io/go#Concurrency).


---
> Une dernière fois, ne faites jamais des packages comme `data`.

# 11 - Concurrency v2

> Pour se casser la tête.

Dans cet exercice, vous allez devoir créer une fonction qui :
* prends un path vers json en argument
* récursivement, et de manière asynchrone passe dans toutes les branches du json
* le programme doit ressortir la somme de tout les floats qui se trouve dans le json avec le moins de temps d'execution possible

Attention, vous savez gérer des erreurs, votre fonction ne doit pas crash et doit ressortir des une erreur claire si besoin
On vous donne unn petit json de test pour celui-ci
> 1.2 + 1.23 + 1.3 + 1 + 2 + 3 + 10 + 12 + 12 + 1 + 11
>
> 55.730000000000004

(l'utilisation de float64 ajoute une petite incertitude)

