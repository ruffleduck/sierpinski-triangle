"""Generate a Sierpinski Triangle.

Creator: Alexander J. Davison
Date:    10/22/2018
"""

from PIL import Image, ImageDraw
from math import sin, cos, pi

ITERATIONS = 8


class Triangle:
    """Represents a specific triangle in the Sierpinski Triangle."""

    def __init__(self, p1, p2, p3):
        """Initialize the three points p1, p2, and p3."""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw_triangle(self, draw):
        """Render the triangle onto the image."""
        draw.polygon((self.p1, self.p2, self.p3), fill=(0, 0, 0))

    def sub_triangles(self):
        """Generate the sub-triangles of the current triangle."""
        a = midpoint(self.p1, self.p2)
        b = midpoint(self.p2, self.p3)
        c = midpoint(self.p3, self.p1)
        t1 = Triangle(self.p1, a, c)
        t2 = Triangle(a, self.p2, b)
        t3 = Triangle(c, b, self.p3)
        return [t1, t2, t3]


def equilateral_triangle(side, x_shift, y_shift):
    """Generate an equilateral triangle.

    side -- The length of each side
    x_shift -- How far left or right you wish to shift the image
    y_shift -- How far up or down you wish to shift the image
    """
    k1 = sin((1 / 6) * pi)
    k2 = cos((1 / 6) * pi)
    return Triangle(
        (x_shift, y_shift),
        (x_shift + side * k1, y_shift + side * k2),
        (x_shift - side * k1, y_shift + side * k2)
    )


def midpoint(p1, p2):
    """Calculate the midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

triangles = [equilateral_triangle(900, 500, 50)]
for _ in range(ITERATIONS):
    new_triangles = []
    for triangle in triangles:
        new_triangles.extend(triangle.sub_triangles())
    triangles = new_triangles

for triangle in triangles:
    triangle.draw_triangle(draw)

img.save('sierpinski.png')
