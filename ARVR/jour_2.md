# Jour 2 - Programmation & premier jeu

## Unity Lights

Ce premier exercice a pour but de vous faire découvrir l’ECS de Unity et les notions de base du moteur physique.
Plus particulièrement, vous allez devoir expérimenter avec les options relatives à la physique de l’environnement et des objets.

Vos encadrants vous ont fourni une scène pour cet exercice. Ouvrez là dans un nouveau projet Unity. Votre but est de faire tomber les cubes bleus sur les socles verts. Si tous les cubes tombent, vous aurez réussi !

## PoC Coin

Cet exercice a pour but de vous faire réaliser un jeu à l’aide des compétences acquises jusqu’ici. Le but du jeu est simple : ramasser le plus de pièces dans un temps imparti.

Créez un terrain parsemé d’obstacles. Si le game design n’est pas votre fort, vos encadrants pourront vous donner une scène pré-faite.

Vous devez être en mesure de pouvoir contrôler un personnage dans les 4 directions mais également sur les 4 diagonales.

Maintenant que vous pouvez vous déplacer, faites de même pour la caméra : votre souris doit être le contrôleur de cette dernière.

Ajoutez des spawns à différents lieux de votre scène accessible par votre personnage. De simples Game Objects feront l’affaire pour le moment. Lors du démarrage du jeu, des prefabs de pièces doivent apparaître à l’emplacement des spawns.

Votre personnage doit pouvoir récupérer les pièces. Attention, si plus aucune pièce n’est disponible, elles doivent apparaître automatiquement de nouveau.

Une contrainte supplémentaire : il ne peut y avoir que 3 pièces en simultané sur la scène.

Une interface serait la bienvenue non ? Ajoutez une barre de score, ainsi qu’un chronomètre. Si ce dernier atteint 0, la partie s’arrête et vous redirige vers un menu qui vous propose deux choix : quitter ou jouer. Il doit également apparaître lors du lancement du jeu.

Ajoutez un thème et un peu de vie à votre jeu.
Commencez par créer et déclencher des animations à plusieurs de vos objets (pièces et joueurs). Puis, jouez avec la verticalité du niveau : ajoutez des plateformes avec des mouvements répétitifs permettant au joueur de prendre de la hauteur.

Plusieurs thèmes sont à votre disposition, de Far West jusqu’à Cyberpunk ! Utilisez celle de votre choix pour votre jeu.

Pour finir, ajoutez des effets sonores (qui se déclenchent lors d'événements particuliers ou lorsque le personnage marche) ainsi qu’une musique d’ambiance.
