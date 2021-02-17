# Bienvenue dans le module *Neuron From Scratch* alias *NFS* du programme *Far From Earth*
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
                                {Module NFS}                    .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [01/02/2021]
```

---

Nous n'arriverons à sauver la terre que si nous travaillons ensemble. Chaque personne ici a son importance et le partage d'idée et de compétence est essentiel. Un homme ne bâtit pas un immeuble tout seul. Cependant si 1 millier de personnes pose une brique la tâche sera réalisée aisément. Telle est notre force. 

  

Dans le but de nous aider nous les hommes, nous avons entrepris de créer différentes IA pour nous assister dans les taches de détection, prévision, simulation et bien d'autres. Pour cela nous avons besoin que l'équipe technique comprenne la base de L'IA j'ai nommé les neurones ! 

  

Le module NFS va vous permettre à travers divers exercices de créer des neurones que nous allons ensuite utiliser pour créer des IA. 

  

Vous avez à votre disposition un sujet et divers markdowns que vous pouvez ouvrir avec un plugin de visualisation markdown sur vs code. Dans ces fichiers .md vous avez des fiches techniques qui vous expliquent certaines notions utiles. Vous avez également des liens web et vous avez également accès à internet et son vaste réseau de connaissances. 

  

--- 

  

# Mini Justi Loss 

Vous avez appris grâce au talk de l'équipe scientifique qu'un neurone n'est qu'une fonction mathématique du type linéaire (f(x) = ax + b). Vous avez également appris que nous calculions l'erreur faite par le neurone grâce à une fonction d'erreur appelée "loss".  

     

Plus la loss est basse plus notre neurone fait de bonne prédiction. Nous avons donc besoin de minimiser la fonction d'erreur loss. Autrement dit quel paramètre de ma fonction puis-je ajuster pour que ma fonction d'erreur me retourne une valeur proche de 0 ?  

     

Pour vous guider vous allez faire un petit exercice dans lequel vous allez minimiser des fonctions plus simples que les "loss". Une fois que vous avez appris à minimiser une fonction lambda, c'est le même principe pour les "loss" 

  

## Consigne : 

Référez-vous au fichier mini_justi_loss.py 

Vous devez créer deux fonctions : 

* une fonction $f2(x) = x^2$ 

* une fonction $f1(x, y) = x^2 + y^2$ 

### Vous allez ensuite devoir minimiser ces deux fonctions pour cela il faudra :            

* Créez une fonction pour calculer la dérivée partielle de f2 par rapport à x ($d_f2_dx$) 

* Créez une fonction pour calculer la dérivée partielle de f1 par rapport à x ($d_f1_dx$) 

* Créez une fonction pour calculer la dérivée partielle de f1 par rapport à y ($d_f1_dy$) 

### Pour tester il nous faut des data, nous allons donc en créer grâce à la fonction linspace de numpy : 

* Créez une fonction qui retourne un array de données x pour la fonction $f2$  

* Créez une fonction qui retourne deux array de donnée x et y pour la fonction $f1$ 

### Une fois cela fait vous avez tous les outils pour minimiser ces deux fonctions : 

* Faire l'étape de pseudo forward pour la fonction $f2$ (calculez $f2(x) = k$). 

* Calculez le gradient de la fonction $f2$ pour le paramètre $x$ 

* Ajustez $x$ avec la technique de descente de gradient  

* Faire l'étape de pseudo forward pour la fonction $f1$ (calculez $f2(x, y) = z$)

* Calculez le gradient de la fonction $f1$ pour le paramètre $x$ 

* Ajustez $x$ avec la technique de descente de gradient 

* Calculez le gradient de la fonction $f1$ pour le paramètre $y$ 

* Ajustez $y$ avec la technique de descente de gradient 

   

# Maxi Neurone  

     

Bravo ! Vous voilà arrivé dans le vif du sujet, nous allons créer notre premier neurone intelligent ! 

Pour cela, nous allons faire les choses bien. Dans cet exercice, vous allez créer une classe "neurone" que vous pourrez réutiliser pour faire des IA. 

  

## Consigne : 

Référez-vous au fichier maxi_neurone.py 

  

> Un "Exemple" représente les données nécessaires pour une seule prédiction. 
> * Dans le cas où nous avons le taux de globule blanc et de globule rouge d'un patient un "Exemple" serait le taux de globule blanc et rouge d'un seul patient. 
> * Dans le cas d'une prédiction à partir d'images un "Exemple" serait une seule image 
> 
> Une IA s'entraîne donc sur plusieurs "Exemples"  
> 
> Les "features" sont les données d'un Exemple. 
> * Dans le cas où nous avons le taux de globule blanc et de globule rouge d'un patient une features serait le taux de globule blanc et l'autre serait le taux de globule rouge. Il y a donc 2 features par Exemple. 
> * Dans le cas d'une prédiction à partir d'images une "feature" serait un pixel d'une image. Les features d'un Exemple serait tous les pixels d'une seule image.  
> 
> Une **époque** représente le passage d'une IA sur l'ensemble du dataset. S'il y a plusieurs epoch, l'IA passe plusieurs fois sur l'ensemble du dataset. 

  

### Nous allons commencer par utiliser un neurone le plus basiquement possible pour pouvoir résoudre des problèmes linéaires (sans fonction d'activation pour casser la linéarité). 

--- 

  

* Commencez par créer une class "Neurone", à laquelle vous ajoutez un constructeur prenant le nombre de features par Exemple. 

* Dans le constructeur créez et initialisez des variables pour les poids $W$ du neurone et le biais $b$ 

* Dans le constructeur créez et initialisez des variables pour les gradients des poids $W$ du neurone et le gradient du biais $b$ 
  
* Créez une fonction resetGrad dans la classe Neurone pour reset les gradients des poids $W$ et du biais $b$ avec leurs valeurs initiales.

<details> 

   <summary> Tips </summary> 

   Faites attentions, on va utiliser des matrices en input que l'on va multiplier avec les poids. 

</details>  

  

<br/> 

  
* Créez une fonction getData() hors de la classe neurone. Celle-ci devra générer des données linéairement espacées. Il nous faut 30 valeurs pour x et 30 valeurs pour y.  

> Cette fonction return x et y sous forme de numpy array 

  

<details> 

   <summary> Tips </summary> 

   np.linspace 

</details>  

  

<br/> 

* Créez une fonction "forward" dans la classe Neurone et implémentez là. (Cette fonction prend un paramètre "input").  

>Cette fonction return le résultat de la forward pass. 

* Créez une fonction linear_activation hors de la classe Neurone qui prend un paramètre input. 
* Créez une fonction d_linear_d_input qui représente la dérivée partielle de la fonction linéaire par rapport aux inputs. 
> Cette fonction prend un params input. 
* Créez une fonction mean_squared_error et implémenté la loss MSE. 
> Cette fonction prend un paramètre, les prédictions du neurone et les targets attendu puis return la moyenne de l'erreur. 

* Créez une fonction "backward" dans la classe Neurone et implémentez là.  

>Cette fonction calcule les gradients des poids $W$ et le gradient du biais $b$ puis les stocks à l'intérieur des variables de classes crée dans le constructeur. 

  

  

<details> 

   <summary> Tips </summary> 

   Utilisez la règle chaînée pour calculer la dérivée partielle de la loss par rapport à tous les poids. Cela vous donnera le calcul du gradient de la loss par rapport aux poids. 

</details>  

  

<br/> 

* Créez un main python dans lequel vous récupérez vos données avec votre fonction getData dans deux variables x et y. 
* Créez une instance de votre classe Neurone en spécifiant la taille des features de vos exemples. 

  

--- 

  

### Vous allez entrainer votre neurone à prédire y à partir de x  

  

* Créez une boucle qui itère sur un nombre d'époques que vous avez définies auparavant. 
* Dans chaque époque itérez sur les x et les y et entraînez votre neurone à partir de ces données.  
> Vous devez implémenter la méthode de descente de gradient. Vous avez normalement tous les outils en mains, c'est juste de l'assemblage. 

Bravo ! Vous avez créé un neurone artificiel. 
