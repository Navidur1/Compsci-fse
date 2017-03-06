#graphics1.py
from pygame import *
from random import *
from glob import *
init()
    #r   g b
RED  =(255,0,0) 
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
MYYELLOW=(204,224,90)

width,height=1024,512
size=(width,height) 
screen=display.set_mode(size)

display.set_caption("Sprite test")

running=True
w=128
x,y=width//2,height//2
cx,cy=0,0
moving=False
count=0
toload=[]
wasd=[0,0,0,0]
s=4
swing=False
rectcoords=Rect(randint(0,width-w),randint(0,height-w),w,w)
for fname in glob('textures/enemies/*.png'):
    fname=image.load(fname)
    s=w/min(fname.get_height(),fname.get_width())
    toload.append(transform.scale(fname,(int(s*fname.get_width()),int(s*fname.get_height()))))
while running:
    moving=swing=False
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        elif evt.type==KEYDOWN:
            if evt.key==K_w:
                wasd[0]=1
            elif evt.key==K_s:
                wasd[2]=1
            elif evt.key==K_a:
                wasd[1]=1
            elif evt.key==K_d:
                wasd[3]=1
        elif evt.type==KEYUP:
            if evt.key==K_w:
                wasd[0]=0
            elif evt.key==K_a:
                wasd[1]=0
            elif evt.key==K_s:
                wasd[2]=0
            elif evt.key==K_d:
                wasd[3]=0
        elif evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                swing=True
        elif evt.type==MOUSEBUTTONUP:
            if evt.button==1:
                swing=False
    
    cx=(wasd[3]-wasd[1])*s
    cy=(wasd[2]-wasd[0])*s
    x+=cx
    y+=cy
    hitbox=Rect(x-w,y+w//8,w*3//2,w//4)
    if cy!=0 or cx!=0:
        moving=True
    count+=1
    screen.fill(BLACK)
    screen.blit(toload[3],rectcoords)
    draw.rect(screen,BLUE,hitbox,1)
    time.wait(70)
    if swing:
        screen.blit(toload[2],(x-w,y-w//2))
        if hitbox.colliderect(rectcoords):
            rectcoords=(randint(0,width-w),randint(0,height-w),w,w)
    elif moving:
        if count%4==0:
            screen.blit(toload[0],(x-w//2,y-w//2))
        elif count%4==1:
            screen.blit(toload[3],(x-w//2,y-w//2))
        elif count%4==2:
            screen.blit(toload[1],(x-w//2,y-w//2))
        else:
            screen.blit(toload[3],(x-w//2,y-w//2))
    else:
        screen.blit(toload[3],(x-w//2,y-w//2))
     

    display.flip()
            
quit() 
