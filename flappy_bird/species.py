import numpy as np
import random 

class species:

    def __init__(self,g):
    
        self.members=[]
        self.members.append(g)
        self.length=len(g.brain[0])
        self.trushold=1
        self.champion=g
        self.maxfitness=g.fitness
        self.average_fitness=0


    #add members to species
    def add(self,g):
        self.members.append(g)
        if g.fitness>self.maxfitness:
            self.maxfitness=g.fitness
            self.champion=g



    #sort memebers of species
    def sort_members(self):
        self.members=sorted(self.members, key=lambda x: x.fitness, reverse=True)


    #caluclate average fitness
    def calculate_average_fitness(self):
        if self.members:

            avg=0
            for i in self.members:
                avg+=i.fitness

            self.average_fitness=avg/len(self.members)
  

    
    #mutati the brains of baby
    def mutate(self, baby, mutation_rate):
        # for p in range(len(baby.brain[0])):
        #     r,c=baby.brain[0][p].shape
        #     for i in range(r):
        #         for j in range(c):
        #             if random.uniform(0, 1) > mutation_rate:
        #                 print('yes')
        #                 baby.brain[0][p][i][j]=random.uniform(-1, 1)
        #         if random.uniform(0, 1) > mutation_rate:
        #             print('yes')
        #             baby.brain[0][p][i][1]=random.uniform(-1, 1)

            
        # return baby
            
            





        
        if random.uniform(0, 1) > mutation_rate:
            for i in range(len(baby.brain[0])):
                # Mutate weights
                baby.brain[0][i] += np.random.uniform(-0.05, 0.05, baby.brain[0][i].shape)
                baby.brain[0][i] = np.clip(baby.brain[0][i], -1, 1)

                # Mutate biases
                baby.brain[1][i] += np.random.uniform(-0.5, 0.5, baby.brain[1][i].shape)
                baby.brain[1][i] = np.clip(baby.brain[1][i], -1, 1)

        return baby



    #generate new baby
    def offspring(self):
       
        if len(self.members)>=1:   
            baby=self.members[random.randint(0,len(self.members)-1)]
            baby=self.mutate(baby,0.8)
            baby.fitness=0
            baby.y=400/2

            baby.score=0  
            baby.st=True                     
            baby.velocity=0
            baby.velocityc=5
            baby.event=False
            baby.onflap=False

            return baby

        else :
            return None
    




    #calculate similar brains
    def similar(self,p):

        similarity=0
        
        for l in range(0,self.length):
            for k in range(0,2):
                similarity+=np.sum(np.abs(p.brain[k][l]-self.champion.brain[k][l]))
        return self.trushold>similarity
         
        