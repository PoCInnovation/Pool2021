# AI Pool 2021 - Deep Learning - VCAI

Bonjour l'équipe technique, vous avez fait du très bon travail. Malheureusement cela ne suffit pas.
Il nous faut plus de main d'œuvre pour accomplir notre mission, mais toutes nos équipes sont déjà surchargées. Vous allez devoir trouver une solution.

L'équipe scientifique nous a fait parvenir des plans d'une potentielle solution.
Ils ont besoin pour la réaliser d'une IA capable de comprendre des ordres qu'on lui donne et de les effectuer.

Vu que vous avez mené à bien la mission XRAI, vous ne devriez pas être dépaysés par ce challenge.
La principale difference se trouve dans le type des données. Vous devrez cette analyser non pas des photos, mais des enregistrements audio.

Vous aurez donc à effectuer un préprocessing des données pour réussir cette mission.

## Dataset

Téléchargez le dataset ici : [speech_commands_v0.02.tar.gz](http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz).

## Consignes

- Créez un spectrogramme à partir de chaque enregistrement audio.
- Sauvegardez les spectrogrammes dans un fichier `.hdf5`. Ces spectrogrammes forment votre dataset.
- Construisez un modèle permettant de déterminer la commande vocale donnée en input, avec une accuracy (précision) minimale de 75%.
- Affichez avec matplotlib l'évolution de la loss
- Affichez avec matplotlib l'évolution de l'accuracy


## Message de l'équipe scientifique

Faites attention à ne donner à votre modèle que les informations essentielles. Éliminez tous le superflu (bordures, marges, etc).

## Usefull links:
- [How to use SciPy](https://docs.scipy.org/doc/scipy/reference/)
- [How to use os](https://docs.python.org/fr/2.7/library/os.html)
