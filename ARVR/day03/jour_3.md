# Jour 3 - Arizona VR

Tout au long de cette journée, vous allez réaliser votre premier projet VR : un jeu similaire à Arizona Sunshine.

Vous découvrirez les outils impliqués dans le développement de jeux et d'applications VR.

## Préparation de Unity

Une première partie de setup est nécessaire pour vous permettre de faire tourner votre jeu en VR. Suivez attentivement chaque étape de cette partie et appelez un de vos encadrant au moindre doute.

Créez un nouveau projet. Assurez-vous bien d'avoir au préalable installé les modules de compilation pour les plateformes Android et IOS.

Dans Unity, ouvrez [Window]->[Package Manager].

Cliquez sur le [+] puis sur [Add Package From git Url] et collez cet url :

<https://github.com/googlevr/cardboard-xr-plugin.git>

Importez le dossier Arizona Empty dans votre projet Unity.

Dans [File]->[Build settings], choisissez comme plateforme de build Android. Confirmez votre choix en appuyant sur Switch Platform. Cliquez sur Open Scenes et sélectionnez HomeLand.

Dans [Project Settings]->[Player]->[Resolution and Presentation] mettez à jour l'option Default orientation à Landscape left.

Cliquez sur le menu Other Settings.

Dans la partie Graphics API, ne mettre que l'option OpenGL ES2 active.

Dans la partie Scripting Backend, sélectionnez IL2CPP.

Dans la partie Target Architectures cochez ARMv7 et ARM64.

Dans la partie Internet Access, passez l'option à required.

Dans la partie Package Name, mettez PoCVR.

Dans la partie API Target Level, renseignez la version d'Android de votre appareil.

Dans la section Build, cochez Custom Main Gradle Template.

Un nouveau fichier est apparu ici : Assets/Plugins/Android/mainTemplate.gradle. Ouvrez-le et ajoutez ces lignes dans la section dependencies :

```shell
implementation 'com.android.support:appcompat-v7:28.0.0'

implementation 'com.android.support:support-v4:28.0.0'

implementation 'com.google.android.gms:play-services-vision:15.0.2'

implementation 'com.google.protobuf:protobuf-lite:3.0.0'
```

Cliquez sur [XR Plugin Management] et cochez [CardBoard XR Plugin].

Puis dans [File]->[Build Settings], assurez-vous d'avoir branché votre appareil en mode débogage USB et développeur (disponible dans les paramètres de ce dernier).

## Arizona

La scène HomeLand contient plusieurs assets : une caméra VR, une map ainsi qu'un prefab de zombie.

Commencez par tester une scène simple avec la caméra VR ainsi que quelques cubes placés dans votre scène. Installez l'application, mettez votre smartphone dans un casque et assurez-vous que la partie VR fonctionne.

Pour bien débuter ce jeu, vous devez être en mesure de tirer sur des zombies.

Sans manettes externes, votre système de tir sera automatique, c'est-à-dire que les tirs se déclencheront uniquement lorsque le zombie est dans votre champ de vision central. Les raycast peuvent aider.

Le projectile tiré peut être pour l'instant un simple cylindre de taille réduite.

Une fois que le tir automatique fonctionne, il faut s'assurer que le zombie touché subisse des dégâts et finisse par disparaître si ses points de vie atteignent 0.

Headshot ! Si le tir est effectué touche la tête du zombie, il meurt instantanément.

Un peu d'UI. Faites un marqueur de visée vert au centre du champ de vision. Lorsque vous visez un zombie, il doit devenir rouge. Il vous aidera en VR.

Pour l'instant vos zombies sont placés à la main.

Faites apparaître des zombies à un intervalle de temps compris entre 5 et 7 secondes.

À présent il ne doit y avoir que 3 zombies présents en même temps sur la map.

Les zombies doivent maintenant attaquer le joueur. Pour cela, ils doivent poursuivre le joueur. Faites les suivre votre position.

Vous devez subir les attaques des zombies : ajoutez une variable de vie à votre personnage. Si vous subissez trois attaques, vous perdez la partie.

Ajoutez un score, qui augmente à chaque zombie tué. Avec la localisation des dégâts, les tirs à la tête comptent double, et si sa jambe est touchée il avancera moins vite.

Selon le score atteint, les zombies gagnent en puissance : certains deviennent plus forts mais perdent en vitesse et à l'inverse d'autres moins résistants mais sont plus rapides.

D'autres devront être en mesure de tirer des projectiles sur vous s'ils se rapprochent trop prêt.

Pour englober ces dernières améliorations, ajoutez un système de manches de zombie. Lorsque tous les zombies de la manche ont été tués, déclenchez l'arrivée du boss de manche.

Dernière tâche : se déplacer.

Donnez la possibilité à votre joueur de se déplacer pour éviter l'arrivée des zombies.