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
w=256
count=0
toload=[]
for fname in glob('sprites/enemies/*.png'):
    toload.append(transform.scale(image.load(fname),(w,w)))
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    count+=1
    screen.fill(BLACK)
    time.wait(400)
    if count%2==0:
        screen.blit(toload[0],(0,0))
    else:
        screen.blit(toload[1],(0,0))
    
        

    display.flip()
            
quit() 
