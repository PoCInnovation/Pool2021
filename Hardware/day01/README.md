# PoC HPool D01 - BAS

Pour toute la durée de cette piscine, vous aurez besoin de l'[IDE Arduino](https://www.arduino.cc/en/main/software)

Les exercices devront être réalisés dans l’ordre et présentés a un encadrant une fois terminés pour qu’il vérifie votre travail.

> Comment fonctionnent les divers objets électroniques qui m’entourent? Comment puis-je moi même fabriquer un robot capable de combattre d'autres robots?

Pro tips: avant de construire le Megazord, apprenez déjà à allumer une LED.

## `Pool TALK` Introduction à l'électronique

Merci d'assister au talk.

## BASICS

---

### *`EX01` No code, just volts*

Faites un circuit reliant une LED a un Arduino et allumer cette LED. Appelez un encadrant avant d’alimenter votre Arduino.

**Contraintes**: Vous ne devrez utiliser aucun code pour cet exercice. Vous n’avez pas le droit à la pin 3,3V de votre carte.

Est-ce que le voltage accepté par la LED est compatible avec le voltage délivré par la carte que vous avez?

### *`EX02` Toogle or not toogle*

Faites en sorte que le bouton change d'état (allume/éteint) la LED a chaque pression.

### *`EX03` blink-182*

Faites en sorte que la LED clignote toutes les secondes.

## DATA

---

Les cartes Arduino possèdent deux type d'I/O, les digitaux et les analogues. La différence est simple, les pins digitaux vont pouvoir, lire / envoyer des valeurs binaires (LOW ou HIGH), alors que les pins analogues vont pouvoir varier. Si par exemple les deux bornes sont (0; 255), alors je pourrais lire 16 comme 232 selon l'information que le capteur remonte.

### *`EX04` Ana-logic*

En reprenant le circuit de l’exercice 3, faites en sorte que le délai de clignotement de la LED soit dépendant d'un potentiomètre.

### *`EX05` Brighter, brighter, out*

En reprenant le circuit de l’exercice 4, faites en sorte que la LED ne clignote plus, et que l’intensité de son éclairage dépende de la valeur du potentiomètre.

> Il serait quand même préférable que votre robot sache ce qui l'entoure ...

### *`EX06` Up ahead in the distance*

Créer un nouveau circuit qui va récupérer la distance donnée par le capteur ultrasons et qui, si elle est inférieure a 30cm, allume la LED.

> ... et que vous sachiez aussi.

### *`EX07` Show me da way*

En reprenant le circuit de l’exercice 6, afficher la distance donnée par le capteur, et envoyez la en centimètres via une connexion série a votre ordinateur.

### *`EX08` MoniTHORing*

En reprenant le circuit de l’exercice 7, et le code Arduino de l’exercice 8, réaliser un programme dans le langage de votre choix qui va récupérer la sortie série de votre Arduino et l’afficher a l'écran dans un format de votre choix.

**Contraintes**: Aucune librairie spécifiquement créée pour ESP32 n’est autorisée.

Afficher la distance sous forme graphique.

## THE ARDUINO IS JUST A MICRO-CONTROLLER

---

### *`EX09` Turn around*

Créer un nouveau circuit qui va alimenter un moteur quand le bouton sera pressé. Appelez un encadrant avant d’alimenter votre circuit.

**Contraintes**: Ne pas utiliser de résistances.

Les moteurs fonctionne mieux avec une alimentation 12v.

![pickaxe](https://github.com/PoCInnovation/Pool2021/blob/master/.github/assets/hardware_pickaxe.png)

## Getting an upgrade

Pour les exercices restants, et si ça n'étais pas le cas depuis le début de la journée, vous devrez changer de carte pour une ESP32. Contactez les encadrants pour savoir de laquelle il s'agit.

Vous aurez besoin de l'extention pour **ESP32** de l'IDE Aduino.

### *`EX10` Flatuicolors death*

Réaliser une WebUI ou gui avec un colorpicker qui pilote la LED selon la couleur sélectionnée.

**Contraintes**: Ne pas connecter l’ESP32 à un réseau wifi existant.

Appelez un encadrant avant de faire vos branchements.

### *`EX11` Minitel*

Votre ESP32 devra se connecté a votre téléphone ou ordinateur en Bluetooth et afficher la distance en centimètres donne par le capteur ultrason.

Appelez un encadrant avant de faire vos branchements.

### *`BONUS` World Wide Hardware*

Reprendre les exercices précédents et ajouter plus de contenu et d’interaction sur le WebGUI. 

## Conclusion

---

Vous avez appris tout au long de cette journée les bases de l'hardware, en réfléchissant un peu vous seriez presque capables de le construire votre robot... Il vous manquerait juste...

![continued](https://github.com/PoCInnovation/Pool2021/blob/master/.github/assets/hardware_continued.png)

## YOUTUBE

---

Voici une liste de chaînes youtube traitant d'électronique / d'hardware  :

[AvE](https://www.youtube.com/user/arduinoversusevil)

[GreatScott!](https://www.youtube.com/user/greatscottlab)

[This Old Tony](https://www.youtube.com/user/featony)

[NYC CNC](https://www.youtube.com/user/saunixcomp)

[ElectroBOOM](https://www.youtube.com/user/msadaghd)
