import math


class InfoFinder:
    def __init__(self):
        self.pi = math.pi

    def sphere(self, r=None, d=None):
        if r is None:
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

    def cube(self, side_length):
        a = side_length
        area = (a * a) * 6
        area_side = a ** 2
        volume = (a ** 3)
        return f"""
Area of side : {area_side}
Total area = {area}
Volume = {volume}
        """

    def cuboid(self, l, b, h):
        area_base = l * b
        vloume = area_base * h
        return f"""
Base area : {area_base}
Volume : {vloume}
        """

    def cylinder(self, h, r=None, d=None):
        pi = self.pi
        hight = h
        if r is None:
            radius = d / 2
        else:
            radius = r

        area_curcle = round((pi * (radius ** 2)))
        area_curved_serface = (round((2 * pi * radius)) * hight)
        volume = area_curcle * hight

        return f"""
Area of circulor base : {area_curcle}
Area of curved serface : {area_curved_serface}
Totel area : {area_curcle + area_curved_serface}
Volume : {volume}
        """

    def squer_pyramid(self, a, h):
        a = a
        h = h
        square_area = a ** 2
        trangle_area = (a * h) / 2
        area_total = (a ** 2) + 2 * a * math.sqrt((((a * a) / 4) + (h * h)))
        volume = (a * a) * (h / 3)
        return f"""
Area of square base : {square_area}
Area of trangulor side : {trangle_area}
Total area : {area_total}
Volume : {volume}
        """

    def corn(self, r, l, h):
        pi = self.pi
        radius = r
        slant_hight = l
        circle_area = pi * radius * radius
        curved_area = pi * radius * slant_hight
        volume = ((pi * radius * radius) * h) / 3
        return f"""
Area of cuirculor part : {circle_area}
Area of curved serface : {curved_area}
Total area : {circle_area + curved_area}
Volume : {volume}
        """


if __name__ == "__main__":
    algo = InfoFinder()
    while True:
        a = input('What is the solid you need help with (Sphere-s, Cude-c, Cuboid-cu, Corn-co, Cylinder-cy, Pyramid-p) exit to exit?\n').lower()
        if a == 'exit':
            print('Bye, hope you coe bac again:)!!')
        if a == 's':
            d_r = input('Radius-r or Diameter-d').lower()
            if d_r == 'r':
                r = float(input('What is the radius?\n'))
                print(algo.sphere(r=r))
            elif d_r == 'd':
                d = float(input('What is the diameter?\n'))
                print(algo.sphere(d=d))
            else:
                print('Please use short form...')
                continue
        elif a == 'c':
            a = float(input('What is the lenght of a side?\n'))
            algo.cube(a)
        elif a == 'cu':
            l, b, h = input('What is the lenght, beadth and hight(separate by coma)?\n').strip(' ').split(',')
            s = [float(i) for i in [l, b, h]]
            l, b, h = s
            print(algo.cuboid(l, b , h))
        elif a == 'co':
            r, l, h = input('What is the radius, slant lenght and higth(separate by coma)?\n').strip(' ').split(',')
            s = [float(i) for i in [r, l, h]]
            r, l, h = s
            algo.corn(r, l, h)
        elif a == 'cy':
            d_r = input('Radius-r or Diameter-d').lower()
            if d_r == 'r':
                r, h = input('What is the radius and hight(separate by coma)? \n').strip(' ').split(',')
                s = [float(i) for i in [r, h]]
                r, h = s
                print(algo.cylinder(h, r))
            elif d_r == 'd':
                d, h = input('What is the diameter and hight(separate by coma)?\n').strip(' ').split(',')
                s = [float(i) for i in [d, h]]
                d, h = s
                print(algo.cylinder(h, d=d))
            else:
                print('Please use short form...')
                continue
        elif a == 'p':
            a, h = input('What is the lenght of the base and the hight(separate by coma)?\n')
            s = [float(i) for i in [a, h]]
            a, h = s
            print(algo.squer_pyramid(a, h))
        else:
            print('Use the short forms...')
            continue