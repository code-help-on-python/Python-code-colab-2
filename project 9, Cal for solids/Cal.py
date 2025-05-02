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
        circumference = 2 * pi * radius
        area = 4 * (pi * (radius ** 2))
        volume = (4 / 3) * (pi * (radius ** 3))
        return f"""
Circumference: {round(circumference)}
Area: {round(area)}
Volume: {round(volume)}
"""

    def cube(self, side_length):
        a = side_length
        area = (a * a) * 6
        area_side = a ** 2
        volume = a ** 3
        return f"""
Area of side: {area_side}
Total area: {area}
Volume: {volume}
"""

    def cuboid(self, l, b, h):
        area_base = l * b
        volume = area_base * h
        return f"""
Base area: {area_base}
Volume: {volume}
"""

    def cylinder(self, h, r=None, d=None):
        pi = self.pi
        height = h
        if r is None:
            radius = d / 2
        else:
            radius = r

        area_circle = round(pi * (radius ** 2))
        area_curved_surface = round((2 * pi * radius) * height)
        volume = area_circle * height

        return f"""
Area of circular base: {area_circle}
Area of curved surface: {area_curved_surface}
Total area: {area_circle + area_curved_surface}
Volume: {volume}
"""

    def square_pyramid(self, a, h):
        square_area = a ** 2
        triangle_area = (a * h) / 2
        total_area = square_area + 2 * a * math.sqrt((((a ** 2) / 4) + (h ** 2)))
        volume = square_area * (h / 3)
        return f"""
Base area (square): {square_area}
Area of triangular side: {triangle_area}
Total area: {total_area}
Volume: {volume}
"""

    def cone(self, r, l, h):
        pi = self.pi
        radius = r
        slant_height = l
        circle_area = pi * (radius ** 2)
        curved_surface_area = pi * radius * slant_height
        volume = (circle_area * h) / 3
        return f"""
Base area (circle): {circle_area}
Curved surface area: {curved_surface_area}
Total area: {circle_area + curved_surface_area}
Volume: {volume}
"""


if __name__ == "__main__":
    algo = InfoFinder()
    while True:
        a = input("What solid do you need help with (Sphere-s, Cube-c, Cuboid-cu, Cone-co, Cylinder-cy, Pyramid-p)? Type 'exit' to exit:\n").lower()
        if a == 'exit':
            print('Bye, hope you come back again! :)')
            break
        if a == 's':
            d_r = input('Type "r" for radius or "d" for diameter: ').lower()
            if d_r == 'r':
                r = float(input('What is the radius?\n'))
                print(algo.sphere(r=r))
            elif d_r == 'd':
                d = float(input('What is the diameter?\n'))
                print(algo.sphere(d=d))
            else:
                print('Please use the correct short form...')
                continue
        elif a == 'c':
            side = float(input('What is the length of a side?\n'))
            print(algo.cube(side))
        elif a == 'cu':
            l, b, h = map(float, input('Enter the length, breadth, and height (separated by commas):\n').split(','))
            print(algo.cuboid(l, b, h))
        elif a == 'co':
            r, l, h = map(float, input('Enter the radius, slant height, and height (separated by commas):\n').split(','))
            print(algo.cone(r, l, h))
        elif a == 'cy':
            d_r = input('Type "r" for radius or "d" for diameter: ').lower()
            if d_r == 'r':
                r, h = map(float, input('Enter the radius and height (separated by commas):\n').split(','))
                print(algo.cylinder(h, r))
            elif d_r == 'd':
                d, h = map(float, input('Enter the diameter and height (separated by commas):\n').split(','))
                print(algo.cylinder(h, d=d))
            else:
                print('Please use the correct short form...')
                continue
        elif a == 'p':
            a, h = map(float, input('Enter the base length and height (separated by commas):\n').split(','))
            print(algo.square_pyramid(a, h))
        else:
            print('Please use the correct short forms...')
            continue
