# circle_optimization

L'objectif de ce repository est de proposer une solution pour le problème suivant :

**Packing n circles in the unit square with the largest possible radius**


## Définition du problème

Soit *n* un nombre naturel, il s'agit de déterminer le rayon *r* maximal de *n* cercles enfermés dans un carré de côté unitaire sans que ces cercles ne se chevauchent. On représentera par (*x<sub>i</sub>*, *y<sub>i</sub>*) les coordonnées du centre du *i*-ème cercle.
<br/>On peut alors écrire le problème de la manière suivante :

![GitHub Logo](/images/formules_mathematiques.png)


## Première stratégie

Recherche historique des solutions (articles)


## Placement initial des points


La façon la plus simple de positionner les points à l'état initial tout en respectant les contraintes est de générer des positions aléatoire dans [0 ,1] en prenant des rayons nuls. Cette initialisation fonctionne très bien, mais nous nous sommes tout de même posés la question suivante: l'initialisation joue-t-elle un rôle crutial dans la performance des algorithmes. Nous avons donc réfléchis à une autre manière de procéder. L'objectif est de trouver une solutions faisable pour tout n.

Pour trouver ainsi un solution quelque soit n, notre démarche est la suivante:
- On calcule le premier carré parfait supérieur à n.
- On calcule alors r en sachant qu'il y sqrt(n) boule à placer dans la largeur.

Cet algorithme nous donne pour tous les carrées parfaits la configuration où r est déjà maximal, enfin d'après l'article [14] global opitimization, on constate que on est proche de la taille moyenne des cercles en moyenne lors de l'initialisation  ou r=1.07456993182354/sqrt(n)

Remarque avec ce type d'initilialisation:
Il s'avère que partir d'un configuration où les boules ont déjà un rayon assez grand ne permets pas d'améliorer radicalement le temps de calcule. Pire, il semble au vu de nos expérimentations que il soit préférable de partir de cercle de rayon 0. En effet, le problème avec ce placement étant déjà optimisé, il est difficile  de changer de configuration radicalement. C'est possibble si l'on commence avec des cercles de rayon très petit)

## Implémentation et utilisation du code

### Description de la disposition des différents fichiers

**my_model.py** contient le code qui contruit le modèle Pyomo utilisé dans l'optimisation. Il contient le modèle utile pour le problème 2D mais aussi le problème 3D.

**optimization_functions.py** contient le code des différents algorithmes d'optimisation.

## Choix du solveur local

## Choix de la perturbation

Pour le choix de la perturbation, nous avons grossièrement trouvé que 0.3 fonctionnait bien. Pour les expérimentations, nous utilisons donc ce paramètre.
Toutefois, nous nous sommes résolus à réaliser de nombreux tests afin d'en déduire la perturbation optimale. Nous avons donc réalisé 18 mesures pour n=44 et pour des perturbations différentes.

En bleu, vous avez la courbe pour l'algorithme MBH (localsolver: snopt, initialisation: random).
En orange, vous avez la courbe pour l'algorithme multistart (localsolver: snopt, initialisation: random) dont le résultat ne dépend bien évidemment pas de la perturbation. Ce resultat est la moyenne de 5 valeurs trouvée pour n=44.

![](/perturbation.png)

Plusieurs remarques sont à faire au vu de ce graphique.

Tout d'abord, on constate que la valeur de la perturbation est non négligeable sur la valeur des rayons obtenus. Etant conscient qu'il nous manque des valeurs pour pouvoir interpoler fiablement les données sur un courbe, nous pouvons penser qu'il pouvons penser que la perturbation optimale se situe dans [0.1, 0.35].

Ensuite, il est rassurant de voir que lorsque l'on choisit une perturbation trop grande nous retrouvons des valeurs de r qui se rapproche de celle du multistart. En effet, lorsque les perturbations sont bien plus grandes que les rayons des cercles, à chaque itération du MBH tout se passe comme nous mélangions de facon complétement aléatoire tous les cercles, ce qui revient au multistart.

## Comparaison avec l'algorithme Multistart

Nous avons par la suite comparé les résultats obtenus avec l'algorithme MBH à ceux obtenus avec l'algorithme Multistart. 

Dans un premier temps avec le solveur snopt, vous trouverez ci-dessous les résultats obtenus pour différents n et différents temps d'execution :
![GitHub Logo](/images/comparaison_MBH_Multistart_snopt.png)

r ref est la valeur donnée par le site Packomania pour chaque n, elle nous permet de calculer un delta relatif. 
On remarque qu'en majorité, l'algorithme MBH est celui qui, à temps égaux, nous donne un rayon le plus proche de celui maximal. 

Nous avons aussi testé avec le solveur knitro et différents n, là encore, c'est plutôt l'algorithme MBH qui donne les meilleurs résultats à temps égaux :
![GitHub Logo](/images/comparaison_MBH_Multistart_knitro.png)

## Conclusion

Cours de la prof : aller plus loin dans le projet
