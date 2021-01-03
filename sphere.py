from cercle import Cercle

class Sphere(Cercle):

    def __init__(self, x, y, z, r):
        super().__init__(x,y,r)
        self.z = z

    def get_position():
        return [self.x,self.y, self.z]


    def set_position(x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return [x, y, z]
