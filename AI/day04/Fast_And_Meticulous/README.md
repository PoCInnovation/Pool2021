# AI Pool 2021 - Reinforcement Learning - Q-learning


#### Félicitations membre de l'IT team, vos efforts ont payés !<br> Votre derniere intervention nous a permit de sauver de nombreuses vie, vous pouvez être fière de vous.<br>

#### Malheuresement nous n'avons pas le temps de célebrer plus longtemps cette réussite.<br> L'équipe scientifique viens de detecter une potentiel menace non loin de là. Nous n'avons pas plus de details pour l'instant.

#### Votre mission est de consevoir et envoyer un vehicule autonome à la recheche de cette menace.<br>Une fois celle-ci localisé faite nous un compte rendu détaillé de cette derniere.


#### Pour vous aider dans cette mission, l'equipe scientifique a élaboré une methode pour automatiser le deplacement de votre vehicule.<br>Ils l'ont nommé: <ins>*Q-learning*</ins>.

#### Le principe est simple, uttiliser l'équation de Bellman pour rediger un tableau detaillé des differents stats et rewards possible pour optimiser les actions de votre agent.

#### Nous vous avons rediger un manuel d'uttilisation pour simplifier sa mise en place.

## Manuel du Q-learning:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686">

**Avant de regarder comment se déroule l'algorithme du Qlearning, commençons par definir la nomenclature:**

- **α** (alpha): alpha est le learning rate, c'est l'importance que l'on donne au new stat. <br>Sachant 0 < α < 1, plus de learling rate est élevé, plus on donne de l'importance au new stat.
- **γ** (gamma): gamma est le discount factor, c'est l'importance donné à un futur reward. <br>Sachant 0 < γ < 1, plus le discount factor est élevé, plus notre agent "pensera" au long terme.

<br>
**Ceci étant fait, passons au fonctionnement du Qlearning:**

Avant de commencer, la Q-table est definit arbitrairement à une valeur choisit.<br>
Maintenant à chaque etape ***e***, l'agent choisit une action ***<span style="font-size:larger;">a</span>e***, observe un reward ***<span style="font-size:larger;">r</span></span><span style="font-size:smaller;">e</span>****** et entre dans un new stat ***<span style="font-size:larger;">S</span><span style="font-size:smaller;">e+1</span>***.
<br>On update alors la Q-table de la façon suivante: <ins>Q[***<span style="font-size:larger;">S</span><span style="font-size:smaller;">e</span>***, ***<span style="font-size:larger;">a</span>e***] = Q[***<span style="font-size:larger;">S</span><span style="font-size:smaller;">e</span>***, ***<span style="font-size:larger;">a</span>e***] + **α** * (***<span style="font-size:larger;">r</span></span><span style="font-size:smaller;">e</span>*** + **γ** * max(Q***<span style="font-size:larger;">S</span><span style="font-size:smaller;">e+1</span>***, ***<span style="font-size:larger;">a</span>*** - Q[***<span style="font-size:larger;">S</span><span style="font-size:smaller;">e</span>***, ***<span style="font-size:larger;">a</span>e***])</ins>.


## Description de l'env:

Here is few things you need to know about the BlobEnv:

*   Pour éffectuer une action: ``BlobEnv().doAction(action: int) -> obs: [(int, int), (int, int)], new_obs: [(int, int), (int, int)], action_reward: int``
*   Pour recupérer l'état actuel de l'env: ``BlobEnv().show()``
*   Pour recupérer l'observation: ``BlobEnv().getObs() -> obs: [(int, int), (int, int)]``
*   Pour réinitialiser l'env: ``BlobEnv().reset()``
*   Qu'est ce ``obs``: C'est l'observation de l'environement avant l'action
*   Qu'est ce ``new_obs``: C'est l'observation de l'environement apres l'action
*   Qu'est ce ``action_reward``: C'est le reward obtenue par l'action

## Consignes:

Completez le code fournit par l'équipe scientifique *(submit.py)* en uttilisant le Q-learning.
<br>Votre agent doit obtenir une moyenne minimum de reward superieur ou egal à -60.

Une fois sela fait, soumetez votre code sur la plateforme.



## Quelques liens utils:
*   Qu'est ce que ``pickle``: https://docs.python.org/3/library/pickle.html
*   Qu'est ce que ``matplot``: https://matplotlib.org/
*   Qu'est ce que le ``Q Learning``: https://youtu.be/qhRNvCVVJaA
