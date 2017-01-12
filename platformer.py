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
    
    def __init__(self, position, invx, invy):
        super().__init__(floor.grnline, position)
        self.vx = 5
        self.vy = 5
        self.vr = 0
        
    
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        self.vr = .1
        if self.y >= 600 or self.y <= 0:
                self.vy = self.vy*-1
                
        if self.x >= 1200 or self.x <= 0:
            self.vx = self.vx*-1

class skipper(Sprite):
    def __init__(self, position, invx, invy):
        super().__init__(position)
        self.vx = invx
        self.vy = invx
        self.vr = 0.01
    def step(self):
        self.x += self.vx
        self.y += self.vy
        myapp.listenKeyEvent('keydown', 'uparrow', upKey)
        myapp.listenKeyEvent('keydown', 'leftarrow', leftKey)
        sp.listenKeyEvent("keydown", "left arrow", self.left)
        sp.listenKeyEvent("keydown", "left arrow", self.right)
        
        self.x += -2
        self.x += 2
    

skipper.go = True

def step():
    if skipper.go:
        skipper.x += skipper.vx
        skipper.y += skipper.vy
        if skipper.x < 0:
            pass
       
class sp(App):
    def __init__(self, position, invx, invy):
        super().__init__(position)
        self.vx = invx
        self.vy = invx
        
        self.x += self.vx
        self.y += self.vy
        
    sp.g1 = floor((100,550))
    sp.g2 = floor((200,550))
    sp.g3 = floor((300,550))
    sp.g4 = floor((400,550))
    sp.g5 = floor((500,550))
    sp.g6 = floor((600,550))
    sp.g7 = floor((700,550))
    sp.g8 = floor((800,550))
    sp.g9 = floor((900,550))
    sp.g10 = floor((1000,550))
    sp.g11 = floor((1100,550))
    sp.g12 = floor((1200,550))


def reverseKey(event):
    reverse(skipper)

def upKey(event):
    self.vy += -2 
    
def leftKey(event):
    self.vx -= 2


def rightKey(event):
    self.vy += 2 



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'r', reverseKey)


myapp.run(step)