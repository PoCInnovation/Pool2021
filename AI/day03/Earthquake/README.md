# AI Pool 2021 - Deep Learning - Earthquake
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
                                {Module Earthquake}             .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [17/03/2020]
```

---

Une série de seismse se produit ces derniers mois dans tout l'hemisphere nord.
L'équipe scientifique à pu récupérer les données de nos differents sismomètres, vous allez devoir les exploiter.

Vous trouverer dans les documents une série de valeurs correspondant sur la gauche la donnée accoustique et sur la droite le temps avant le prochain séisme.
Votre objectif est de concevoir un modele de Deep Learning capable de predire depuis une série de donnée accoustique le temps avant le prochain séisme.

Pour cela vous devrez uttilisez un modele recurant (RNN).

# Manuel RNN

Un RNN à pour particularité de gérer non pas de simple donnée mais des sequences de données.
Pour cela le modele à en plus de son layer d'output un layer hidden.

<img src=".img/rnn-struct.png" />

Ce layer hidden permet de conserver de la donnée à travers plusieurs forward permetant ainsi à votre modele d'avoir une notion de séquence.
Enfin pour calculer la loss il ne faut pas oublier que cette derniere est la somme de la loss de tout les foward d'une meme sequence.

# Consigne

- Sauvergardez et loadez votre dataset via numpy pour faciliter son usage.
- Créez un modele RNN en uttilisant seulement nn.Linear.
- Uttilisez des sequences de données de taille 100
- Entrainez le model jusqu'à avoir un delta moyen de 10% entre votre prediction et le label.
- Affichez un graphique montrant l'évolution de la loss et du delta moyen.
- Si vous augmentez la taille de votre séquence que se passe-t-il ? Pourquoi ?

**few tips**
- La donnée est de shape `(-1, batch, sequence, data)`.
- La loss est calculé sur l'ensemble de la sequence.
  Ainsi sur une sequence $S$ de taille $5$: loss = l(S[0]) + l(S[1]) + l(S[2]) + l(S[3]) + l(S[4])

**Usefull link**
- Slides RNN: https://docs.google.com/presentation/d/17-OeHgELG6fgAOvDLRmMl6MVpGYkANmSBcLcIVa_X70/edit?usp=sharing
- NLP from scratch (doc torch): https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html
- numpy.save: https://numpy.org/doc/stable/reference/generated/numpy.save.html
