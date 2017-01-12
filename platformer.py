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


skip = PolygonAsset([(0, 20), (0, 0), (8, -15), (16, 0), (16, 20)], thinblueline, blue)
skipper = Sprite(skip, (100, 524))

def grnwave(Sprite):
    grnwave.dir = -1.5
     
class floor(Sprite):
    
    grnline = RectangleAsset(5, 50, dgreenline, dgreen)
    
    def __init__
    grnwave((100, 546))
    grnwave((200, 546))
    grnwave((300, 546))
    grnwave((400, 546))
    grnwave((500, 546))
    grnwave((600, 546))
    grnwave((700, 546))
    grnwave((800, 546))
    grnwave((900, 546))
    grnwave((1000, 546))
    grnwave((1100, 546))
    grnwave((1200, 546))

def grnwave(Sprite):
    grnwave.dir = -1.5

class skipper(Sprite):
    def __init__(self, position):
        super().__init__(position)
        self.vx = 2
        self.vy = 2
        self.vr = 0.01
    def step(self):
        self.x += self.vx
        self.y += self.vy
        myapp.listenKeyEvent('keydown', 'uparrow', upKey)
    myapp.listenKeyEvent('keydown', 'leftarrow', leftKey)
    myapp.listenKeyEvent('keydown', 'rightarrow', rightKey)
        
skipper.go = True
  
def step():
    if skipper.go:
        skipper.x += skipper.vx
        skipper.y += skipper.vy
        if skipper.x < 0:
            pass
            


def reverseKey(event):
    reverse(skipper)

def upKey(event):
    self.vy += 3
    
def leftKey(event):
    self.vx -= 2


def rightKey(event):
    self.vy += 2 




myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'r', reverseKey)


myapp.run(step)