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

### Première idée:

La façon la plus simple de positionner les points à l'état initial tout en respectant les contraintes est de générer des positions aléatoire dans [0 ,1] en prenant des rayons nuls. Cette initialisation fonctionne très bien, mais nous nous sommes tout de même posés la question suivante: l'initialisation joue-t-elle un rôle crutial dans la performance des algorithmes. Nous avons donc réfléchis à une autre manière de procéder. L'objectif est de trouver une solutions faisable pour tout n.

Pour trouver ainsi un solution quelque soit n, notre démarche est la suivante:
- On calcule le premier carré parfait supérieur à n.
- On calcule alors r en sachant qu'il y sqrt(n) boule à placer dans la largeur.

Cet algorithme nous donne pour tous les carrées parfaits la configuration où r est déjà maximal, enfin d'après l'article [14] global opitimization, on constate que on est proche de la taille moyenne des cercles en moyenne lors de l'initialisation  ou r=1.07456993182354/sqrt(n)

Remarque avec ce type d'initilialisation:
Il s'avère que partir d'un configuration où les boules ont déjà un rayon assez grand ne permets pas d'améliorer radicalement le temps de calcule. Pire, il semble au vu de nos expérimentations que il soit préférable de partir de cercle de rayon 0. En effet, le problème avec ce placement étant déjà optimisé, il est difficile  de changer de configuration radicalement. C'est possibble si l'on commence avec des cercles de rayon très petit)

## Choix du solveur local

## Choix de la perturbation

## Comparaison avec l'algorithme Multistart

## Conclusion

Cours de la prof : aller plus loin dans le projet
