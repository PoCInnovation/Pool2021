# Jour 1 - Découverte du moteur Unity

Tout au long de cette journée, vous allez découvrir les bases nécessaires au développement sur Unity.
Dans un premier temps, vous découvrirez les bases de la modélisation avec la création d’assets.
Vous les utiliserez ensuite dans une scène qui vous servira de plateforme de test pour découvrir les événements ainsi que la physique du moteur.

Vous devrez effectuer les exercices dans l’ordre et dans un seul projet Unity.

## Modélisation

Unity étant composé de plusieurs parties (un moteur physique, de rendu, un ECS) il est en premier lieu nécessaire de comprendre l’interface avec laquelle vous devrez le plus interagir.

Créez un cube. Il va vous servir de base pour la première étape de familiarisation avec Unity : la modélisation.

Modifiez les dimensions de votre cube pour le rendre 10 fois plus petit. Vous devrez être en mesure d’utiliser ce modèle réduit plus tard à de nombreuses reprises, trouvez donc un moyen de rendre cela possible.

Votre troisième tâche est de modéliser (enfin !) deux meubles.
Voici les schémas correspondants à l’etajaren ainsi que l’assoiren.

<div align="center">
  <img src=".github/assets/arvr_1.png" width=50%"/>
</div>

<div align="center">
  <img src=".github/assets/arvr_2.png" width=50%"/>
</div>

## IKEO War

Passons à présent à l’étape de programmation.
Les scripts que vous écrirez tout au long de cette piscine utilisent le langage C#.
Un conseil : la documentation officielle de Unity est très utile.

Commençons simple : vous devez afficher ‘start’ lorsque vous lancez votre jeu et ‘update’ à chaque nouvelle frame dans la console de debug. Profitez-en dès à présent pour vous renseigner sur les étapes de la pipeline de rendu du moteur.

Maintenant lors de chaque input du joueur (par exemple la touche espace) vous devrez faire apparaître un assoirien et un etajaren à des positions aléatoires comprises entre
[0 > x > 10; 0 > y > 10; 0 > z > 10].

Ajoutez un sol à votre scène et ajoutez de la gravité pour faire tomber vos meubles lorsqu'ils apparaissent.

Lorsque le joueur clique sur un des meubles avec sa souris, il doit disparaître. Si vous enlevez le sol, faites en sorte que vos objets précédemment instanciés soient bien supprimés et ne surchargent pas la mémoire de votre moteur et par extension de votre pc.

Ajoutez du mouvement ! Votre caméra est pour le moment statique, alors créez un script qui puisse lui permettre de se déplacer sur l’axe X selon la direction des flèches de votre clavier sur laquelle vous appuyez.
Ajoutez à ce mouvement un effet de latence, de sorte que l’interaction dans la scène soit plus fluide.

Tant que vous travaillez avec la caméra, ajoutez des effets de post-processing à cette dernière :

- Des lens-flare
- Des effets chromatiques 

Ajustez ces effets selon votre préférence.

Dernière tâche : le multijoueur.
Vous l’aurez deviné, le but est ici de rendre tout ce que vous avez accompli jusque’ici accessible à d'autres joueurs.
Vous devez permettre à d’autre joueurs de se connecter à votre scène pour qu’ils puissent :

- Voir votre scène
- Interagir avec vos assets
- Se voir entre eux (avec une capsule ou un pseudo au-dessus de la position de chaque joueur)

