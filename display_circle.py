import sys

from cercle import Cercle
import matplotlib.pyplot as plt


def init_circles(n):
    """
    Description:
        Cette fonction positionne les cercles de façon ordonnée mais pas forcément optimisée
    Args:
        n : le nombre de boules dans le a caser

    """

    carre_sup = int(n**0.5+1)
    # le nombre de cercle que l'on peut placer au max
    n_max = carre_sup**2
    # le rayon de chaque cercle
    r = 1/(carre_sup*2)
    # matrice qui contient les différents points
    matrice = []
    # coordonnées du point en cours de placement
    x = 0
    y = 0
    for i in range(n):
        x = (i%carre_sup)*r+r
        y = (i//carre_sup)*r+r
        matrice.append(Cercle(x, y, r))
    return matrice, r


if __name__ == '__main__':

    matrice, r = init_circles(int(sys.argv[1]))
    print(matrice)
    for point in matrice:
        print(point.x)
        plt.scatter(point.x, point.y,s=r**2)
    plt.show()
