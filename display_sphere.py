import sys

from sphere import Sphere
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from random import random

def init_spheres(n):
    """

    Description:
        Cette fonction positionne les spheres de façon ordonnée mais pas forcément optimisée
    Args:
        n : le nombre de boules dans le a caser

    """
    # Disjonction de cas suivant si le chiffre est un carré parfait ou non

    if int(n**(1/3)) == n**(1/3):
        cube_sup = n**(1/3)
    else:
        cube_sup = int(n**(1/3)+1)

    # le nombre de cercle que l'on peut placer au max
    n_max = cube_sup**3

    # le rayon de chaque cercle
    r = 1/(cube_sup*2)

    # matrice qui contient les différents points
    matrice = []
    # coordonnées du point en cours de placement
    x = 0
    y = r
    z = r

    for i in range(n):
        x = (i%cube_sup)*2*r+r
        if (i%cube_sup == 0) and (i != 0):
            y += 2*r
            y = y%1
        if (i%(cube_sup**2) == 0) and (i!=0):
            z += 2*r
        matrice.append(Sphere(x, y, z, r))
    return matrice, r


def init_spheres_random(n):
    r = 0
    matrice = []
    for i in range(n):
        x = random()
        y = random()
        z = random()
        matrice.append(Sphere(x, y, z, r))
    return matrice, r

def display_spheres(matrice, r):
    fig = plt.figure(figsize=[5, 5])
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    points_whole_ax = 5 * 72 * 0.425  # 1 point = dpi / 72 pixels

    for point in matrice:

        # this lines comes from the stackoverflow thread :
        # https://stackoverflow.com/questions/33094509/correct-sizing-of-markers-in-scatter-plot-to-a-radius-r-in-matplotlib

        points_radius = 2 * r / 1.0 * points_whole_ax
        ax.scatter(point.x, point.y, point.z, s=points_radius**2)
    plt.grid()
    plt.draw()

if __name__ == '__main__':

    matrice, r = init_spheres(int(sys.argv[1]))
    display_spheres(matrice, r)
    plt.show()
