 # Bienvenue dans le module *Defense Advanced* du programme *Far From Earth*
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
                                {Module Defense Advanced}                .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [05/02/2021]
```

--- 
 
 
Bonjour l'équipe technique ! Nous voilà à présent dans la dernière mission ! L'Equipe PoC souhaite vous remercier fortement pour votre courage et votre motivation ! La plupart des problèmes terrestres ont été résolus. Nous avons détecté que la plupart de ces soucis avaient été causés par des OVNIs. Nous avons donc prévu de créer un module de défense Advanced qui va s'occuper de tirer sur les vaisseaux extraterrestres qui pourraient essayer d'envahir la Terre.  
>  * Vous avez récemment utilisé la technique de *policy gradient* et l'avez testée sur *Cartpole*. Nous allons maintenant l'améliorer avec ce qu'on appelle *l'Actor-Critic* policy based qui est un mixte entre *value-based* et *policy based*.   
> * Pour faire simple nous allons avoir deux prédictions faites par notre réseau de neurones. La prédiction faite par *policy gradient* et aussi la valeur de l'état actuel :  *V(s)*.   
> * Nous allons ensuite calculer l'erreur pour *V(s)* en comparant *V(s)* avec les *qvals*. La prochaine étape consistera à calculer l'erreur pour la sortie *policy gradient* du neurone en multipliant le logarithme de la probabilité par ce qu'on appelle *l'avantage* `(qvals - V(s))`. Nous allons ensuite additionner les deux erreurs et optimiser notre réseau de neurone en minimisant cette erreur.  
Vous allez commencer par résoudre l'environnement GYM « Cartpole » grâce à la méthode de Reinforcement Learning **Actor Critic**, puis vous allez résoudre **Assault-ram-v0** qui est un jeu d'arcade ou l'on tire sur des vaisseaux spatiaux.  
## Voici quelques directives :   
- Vous devez avoir un réseau de neurones avec des couches denses et linéaires. Il prédira la meilleure action à prendre parmi la liste des actions possibles. Il renvoie donc un `softmax` mais également la valeur de l'état `V(s)` qui est simplement le retour d'un layer `linear` ce V(s) va représenter la valeur `critic` tandis que la sortie du *policy gradient* sera *l'actor*. (Regardez comment fonctionne un environnement gym et comment vous pouvez récupérer le nombre d'actions possibles et la shape des inputs).   
- Vous devez également avoir une classe `Memory` comme dans les exercices de Reinforcement Learning précédents pour stocker des `Transitions`et des `SavedAction`. La classe `Memory` doit pouvoir stocker et récupérer des `Transitions`/`SavedAction`, ainsi que pouvoir être vidée.  
- Vous devez ensuite créer une classe `Agent` qui va représenter notre agent :   
- Un agent possède une mémoire et doit pouvoir prendre des actions. Il contient donc une instance de la classe mémoire et de la classe réseau de neurone.   
- Pour prendre des actions, cet agent doit implémenter une fonction `take_action()`, qui va utiliser la technique de *Policy Gradient* pour choisir une action grâce à son réseau de neurones, qui prend en entrée l'état actuel de l'agent. Cette fonction return l'action à prendre ainsi qu'un tuple représentant le `(log_prob, V(s))`  qui sont les deux valeurs que votre réseau de neurones retourne.   
- Vous devez ensuite calculer les `qvals` comme dans *policy gradient* de la mission précédente. Cela va servir pour calculer l'erreur de `V(s)` (value loss) mais également pour calculer *l'avantage* `(qvals - V(s))` qui va servir pour calculer l'erreur *policy gradient* du réseau de neurones.  
  
  
### Maintenant que vous avez toutes les fonctions utilitaires, il vous faut maintenant les assembler pour créer la fonction d'apprentissage `learn()` :   
- Cette fonction récupère toutes les transitions de l'épisode soit ` n * ('state', 'action', 'next_state', 'reward')`, mais également les `SavedActions `'log_prob', 'value'`. Ensuite elle calcule les `Qvals` de chaque transition grâce à la fonction que vous avez créé précédemment. Après cela, on applique la technique *Actor Critic*.   
  
  
### Tips :   
- Je n'oublie pas de reset les gradients avec mon optimizer.   
- Je calcule l'avantage qui va me servir pour calculer la `policy gradient loss`.  
- Je calcule la `Value loss` avec la `MSE` et les `Qvals` comme target/labels  
- Je calcule la `policy gradient loss`  ` ( - log_prob * advantage)`  
- J'additionne les deux loss en une seule.  
- J'utilise la fonction `backward()` sur le retour de la somme des loss (pour calculer les gradients). Ensuite j'utilise la fonction `step()` pour appliquer les changements. Suite à cela je `clear()` la mémoire pour dire que l'épisode est terminé et que l'on passe au suivant.  
  
  
### Il faut maintenant créer un `main()` pour créer un agent et tout ce dont il a besoin pour apprendre :   
- Tout d'abord récupérez l'environnement GYM.  
- Créez une instance de votre réseau de neurones, qui prend en paramètre la shape d'entrée et de sortie de l'environnement.   
- Créez un optimizer.   
- Créez un agent avec l'optimizer et le réseau de neurone.  
- Maintenant faites une boucle sur le nombre d'épisodes que vous voulez faire, et dans chaque épisode faites progresser votre agent jusqu'à un nombre d'étapes maximum, ou jusqu'à ce que l'environnement vous renvoi 'DONE'.  
- À chaque étape de l'épisode, récupérez l'état de l'environnement et donnez-le à la fonction `take_action()` de l'agent. Celui-ci renvoi l'action à prendre, que vous passez ensuite à la fonction `step()` de l'environnement. (N'oubliez pas de récupérer les `SavedAction` qu'il faudra push dans la mémoire. Cela est utile pour la fonction `learn()`).  
- La fonction take_action renvoie aussi le `namedtuple` `savedAction` que vous devez aussi stocker dans la mémoire pour l'entrainement.  
- La fonction `step()` vous renvoit `new_state, reward, done`. Stockez toutes les `Transitions` et les `SavedAction` dans la mémoire pour qu'à la fin de l'épisode, l'agent puisse les utiliser pour apprendre.  
- Une fois qu'un épisode est terminé, appelez la fonction `learn()` de l'agent. N'oubliez pas de `clear()` la mémoire pour le prochain épisode.   
Tentez maintenant de faire réussir l'env GYM **Assault-ram-v0** à votre agent. 
 
