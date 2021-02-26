 # Bienvenue dans le module *Defense* du programe *Far From Earth*
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
                                {Module Defense}                .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [04/02/2021]
```

--- 
 
 
Bonjour l'équipe technique ! Je suis heureux de vous voir toujours d'aplomb ! Vous venez de faire vos premiers pas dans le monde du Reinforcement Learning, un domaine de l'IA souvent utilisé dans la robotique et les jeux vidéo ! 
 
 
Le Reinforcement Learning est souvent découpé en deux types d'algorithmes : Value Based et Policy Based. Vous venez de voir le Q Learning et le Deep Q Learning qui sont des algorithmes « Value Based ». Maintenant vous allez voir certains algorithmes « Policy Based ». 
 
 
Les deux types ont leurs avantages et leurs inconvénients, et dans certains algorithmes on peut même mixer les deux pour croiser les prédictions et créer des algorithmes capables d'évoluer dans des environnements extrêmement complexes ! 
 
 
C'est pourquoi vous aller devoir maîtriser les deux types de Reinforcement Learning.
Grâce a ces nouvelles compétences, vous allez pouvoir résoudre de nouvelles missions et agrandir votre bagage de connaissances en intelligence artificielle. 
 
Le premier algorithme « Policy Based » que vous allez voir s’appelle Policy Gradient. À la différence du Deep Q Learning Policy Gradient est capable de gérer des actions continues. Autrement dit, il peut par exemple choisir précisément l'angle du volant en conduisant une voiture. Je vous invite à chercher la différence entre une action continue et une action discrète pour comprendre cette nuance.

Cependant, Policy gradient est également capable de gérer des actions discrètes. C’est ce par quoi nous allons commencer, car gérer des actions discrètes est bien plus simple que des actions continues.
---
### Les méthodes  « Policy Based » peuvent résoudre des problèmes que les méthodes  « Value Based »  ne peuvent pas:  
* Elles peuvent par exemple gérer des actions continues, et donc avoir plus de choix possibles et plus de contrôle qu'un simple choix parmis une liste d'actions.
* Les méthodes « Policy Based » sont plus efficaces dans des environnements stochastiques [(cf: Explications)](https://www.freecodecamp.org/news/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f/). Autrement dit, ce sont des environnements dans lesquels effectuer deux fois la même action n'a pas 100% de chances d'aboutir au même resultat.

### Cependant, les méthodes « Value Based » comme le Q-learning présentent également des avantages:
* Ces méthodes on une convergence plus rapide, c'est-à-dire que le modèle apprend plus vite car on minimise la fonction de loss plus rapidement.
* Elles convergent mieux. Autrement dit elle ne tombe pas dans des mimimun locaux. Dans une fonction d'erreur, il y a souvent de nombreux minimun locaux, mais un seul minimum global. Les méthodes « Policy Based » tombent plus facilement des minimums locaux, et peuvent donc stagner dans leur apprentissage si on ne prend pas de mesures pour contrer ce phénomène.
* Les méthodes « Value Based » sont plus simples à comprendre et à expliquer, puisqu'on peut directement représenter la Q-table comme un tableau a plusieurs dimensions dans lequel nous mettons les états, les actions et les récompence attendues.

---
 
Avant de rentrer dans le vif du sujet, nous allons aborder un principe important dans la création d'algorithmes et d’IA en général. Lorsque vous voulez résoudre un problème complexe, il vaut mieux d’abord tester votre algorithme sur un problème classique et simple pour s'assurer qu'il fonctionne C'est seulement une fois que vous êtes certains que votre algorithme fonctionne sur un problème basique que vous pourrez commencer à le tester sur des problèmes plus complexes. 
 
 
Vous avez vu dernièrement l'environnement GYM « Cartpole » : c’est un environnement basique qui va justement vous permettre de tester vos IA de Reinforcement Learning. 
 
 
Vous devez donc résoudre l'environnement GYM « Cartpole » grâce à la méthode de Reinforcement Learning **Policy Gradient**. 
 
 
## Voici quelques directives :  
 
 
- Vous devez avoir un réseau de neurone avec des couches denses et linéaires, qui prédira la meilleure action à prendre parmi la liste des actions possibles. (Regardez comment fonctionne un environnement gym et comment vous pouvez récupérer le nombre d'actions possibles et la shape des inputs.) 
- Vous devez également avoir une classe `Memory` comme dans les exercices de Reinforcement Learning précédents pour stocker des Transitions. La classe `Memory` doit pouvoir stocker et récupérer des Transitions, ainsi que pouvoir être vidée.
- Vous devez ensuite créer une classe `Agent` qui va représenter notre agent : 
- Un agent possède une mémoire et doit pouvoir prendre des actions. Il contient donc une instance de la classe mémoire et de la classe réseau de neurone. 
- Pour prendre des actions, cet agent doit implémenter une fonction `take_action()`, qui va utiliser la technique de Policy Gradient pour choisir une action grâce à son réseau de neurones, qui prend en entrée l'état actuel de l'agent.
- Si vous avez bien compris la technique de Policy gradient, vous avez vu que l'on calcule ce qu'on appelle les Qval à partir de toutes les récompenses de l'épisode. Vous devez donc faire une fonction qui prend en paramètre les récompenses de l'épisode actuel, puis qui calcule les Qvals de chaque transition en partant de la dernière récompense. Un épisode représente dans cet environnement toutes les actions prise entre le début d'une nouvelle partie, et le moment où l'agent gagne ou perd. Chaque épisode est donc composé de plusieurs transitions. On effectue un grand nombre d'épisodes afin d'entraîner l'agent.

### Maintenant que vous avez toutes les fonctions utilitaires, il vous faut maintenant les assembler pour créer la fonction d'apprentissage `learn()` : 
- Cette fonction récupère toutes les transitions de l'épisod,e soit ` n * ('state', 'action', 'next_state', 'reward')`, mais sous forme de 4 tableaux différents. Ensuite elle calcule les Qvals de chaque transition grâce à la fonction que vous avez créé précédemment, en lui donnant la liste des récompenses de l'épisode. Après cela, on applique la technique de policy gradient.  

### Tips : 
- Je n'oublie pas de reset les gradients avec mon optimizer. 
- Je n'oublie pas d'utiliser un softmax pour avoir une répartition de probabilité (Rechercher a quoi sert un softmax puis appeler un encadrant). 
- Je calcule la loss (la suite de la technique policy gradient) 
- J'utilise la fonction `backward()` sur la loss pour calculer les gradients, puis la fonction `step()` pour appliquer les changements. Suite à cela je `clear()` la mémoire pour dire que l'épisode est terminé et que l'on passe au suivant.

### Il faut maintenant créer un `main()` pour créer un agent et tout ce dont il a besoin pour apprendre : 
- Tout d'abord récupérez l'environnement GYM.
- Créez une instance de votre réseau de neurone, qui prend en paramètre la shape d'entrée et de sortie de l'environnement. 
- Créez un optimizer. 
- Créez un agent avec l'optimizer et le réseau de neurone.
- Maintenant faites une boucles sur le nombre d'épisodes que vous voulez faire, et dans chaque épisode faite progresser votre agent jusqu'à un nombre d'étapes maximum, ou jusqu'à ce que l'environnement vous renvoit 'DONE'.
- À chaque étape de l'épisode, récupérez l'état de l'environnement et donnez le à la fonction `take_action()` de l'agent. Celui-ci renvoit l'action à prendre, que vous passez ensuite à la fonction `step()` de l'environnement, qui vous renvoit `new_state, reward, done`. Stockez toutes les transitions dans la mémoire pour qu'à la fin de l'épisode, l'agent puisse les utiliser pour apprendre.
- Une fois qu'un épisode est terminé, appelez la fonction `learn()` de l'agent. N'oubliez pas de clear la mémoire pour le prochain épisode. 
 
 
Tentez maintenant de faire réussir *Cartpole* à votre agent. Il doit être capable de faire tenir le bâton en l'air pendant 499 itérations/Transitions (ce qui est le maximum). 

---
# À suivre ...

Vous venez de créer votre premier algorithme de Deep Reinforcement Learning (Réseau de neurone + Reinforcement Learning). Dans la prochaine missions, vous allez reprendre les notions de ce module pour créer le module Defense Advanced qui va s'occuper de tirer sur les vaiseaux extraterestre qui pourrait essayer d'envahir la Terre.
