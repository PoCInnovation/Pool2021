# Jour 4 - Kart VR

Au cours de cette journée, vous réaliserez un jeu de course en VR. Vous devrez créer un environnement en VR multijoueur dans lequel vous et vos amis pourrez faire une course.

## Configuration

Il s'agit de la même configuration qu'hier, repassez donc voir le sujet précédent si nécessaire.

## Le jeu

Commencez par créer un personnage auquel vous attacherez une caméra VR.

Il avancera dans la direction ou vous regardez.

Choisissez un thème parmi les packs d'assets fournis. Ouvrez la map de démo, ou faites en une de toute pièce.

Ajoutez des checkpoints, qui peuvent être dans la plus basique des formes des cerceaux, sur le tracé de votre parcours.

Lorsque votre personnage passe au travers de l'un d'entre eux, il doit disparaître.

Pour guider le joueur, vous devrez lui indiquer le nombre de cerceaux restants ainsi que le direction du cerceaux le plus proche de lui, par exemple grâce à une flèche.

Ajoutez des powers-up qui apparaissent à des positions aléatoires sur le parcours qui vous confèrent des bonus : vitesse ou score par exemple.

Faites de même pour les malus, qui vous ralentissent.

Un système de multijoueur serait le bienvenue pour ce jeu de course.

Vous pourrez être jusqu'à 5 dans la même partie avec pour objectif d'être le premier à passer dans tous les cerceaux.

Ajoutez un menu de début et de fin afin de donner un aspect plus pro au jeu.

Au début de chaque course, faire jouer une cinématique. Il s'agira ici d'une caméra libre qui se déplace à certains lieux de votre parcours. Puisqu'il s'agit d'un jeu VR, le joueur doit pouvoir déplacer la vue de la caméra comme bon lui semble.

Ajoutez une identité sonore à votre jeu.

D'une part à l'aide de plusieurs musiques qui doivent s'enchaîner dès que l'une d'entre elle se termine, mais d'autre part grâce à des effets qui se déclenchent tout au long de la partie : bruit de moteurs (ou de sabots si vous avez pris le pack western), indicateurs de passage dans les cerceaux / checkpoints et de collision si vous tamponnez un autre joueur.

Comme tout jeu multijoueur, un classement des scores est nécessaire.

Plusieurs fonctionnalités sont ici demandées :

-   Le tableau de high-score doit s'afficher à l'issue de la partie avec les scores mis-à-jour.

-   Il doit être permanent et s'afficher lors d'un premier démarrage du jeu sur le menu principal.
