from bird import bird
from newralNet import newral_network
import pygame as p
from species import species
import math

class natural_selection:

    popsize=100
   


    def __init__(self,screen,bars):
        self.screen=screen
        self.cgeans=[]
        self.geans=[]
        self.species=[]
        self.net=newral_network()

        #initilize biras population
        
        for _ in range(self.popsize):

            #net inputs  --> bird y, next bar x ,bar gap cpoint 
            # net out 1/0
            self.geans.append(bird(self.screen,140,400,10,0.3,5,self.net.make_network(3,[1])))
            

        #get bar  objets
        self.bars=bars

        self.score=0




    #for classfication
    def classfi(self,input):
        
        if input[0][0]>0.52:
            return 1
        else:
            return 0




    #for finding next bar
    def find_next_bar(sefl,bar_array,birx):
        for bar in bar_array:
            if bar.x>birx:
                return bar
            
        return False
            




    #speciation
    def speciation(self,cgeans):
        for s in self.species:
            s.members=[]

        # print(len(self.species),cgeans[0].fitness)

        for g in cgeans:
            added=False
            
            for s in self.species:
                if s.similar(g):
                    s.add(g)
                    added=True
                    break

            if not added:
                self.species.append(species(g))

        


    #breed
    def breed(self):
        geans=[]
        for s in self.species:
            #just reinizlizing
            x=s.champion
            x.fitness=0
            x.y=400/2
            x.score=0  
            x.st=True                     
            x.velocity=0
            x.velocityc=5
            x.event=False
            x.onflap=False

            geans.append(x)

        #fill rest of children
        rest_of_children=math.floor((self.popsize-len(self.species))/len(self.species))

        for s in self.species:
               
            for _ in range(0,rest_of_children):
                offspring=s.offspring()
                if offspring:
                    geans.append(offspring)

        while len(geans)<self.popsize:
            geans.append(self.species[0].offspring())

        return geans



    #remove poor perfomers
    def remove_poor(self):
        for s in self.species:
            if len(s.members)==0 or s.average_fitness<5: 
                self.species.remove(s)                


    


    #repopulate after extintion    
    def repopulate(self):


        self.speciation(self.cgeans)
        self.cgeans=[]

        #find average fitness/fitness of members for each species
        for s in self.species:
            s.calculate_average_fitness()
            s.sort_members()

        #sort the species according to average fitness
        self.species=sorted(self.species, key=lambda x: x.average_fitness, reverse=True)

        #remove poor perfomers
        # self.remove_poor()

        print(self.species[0].average_fitness,self.species[-1].average_fitness)
        print("len self species=",len(self.species))
        print("best player fitness",self.species[0].members[0].fitness)
        print(self.species[0].members[0].brain)

        
        #breed to get new generation
        self.geans=self.breed() 
          
        
        
    



        
    

    #draw genoms until dead    
    def draw_geneoms(self):

        next_bar=self.find_next_bar(self.bars.array,self.geans[0].x)
        if next_bar:

            for bir in self.geans:

                if bir.score>self.score:
                    self.score=bir.score
            
                
                by=bir.y
                bp_len=(next_bar.x-bir.x)
                ct=(next_bar.cpoint-next_bar.gap)
                cb=(next_bar.cpoint+next_bar.gap)

                p.draw.line(self.screen,start_pos=(bir.x,bir.y),end_pos=(next_bar.x,bir.y),color="White")
                p.draw.line(self.screen,start_pos=(bir.x,bir.y),end_pos=(next_bar.x,ct),color="White")
                p.draw.line(self.screen,start_pos=(bir.x,bir.y),end_pos=(next_bar.x,cb),color="White") 

                # action=self.classfi(self.net.forward(bir.brain[0],bir.brain[1],[by/400,bp_len/(700-bir.x),ct/400,cb/400]))
                prediction=self.net.forward(bir.brain[0],bir.brain[1],[bp_len,(by-ct),(by-cb)])
                action=self.classfi(prediction)
        
                if action==1 and not bir.onflap:                    
                    bir.event=True


                bir.update_evnt()
                bir.draw()
        
    
                if not self.bars.collition(bir):
                    self.cgeans.append(bir)
                    self.geans.remove(bir)


            
            if len(self.geans)==0:    
                self.bars.array=[]    #reset the bars  
                self.repopulate()      #repopulate the geans array 

                self.score=0     
            return self.score

        else:
            return self.score
            
            

       