# Bienvenue dans le module *Virus Scan* du programme *Far From Earth*
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
                                {Virus Scan}                    .;;
                                                               ,;;;
                                --Far From Earth--           ,;;;;:
                                                          ,;@@   .;
                                                         ;;@@'  ,;
                                                         ';;, ,;'        [01/02/2021]
```

---
Bonjour l’équipe technique, l’heure est grave. Nous savons que nous vous sollicitons énormément mais votre travail est vital et contribue à la survie de l’humanité !

Nous avons détecté un nouveau virus capable d’accélérer les problèmes cardiaques. Nous menons des analyses plus poussées pour savoir d’où il vient, et sont les personnes les plus à risque d'être affectées. Nous vous avons fourni des données, et nous avons besoin que vous développiez une IA capable de prédire les personnes susceptibles de contracter une forme sévère de ce virus.

Nous comptons sur vous !

## Consigne :

Référez-vous au fichier ```submit/maxi_neurone.py```

> Vous avez besoin d’améliorer votre classe `Neurone`, car le problème ici n’est plus linéaire mais binaire “oui ou non”

+ Créez une fonction `sigmoid_activation()` qui représente l'étape forward de la sigmoide.

> Cette fonction prend en paramètre les inputs.

+ Créez une fonction `d_sigmoid_d_input()` qui représente la dérivée de la sigmoid (et donc l'étape backward).

> Cette fonction prend en paramètre les inputs.

+ Dans la classe `Neurone`, créez une fonction `backward_sigmoid()` qui implémente l’étape de backward du neurone avec la fonction d’activation sigmoid et non la fonction d’activation linear.

---

Référez-vous au fichier ```submit/virus_scan.py```

> Vous avez dans le dossier `data/` toutes les données nécessaires.

+ Créez une fonction `getData()` qui récupère et nettoie ces données. N’oubliez pas de normaliser !

> Utilisez pandas pour étudier et comprendre les données.

+ Créez une fonction (un itérateur) pour séparer les données en batch.

+ Implémentez un `main` Python en utilisant votre classe `Neurone` créant une IA capable de prédire si une personne est susceptible d’avoir une forme sévère ou non du virus.
