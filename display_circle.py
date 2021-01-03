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
    # Disjonction de cas suivant si le chiffre est un carré parfait ou non

    if int(n**0.5) == n**0.5:
        carre_sup = n**0.5
    else:
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
        x = (i%carre_sup)*2*r+r
        y = (i//carre_sup)*2*r+r
        matrice.append(Cercle(x, y, r))
    return matrice, r


def init_circles_random():

    return matrice, r

def display_circles(matrice, r):
    plt.figure(figsize=[5, 5])
    ax = plt.axes([0.1, 0.1, 0.8, 0.8], xlim=(0, 1), ylim=(0, 1))
    points_whole_ax = 5 * 0.8 * 72    # 1 point = dpi / 72 pixels

    for point in matrice:

        # this lines comes from the stackoverflow thread :
        # https://stackoverflow.com/questions/33094509/correct-sizing-of-markers-in-scatter-plot-to-a-radius-r-in-matplotlib

        points_radius = 2 * r / 1.0 * points_whole_ax
        ax.scatter(point.x, point.y, s=points_radius**2, color='r')
    plt.grid()
    plt.draw()

if __name__ == '__main__':

    matrice, r = init_circles(int(sys.argv[1]))
    display_circles(matrice, r)
    plt.show()
