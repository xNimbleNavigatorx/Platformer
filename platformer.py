"""
platformer.py
Author: xNimbleNavigatorx
Credit: ggame and classes tutorial
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

black = Color(0, 1)
white = Color(0xffffff, 1.0)
lgreen = Color(0x08FF00, 1.0)
dgreen = Color(0x126D0F, 1.0)
blue = Color(0x0F3E6D, 1.0)

thinblackline = LineStyle(2, black)
thinblueline = LineStyle(2, blue)
greenline = LineStyle(2, lgreen)
boundary = RectangleAsset(SCREEN_WIDTH-3, SCREEN_HEIGHT-3, thinblackline, white)
boundary1 = Sprite(boundary, (1,1))

ground = RectangleAsset(SCREEN_WIDTH-8, 50, greenline, lgreen)
ground1 = Sprite(ground, (4, SCREEN_HEIGHT-54))

skip = PolygonAsset([(0, 20), (0, 0), (8, -15), (16, 0), (16, 20)], thinblueline, blue)
skipper = Sprite(skip, (50, 50))

class skipper(Sprite):
    def __init__(self, position):
        super().__init__(position)
        skip = PolygonAsset([(0, 20), (0, 0), (8, -15), (16, 0), (16, 20)], thinblueline, blue)
        skipper = Sprite(skip, (0,0))
        self.vx = -1
        self.vy = 0
        self.vr = 0
 

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()