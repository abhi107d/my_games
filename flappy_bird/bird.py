import pygame as p
import random 
class bird:

    def __init__(self,screen,x,sh,size,gravity,velocity,brain):
        #screen info
        self.x=x
        self.h=sh
        self.y=sh/2
        self.screen=screen
        self.size=size

        #bird movments
        self.gravity=gravity
        self.velocity=0
        self.velocityc=velocity
        self.maxv=8
        self.event=False
        self.fitness=0
        self.onflap=False

        #scor
        self.score=0
        self.st=True


        #brain
        self.brain=[brain[0],brain[1]]

        #color 
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
 
        p.draw.circle(self.screen,self.color,[self.x,self.y],self.size)



    def update_evnt(self):
            

        #making velocity to jump          
        if self.event:           
            self.velocity=-1*self.velocityc
            self.event=False
            self.onflap=True

        if self.velocity>=0:
            self.onflap=False


        #check for above the screen
        if self.y<0:

            self.fitness-=1
            if self.fitness<0:
                self.fitness=0
            self.velocity=1

        #incrimenting fitness
        else:
            self.fitness+=0.1


        #fall/jump update
        self.velocity+=self.gravity       
        self.y=self.y+self.velocity


         #terminal velocity /air resistance
        if self.velocity>self.maxv:
            self.velocity=8




