import pygame as p
from bar import bar

class move_bar:

    def __init__(self,screen,width):
        self.width=width
        self.screen=screen
        self.array=[]


    #slid bars
    def animate(self,rate):
        for i in self.array:
            p.draw.rect(self.screen, (144, 238, 144),[i.x, i.gs1, self.width, i.ge1], 0)
            p.draw.rect(self.screen, (144, 238, 144),[i.x, i.gs2, self.width,i.ge2 ], 0)
            i.x=i.x-rate
        
        for i in self.array:
            if 0>i.x+self.width:
                self.array.remove(i)
       


    #append bar to array
    def put(self,w,h):
        obj=bar(w,h)
        self.array.append(obj)


    #collition detection   
    def collition(self,bird):
   
        for i in self.array:
            if (bird.x+bird.size>=i.x and bird.x-bird.size<=i.x+self.width and  not (bird.y-bird.size>=i.ge1 and bird.y+bird.size<=i.gs2) 
            or bird.y>400):
                return False
            
            if bird.x+bird.size>=i.x and bird.x-bird.size<=i.x+self.width and  (bird.y-bird.size>=i.ge1 and bird.y+bird.size<=i.gs2) and bird.st:
                bird.fitness+=2
                bird.score+=1
                bird.st=False
            
            if bird.x-bird.size>=i.x+self.width:
                bird.st=True
            


        return True



