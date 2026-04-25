from random import *
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,color,x,y,w,h,spd):
        super().__init__()
        self.image = Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = spd
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,color,x,y,w,h,spd):
        super().__init__(color,x,y,w,h,spd)
        self.vel_y = 0
        self.on_ground = True
    def update(self):
        keys = key.get_pressed() 
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_d] and self.rect.x  <win_width-50:
            self.rect.x += self.speed
        if keys[K_SPACE] and self.on_ground:
            self.vel_y = -13
        self.on_ground = False
        self.vel_y += 0.6
        self.rect.y += int(self.vel_y)
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_y > 0:
                    self.rect.bottom = p.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = p.rect.bottom
                    self.vel_y = 0
font.init()
font1 = font.Font(None,36)
mixer.init()
window = display.set_mode((700,500))
win_width = 700
win_height = 500
speed1 = 10
x1 = 50
y1= 405
speed_y = 6
speed2 = 6
display.set_caption('Платформер')
player1=Player((50,50,255),x1,y1,45,45,speed1)
platform = GameSprite((60,179,60),0,450,700,20,0)
platform1 = GameSprite((60,179,60),250,350,200,20,0)
platform2 = GameSprite((60,179,60),450,250,200,20,0)
platform3 = GameSprite((60,179,60),100,200,200,20,0)
platforms = sprite.Group()
platforms.add(platform)
platforms.add(platform1)
platforms.add(platform2)
platforms.add(platform3)
background = transform.scale(image.load('galaxy.jpg'),(700,500))
clock = time.Clock()
FPS = 60
total = 0
finish = False
game = True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish!=True:
        window.blit(background,(0,0))
        platforms.draw(window)
        player1.reset()
        player1.update()
    display.update()
    clock.tick(FPS)