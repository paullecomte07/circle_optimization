# PACKING N CIRCLES IN THE UNIT SQUARE

Proposition d'une solution par Paul Lecomte, Noémie Laguelle et Thomas Meier.

## Introduction

### Historique

Tout d’abord, il existe de nombreux problèmes d'optimisation intéressants liés au placement d’objets dans un volume fermé ou une surface délimitée. Des exemples typiques surgissent en physique ou en chimie où des questions du type "Quel est l'empilement le plus dense d'atomes ou de molécules ?" peuvent se poser, comme lorsqu'un cristal ou une macromolécule est formé avec la plus faible énergie. C’est donc de ce constat que nous pouvons étudier au-delà de l’aspect purement mathématique ce problème de l'empilement optimal de n cercles égaux dans un carré, problème qui a d’ailleurs fasciné les mathématiciens au cours des dernières années. Aussi, il est intéressant de noter que ce problème est équivalent à un autre problème : celui du placement de n points dans un carré unité tel que la distance minimum m entre deux de ces points soit maximale. En notant r le rayon des cercles dans la première formulation du problème, la relation entre ces deux problèmes est r = m/(2*(m+1)).

Pour mettre un peu de contexte dans la résolution historique de ces deux problèmes qui ne sont qu’un, de nombreux papiers scientifiques sont sortis au cours des dernières décennies dans le but de les résoudre malgré leur caractère plutôt simple au premier abord :

-	La situation pour le placement de 2 à 9 cercles dans un carré a déjà été résolue en 1964. Les cas n = 2,3,4 et 5 ont été résolus facilement. Pour n = 6, c'est R.L. Graham qui a trouvé la solution optimale. Les preuves pour n = 7 et n = 8 ont été faites par J. Schaer et A. Meir. Il est intéressant de noter que le placement optimal de 7 cercles se fait avec un cercle "libre", c'est-à-dire qui voit son centre être déplacé à l'intérieur d'une région délimitée ;

-	Pour 10 cercles, ce problème a connu une longue histoire qui a commencé en 1970 lorsque M. Goldberg a proposé un arrangement symétrique composé de 4 rangées de 3-2-3-2 cercles. Les cercles de cet arrangement avaient un rayon environ égal à 0,14706. Seize ans plus tard, en 1986, R. Milano a prouvé que son arrangement à lui avec un rayon d’environ 0,14792 était alors le meilleur arrangement symétrique. Cependant, quelques années plus tard, de meilleures solutions, chaotiques qui plus est, ont été trouvées et notamment la solution optimale avec un rayon environ égal à 0,148204. De plus, il fut même possible de donner le résultat exact puisque celui-ci correspond au plus petit zéro positif du polynôme suivant : 1180129m^18 – 11436428m^17 + 98015844m^16 – 462103584m^15 + 1145811528m^14 – 1398966480m^13 + 227573920m^12 + 1526909568m^11 – 1038261808m^10 – 2960321792m^9 + 7803109440m^8 – 9722063488m^7 + 7918461504m^6 – 4564076288m^5 + 1899131648m^4 – 563649536m^3 + 114038784m^2 – 14172160m + 819200 ;

-	Pour les cas de 11 à 13 cercles, les preuves de l’optimalité des solutions trouvées utilisèrent essentiellement les mêmes techniques que pour 10 cercles. Il est intéressant de noter que pour le cas n = 12, la solution optimale est une simple structure en diamant formée de 4 rangées de 3 cercles chacune mais que si l'on considère un cercle de plus, la situation devient beaucoup plus compliquée. Comment disposer un cercle supplémentaire dans la configuration très compacte de 12 ? Finalement, la solution fut trouvée. Enfin, dans les trois cas, le résultat exact peut être obtenu comme étant le plus petit zéro positif d'un polynôme, le cas le plus difficile ayant été n = 13, avec un polynôme de degré 40 ;

-	Pour les cas de 14 à 20 cercles, les solutions furent trouvées numériquement mais avec un nombre croissant de cercles, il devient de plus en plus difficile de converger vers l'optimum global. Pour un nombre de cercles encore plus grand, il devient même plus probable d’être piégé dans des optima locaux.

### Définition du problème

Soit *n* un nombre naturel donné. Le problème consiste à placer *n* cercles identiques dans le carré unité avec le plus rand rayon possible pour ces cercles, sans que ceux-ci ne se chevauchent ou ne chevauchent les frontières du carré. Il s'agit donc de déterminer le rayon *r* maximal de ces *n* cercles enfermés. On représentera par (*x<sub>i</sub>*, *y<sub>i</sub>*) les coordonnées du centre du *i*-ème cercle. On peut alors écrire le problème de la manière suivante :

![GitHub Logo](/images/formules_mathematiques.png)

Aussi, le but est ici de proposer une stratégie de résolution de ce problème par MBH : il faut donc choisir et générer une bonne situation de départ, choisir un bon solveur, déterminer les variables à perturber, tester l’algorithme… Le but est également de résoudre ce problème mais dans le cube unité avec *n* sphères identiques.


## Placement initial des points

La façon la plus simple de positionner les points à l'état initial tout en respectant les contraintes est de générer des positions aléatoire dans l'intervale [0,1] en prenant des rayons nuls. Cette initialisation fonctionne très bien, mais nous nous sommes tout de même posés la question suivante : l'initialisation joue-t-elle un rôle crucial dans la performance des algorithmes. Nous avons donc réfléchi à une autre manière de procéder. L'objectif est de trouver une solutions faisable pour tout *n*.

Pour trouver ainsi un solution quelque soit *n*, notre démarche est la suivante :

- On calcule le premier carré parfait supérieur à *n* ;

- On calcule alors *r* en sachant qu'il y sqrt(*n*) boule à placer dans la largeur.

Cet algorithme nous donne pour tous les carrées parfaits la configuration où *r* est déjà maximal, enfin d'après l'article [14] global opitimization, on constate que on est proche de la taille moyenne des cercles en moyenne lors de l'initialisation  où *r* = 1.07456993182354/sqrt(*n*).

Remarque avec ce type d'initilialisation : il s'avère que partir d'un configuration où les boules ont déjà un rayon assez grand ne permet pas d'améliorer radicalement le temps de calcul. Pire, il semble au vu de nos expérimentations qu'il soit préférable de partir de cercles de rayon 0. En effet, le problème avec ce placement déjà optimisé, c'est qu'il est difficile  de changer de configuration radicalement. C'est possibble si l'on commence avec des cercles de rayon très petit.


## Implémentation et utilisation du code

### Description de la disposition des différents fichiers

**my_model.py** contient le code qui contruit le modèle Pyomo utilisé dans l'optimisation. Il contient le modèle utile pour le problème 2D mais aussi le problème 3D.

**optimization_functions.py** contient le code des différents algorithmes d'optimisation.

### Choix de la perturbation

Pour le choix de la perturbation, nous avons grossièrement trouvé que 0,3 fonctionnait bien. Pour les expérimentations, nous utilisons donc ce paramètre. Toutefois, nous nous sommes résolus à réaliser de nombreux tests afin d'en déduire la perturbation optimale. Nous avons donc réalisé 18 mesures pour *n* = 44 et pour des perturbations différentes.

En bleu, vous avez la courbe pour l'algorithme MBH (localsolver : snopt, initialisation : random). En orange, vous avez la courbe pour l'algorithme multistart (localsolver : snopt, initialisation : random) dont le résultat ne dépend bien évidemment pas de la perturbation. Ce resultat est la moyenne de 5 valeurs trouvées pour *n* = 44.

![](/perturbation.png)

Plusieurs remarques sont à faire au vu de ce graphique.

Tout d'abord, on constate que la valeur de la perturbation est non négligeable sur la valeur des rayons obtenus. Étant conscient qu'il nous manque des valeurs pour pouvoir interpoler fiablement les données sur un courbe, nous pouvons penser que la perturbation optimale se situe dans l'intervalle [0.1,0.35].

Ensuite, il est rassurant de voir que lorsque l'on choisit une perturbation trop grande, nous retrouvons des valeurs de *r* qui se rapprochent de celle du multistart. En effet, lorsque les perturbations sont bien plus grandes que les rayons des cercles, à chaque itération du MBH, tout se passe comme si nous mélangions de facon complétement aléatoire tous les cercles, ce qui revient au multistart.


## Comparaison avec l'algorithme Multistart

Nous avons par la suite comparé les résultats obtenus avec l'algorithme MBH à ceux obtenus avec l'algorithme Multistart. 

Dans un premier temps avec le solveur snopt, vous trouverez ci-dessous les résultats obtenus pour différents *n* et différents temps d'exécution :

![GitHub Logo](/images/comparaison_MBH_Multistart_snopt.png)

*r*_ref est la valeur donnée par le site Packomania pour chaque *n*, elle nous permet de calculer un delta relatif. On remarque qu'en majorité, l'algorithme MBH est celui qui, à temps égaux, nous donne un rayon le plus proche du rayon maximal.

Nous avons aussi testé avec le solveur knitro et différents *n*, là encore, c'est plutôt l'algorithme MBH qui donne les meilleurs résultats à temps égaux :

![GitHub Logo](/images/comparaison_MBH_Multistart_knitro.png)


## Conclusion

Pour conclure, nous avons vu que le problème de la maximisation du rayon de n cercles identiques dans le carré unité 
