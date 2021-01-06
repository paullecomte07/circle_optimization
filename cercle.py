"""

Ce script définit l'objet Cercle que nous serons amenés à manipuler dans différents script comme entre autres dans display_circle.py.

"""


class Cercle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_position():
        return [self.x,self.y]

    def get_raduis():
        return self.r

    def set_radius(nouveau_rayon):
        self.r = nouveau_rayon
        return self.r

    def set_position(x, y):
        self.x = x
        self.y = y
        return [x, y]
