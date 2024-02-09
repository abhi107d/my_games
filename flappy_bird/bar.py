import random
class bar:
    def __init__(self,w,h):
        self.w=w
        self.h=h
        self.x=w
    
        
        self.cpoint=random.randint(self.h/4,self.h-(self.h/4))
    
        self.gap=50
        self.gs1=0
        self.ge1=self.cpoint-self.gap
        self.gs2=self.cpoint+self.gap
        self.ge2=self.h
