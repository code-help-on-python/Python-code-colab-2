import math


class InfoFinder:
    def __init__(self):
        self.pi = math.pi

    def crircle_area(self, r=None, d=None):
        if r == None:
            radius = d / 2
        else:
            radius = r
        pi = self.pi
        circumfernce = 2 * pi * radius
        area = 4 * (pi * (radius ** 2))
        volume = 4/3 * (pi * (radius ** 3))
        return f"""
        Circumference : {round(circumfernce)}
        Area : {round(area)}
        volume : {round(volume)}
        """


algo = InfoFinder()
r_or_d = input('Do you have radius or diamiter? (diamiter(d) radius(r))? ').lower()
if r_or_d == 'd':
    print(algo.crircle_area(d=float(input('What is the diamiter? '))))
else:
    print(algo.crircle_area(r=float(input('What is the radius? '))))
