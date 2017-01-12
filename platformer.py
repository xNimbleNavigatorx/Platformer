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
dgreenline = LineStyle(2, dgreen)
boundary = RectangleAsset(SCREEN_WIDTH-3, SCREEN_HEIGHT-3, thinblackline, white)
boundary1 = Sprite(boundary, (1,1))

ground = RectangleAsset(SCREEN_WIDTH-8, 50, greenline, lgreen)
ground1 = Sprite(ground, (4, SCREEN_HEIGHT-54))

grnwave = RectangleAsset(5, 50, dgreenline, dgreen)
grnline1 = Sprite(grnwave, (100, 546))
grnline2 = Sprite(grnwave, (200, 546))
grnline3 = Sprite(grnwave, (300, 546))
grnline4 = Sprite(grnwave, (400, 546))
grnline5 = Sprite(grnwave, (500, 546))
grnline6 = Sprite(grnwave, (600, 546))
grnline7 = Sprite(grnwave, (700, 546))
grnline8 = Sprite(grnwave, (800, 546))
grnline9 = Sprite(grnwave, (900, 546))
grnline10 = Sprite(grnwave, (1000, 546))
grnline11 = Sprite(grnwave, (1100, 546))
grnline12 = Sprite(grnwave, (1200, 546))

grnline1.dir = -1.5
grnline2.dir = -1.5
grnline3.dir = -1.5
grnline4.dir = -1.5
grnline5.dir = -1.5
grnline6.dir = -1.5
grnline7.dir = -1.5
grnline8.dir = -1.5
grnline9.dir = -1.5
grnline10.dir = -1.5
grnline11.dir = -1.5
grnline12.dir = -1.5

grnline1.go = True
grnline2.go = True
grnline3.go = True
grnline4.go = True
grnline5.go = True
grnline6.go = True
grnline7.go = True
grnline8.go = True
grnline9.go = True
grnline10.go = True
grnline11.go = True
grnline12.go = True

def step():
    if grnline1.go:
        grnline1.x += grnline1.dir
        if grnline1.x + grnline1.width > SCREEN_WIDTH or grnline1.x < 0:
            grnline1.x == 0
            reverse(grnline1)

skip = PolygonAsset([(0, 20), (0, 0), (8, -15), (16, 0), (16, 20)], thinblueline, blue)
skipper = Sprite(skip, (100, 524))

skipper.dir = 4
skipper.go = True

def reverse(b):
    b.dir *= -1

def step():
    if skipper.go:
        skipper.x += skipper.dir
        if skipper.x + skipper.width > SCREEN_WIDTH or skipper.x < 0:
            skipper.x == 0
            reverse(skipper)
            

def reverseKey(event):
    reverse(skipper)


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.run(step)