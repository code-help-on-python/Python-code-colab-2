import math


class InfoFinder:
    def __init__(self):
        self.pi = math.pi

    def crircle(self, r=None, d=None):
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

    def cilinder(self, h, r=None, d=None):
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

    def squer_piremid(self, a, h):
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


if __name__ == "__main__":
    algo = InfoFinder()
