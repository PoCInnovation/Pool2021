# Bienvenue dans le module *Neural Network From Scratch* alias *NNFS* du programme *Far From Earth*
```
     
                                           ..,,;;;;;;,,,,
                                     .,;'';;,..,;;;,,,,,.''';;,..
                                  ,,''                    '';;;;,;''
                                 ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
                                ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
                                   ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
                                  ;;@@@@@@;           , ';;;@@@@@@@@;;;.
                                   '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
                                      .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
                                        ''..,,     ''''    '  .,;'
                                             ''''''::''''''''
                                                                 ,;
                                {Module NNFS}                   .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [02/02/2021]
```

---

Bonjour l’équipe technique, nous sommes fiers de vous ! Après avoir réussi avec succès la création d’un Neurone ainsi que deux missions associées, vous avez l'étoffe d’accomplir des missions plus importantes. Vous avez acquis la base du Deep-Learning, et nous allons maintenant découvrir ce qui en fait un outil si puissant, j’ai nommé : les réseaux de neurones artificiels ! 

Un neurone tout seul n'est capable que de résoudre des problèmes assez simples. Cependant si on rassemble plusieurs neurones on peut résoudre des problèmes extrêmement complexes. 

N’oublions pas notre objectif, nous avons un an pour redresser l'écosystème de la terre et nous avançons dans l’ombre, l'imprévu est partout. Nous avons donc besoin d’un module pouvant gérer des réseaux de neurones pour pouvoir gérer des problèmes plus complexes. Nous comptons sur vous pour la création de ce module NNFS ! 

 

# Création du Module NNFS V1 

--- 

## Consigne : 

Référez-vous au fichier nnfs_ones.py 

> Dans le dossier eval vous pouvez trouver les détails des tests que nous lançons pour évaler votre avancement. 
> 
> Comme vous l’avez vu dans le talk, les réseaux de neurones fonctionnent avec des Layer (des couches).  Chaque Layer contient un ou plusieurs neurones et chaque Layer est relié au suivant.
> La méthode pour entraîner un réseau de neurones est semblable à celle pour entraîner un seul neurone, mais cette fois-ci nous allons devoir gérer un peu plus de logique pour calculer les gradients de chaque Layer et non pas d’un seul neurone. Cela peut vous paraître compliqué, mais l’équipe scientifique n’est pas bien loin ! Vous pouvez poser des questions ou demander des indices. 

> Un Layer peut être une couche de neurones (le layer Dense par exemple) mais il peut également être une étape de transformation, un Layer de transformation entre deux Layers de neurone par exemple. Voyez-vous de quoi je parle ? Et oui, je parle des fonctions d’activation, qui peuvent également être des Layers. Il existe plusieurs fonctions d’activation (sigmoïde, tanh, relu …) et nous implémenterons celles dont nous avons besoin. 

---- 

* Nous avons besoin de ce qu’on appelle une interface appelée `Layer`. Une interface est une classe mère. Nous pourrons créer des sous-classes à partir de celle-ci. Vous devez donc créer une interface appelée `Layer` que nous utiliserons ensuite comme classe mère pour nos Layers. Chaque Layer possède une fonction `forward()` qui prend en paramètre des inputs et qui renvoit un résultat. Ainsi qu’une fonction `backward()` qui prend en paramètre des inputs et des gradients (venant de la couche précédente). La classe `Layer` mère sera considérée comme la Layer d’activation linéaire. Implémentez les fonctions `forward()` et `backward()` de la classe mère `Layer`. 

> Souvenez vous de l’activation linéaire que vous avez utilisé dans le module NFS. Elle comprenait une fonction `forward()` et une fonction `backward()` (la dérivée) ? Et bien maintenant, il faut créer cette classe mère `Layer` qui contiendra la fonction `forward()` et `backward()` de l’activation linéaire. 

--- 

### Maintenant que nous avons une interface `Layer` nous allons implémenter de nouvelles Layers qui se basent su cette classe mère. 

*  Commençons par le Layer le plus important, le Layer `Dense`. Le Layer `Dense` est le Layer qui va contenir une couche complète de neurones. C’est comme quand vous aviez un seul neurone, mais cette fois-ci vous avez tout une rangée de neurones. Vous pourrez définir combien de neurones vous voulez pour chaque Layer `Dense`. La classe `Dense` hérite de `Layer`, c'est-à-dire qu'elle possède toutes les fonctionnalités de la classe `Layer`, mais en rajoute ou en remplace certaines. Vous devez maintenant créer cette classe `Dense`.

* Tout d'abord, vous devez implémenter le constructeur qui prend en paramètre le nombre d'entrées et le nombre de neurones que la couche va contenir. Le nombre de neurones correspond également au nombre de sorties du Layer (s'il y a 2 neurones, il y aura 2 sorties). Le constructeur prend aussi un troisième paramètre, le Learning-Rate, pour ajuster les gradients.

* En parlant des gradients, vous devez créer deux variables de classe : une pour les poids *W* et une pour le biais *b*, qui doivent être initialisées avec des valeurs aléatoires. Profitez-en également pour stocker le learning rate dans une autre variable de classe.

* Ensuite, vous devez implémenter les fonctions `forward()` et `backward()` de cette classe. Elles prennent les mêmes paramètres que la classe mère `Layer`. La fonction `backward()` reçoit en paramètre les gradients de la couche précédente, vous n’avez donc pas besoin d'appliquer une règle chaînée complète.  

> La fonction `backward()` doit renvoyer les gradients de la couche pour que la couche suivante puisse les recevoir en paramètre de sa propre fonction `backward()`. 

--- 

Maintenant que nous avons le Layer `Dense`, il nous manque les fonctions d’erreur (les Loss). Vous vous en souvenez ? Oui évidemment puisque vous avez attentivement écouté le Talk. Nous allons donc créer une deuxième classe mère `Loss` qui va nous servir de base, puis nous créerons des sous-classes avec les différentes fonctions d’erreur existantes. 

* Vous allez maintenant créer la classe `MeanSquaredError`, qui hérite de la classe mère `Loss`. Comme nous l’avons vu la classe mère `Loss` possède des fonctions `forward()` et `backward()`. Vous devez donc implémenter les fonctions `forward()` et `backward()` de la classe `MeanSquaredError`. La fonction `forward()` renvoit l’erreur tandis que la `backward()` renvoit la dérivée de la Mean Squared Error par rapport aux logits (les prédictions).

--- 

### Nous allons maintenant nous attaquer à la classe `Model`, qui va s’occuper de la liaison et de la logique entre toutes nos Layer, et va nous permettre de les entraîner.

> Actuellement, nous avons un Layer `Dense` et une Loss `MeanSquaredError`. Nous pouvons donc enchaîner plusieurs Layers `Dense` pour faire un réseau de neurones. Cependent il va falloir appeler les `forward()` et les `backward()` en cascade de toutes les Layers pour récupérer les gradients de chaque Layer, et ainsi ajuster les paramètres de chaque layer en fonction de l’erreur totale du modèle.

 
+ Commençons par créer une classe `Model` avec un constructeur prenant en paramètre une instance de la classe `Loss`. N'oubliez pas que la classe `Loss` est une classe mère, donc ce paramètre peut prendre n’importe quelle classe héritant de `Loss`. Nous stockons l’instance de la classe `Loss` dans une variable membre pour pouvoir l'utiliser plus tard. Le constructeur doit également créer une liste vide `network`, qui va nous permettre de stocker les Layers. Cette liste représente globalement notre réseau de Neurones.

+ Vous devez ensuite créer une fontion `add()` dans la classe `Model` qui va prendre en paramètre une instance de la classe `Layer` et va l’ajouter à la fin de la liste `network`.

+ Vous commencez sûrement à voir ou nous allons en venir. Créez ensuite une fonction `forward()` dans la classe `Model`, qui va appeler en cascade les fonctions `forward()` de toutes les Layers stockées dans `network`, et stocker chaque valeur de retour dans un tableau `activations`. La fonction `forward()` doit renvoyer ce tableau `activations`.

> La valeur de retour d’un Layer est l’entrée du suivant. 

+ Nous arrivons à la fonction qui va permettre de faire l’entraînement de tous les Layers. Créez une fonction `train()` dans la classe `Model` qui prend en paramètre les inputs et les targets (les valeurs attendues), et va lancer la fonction `forward()` que vous venez de créer pour récupérer les activations (n'oubliez pas les inputs principaux). Calculez ensuite la Loss et son gradient grâce à l’instance de `Loss` ainsi que ses fonctions `backward()` et `forward()`. Vous aurez sûrement besoin des prédictions de la dernière Layer du modèle pour cela. 

+ Ensuite, vous allez parcourir votre `network` pour appeler la fonction `backward()` de chaque Layer en cascade. Cette étape est subtile, réfléchissez bien et posez des questions si nécessaire.  

+ La fonction `train()` renvoie finalement la moyenne de l’erreur, soit la moyenne de la Loss.

---  

### Vous avez fait le plus dur bravo ! Maintenant, il nous reste une fonction importante à implémenter, et quelques-unes dites de “Pré-process de data”.  

+ Implémentons la fonction `fit()` (toujours dans la classe `Model`). Cette fonction prend en paramètre les inputs et les targets et va les découper sous forme de mini batch pour les passer à la fonction `train()`. N’oubliez pas de faire une boucle pour les époques et ajoutez un peu de visuel avec matplotlib.

+ Pour finir, reprenez vos données des missions précédentes pour tester votre Module NNFS.  

Vous pouvez être fiers de vous et nous le sommes également. Vous venez de créer un framework de Deep learning à partir de rien ! Vous avez acquis énormément de connaissances. Nous allons toutefois ajouter quelques petits utilitaires à ce module NNFS, et vous serez enfin prêts à résoudre des missions plus complexes. 

# Création du Module NNFS V2 

--- 

## Consigne : 

Référez-vous au fichier `nnfs_two.py`

> Pas de panique vous avez fait le corps du module. Maintenant nous allons simplement rajouter des fonctions d’activation et d’erreur qui vont vous permettre d'avoir de meilleurs résultats sur certaines missions. 

+ Créez une classe `Sigmoid` qui hérite de `Layer` et implémentez les fonctions `forward()` et `backward()`.

+ Créez une classe `ReLU` qui hérite de `Layer` et implémentez les fonctions `forward()` et `backward()`.

+ Créez une classe `Softmax_Cross_entropy_with_logits` qui hérite de `Loss` et implémentez les fonctions `forward()` et `backward()`.

Bravo ! Vous avez fini, mais nous pourrons toujours rajouter de nouvelles Loss et de nouveaux Layers à la façon de "plugins" au cours des missions.

 
