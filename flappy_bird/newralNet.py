import numpy as np
import copy
class newral_network:


    def sigmoid(self,x):  
        return 1/(1+np.exp(-x))
    
    def d_sigmoid(self,x):
        # x is sigmoid(x) 
        return x*(1-x)
    

    #making the structre
    def make_network(self ,inputlayer,hiddenlayer): #an array containing no of nurons in hidden layer
        self.N=len(hiddenlayer)
        temp=[]
        weights=[]
        bias=[]
        temp.append(inputlayer)

        for i in range(self.N):
            weights.append(np.random.uniform(-1, 1,(hiddenlayer[i],temp[i])))
            temp.append(hiddenlayer[i])
            bias.append(np.random.uniform(-1,1,(hiddenlayer[i],1)))

        self.gw=copy.deepcopy(weights)
        self.gb=copy.deepcopy(bias) #copyed for temprorly storing gradient value in gradient descent function
        return [weights,bias]
    
    #for calculating the value through newral network
    def forward(self,w,b,x):
        tx=[]
        tx.append(np.row_stack(x))

        for i in range(self.N):
            tx.append(self.sigmoid(b[i]+np.dot(w[i],tx[i])))

        return tx[-1] # only the oputput of last layer
    
    #for back propogation we need the intermediat value too sooo (i didn't wanna mess up what i did earlyer (i'm lazzy))
    def forward_bp(self,w,b,x):
        tx=[]
        tx.append(np.row_stack(x))

        for i in range(self.N):
            tx.append(self.sigmoid(b[i]+np.dot(w[i],tx[i])))

        return tx  # here we return the entire tx



    #calculates error of the predicted and actual values  
    def error(self,w,b,x,y):
        n=len(x)
        err=0
        for i in range(n):
            err+=((y[i])-self.forward(w,b,x[i]))**2
        
        return (err.sum())/n 
    

    
####################################socacstic backpropagation #########################################################

    #gradient descent with back propogation ( socastic )
    def grmsd_s(self,w,b,x,y,lr,n):
        delta_weights=[]
        delta_bias=[]
        # for all data points
        for i in range(len(x)):
            
            fp=self.forward_bp(w,b,x[i])
            out_error=self.d_sigmoid(fp[-1])*(fp[-1]-y[i])
            fp.pop(-1)
          
            for j in range(self.N-1,-1,-1):
                
                weight_err=np.dot(np.row_stack(out_error),np.column_stack(fp[-1]))*lr
                bias_err=out_error*lr

                

                delta_weights.append(weight_err)
                delta_bias.append(bias_err)
                

                out_error=np.dot(w[j].T,np.row_stack(out_error))*self.d_sigmoid(fp[-1])
                fp.pop(-1)

    
            for k in range(self.N):
                w[k]=w[k]-delta_weights[-1]
                b[k]=b[k]-delta_bias[-1]

                delta_bias.pop(-1)
                delta_weights.pop(-1)





        

    #descent algorithm
    def grad_descent_soc(self,w,b,x,y,lr,ep):
        n=len(x)
        for i in range(ep):
            self.grmsd_s(w,b,x,y,lr,n)
            c=self.error(w,b,x,y)
            if i%50==0:
                print(c)
            if c<0.02:
                break

################################################### batch backpropogation ##########################################

    def grmsd_b(self,w,b,x,y,lr,n):
        delta_weights=[]
        delta_bias=[]
        # for all data points
        for i in range(len(x)):
            
            fp=self.forward_bp(w,b,x[i])
            out_error=self.d_sigmoid(fp[-1])*(fp[-1]-y[i])
            fp.pop(-1)
          
            for j in range(self.N-1,-1,-1):

                weight_err=np.dot(np.row_stack(out_error),np.column_stack(fp[-1]))
                bias_err=out_error
               
                if len(delta_weights)<self.N:
                
                    #adding error to delta_weight during first sample
                    delta_weights.append(weight_err)
                    delta_bias.append(bias_err)
                
                else:
                    
                    # addin error of previous delta_weights after the first data sample             
                    delta_weights[(self.N-1)-j]+=weight_err
                    delta_bias[(self.N-1)-j]+=bias_err

                out_error=np.dot(w[j].T,np.row_stack(out_error))*self.d_sigmoid(fp[-1])
                fp.pop(-1)

            
        
        
        #updating weights
        for k in range(self.N):
            w[k]=w[k]-(delta_weights[-1]/n)*lr
            b[k]=b[k]-(delta_bias[-1]/n)*lr

            delta_bias.pop(-1)
            delta_weights.pop(-1)





        

    #descent algorithm
    def grad_descent_batch(self,w,b,x,y,lr,ep):
        n=len(x)
        for i in range(ep):
            self.grmsd_b(w,b,x,y,lr,n)
            c=self.error(w,b,x,y)
            if i%50==0:
                print(c)
            if c<0.03:
                break
    
################################################### finite distance methodee#########################################

    #gradient descent with micro steps
    def grms(self,w,b,x,y,esp,lr):
        err=self.error(w,b,x,y)

        for i in range(self.N):

            for wi in range(len(w[i])):
                for wj in range(len(w[i][wi])):

                    save=w[i][wi][wj]
                    w[i][wi][wj]+=esp
                    self.gw[i][wi][wj]=(self.error(w,b,x,y)-err)/esp
                    w[i][wi][wj]=save

                    #clculating the gradient and putting it on the gw and gb metrix
                
                #since no fo rowos of w and b are same we can use this outer 
                #loop to iterate to b and calculate the gradient of b

                save=b[i][wi][0]
                b[i][wi][0]+=esp
                self.gb[i][wi][0]=(self.error(w,b,x,y)-err)/esp
                b[i][wi][0]=save

        #get out of loop
        for i in range(self.N):
            b[i]=b[i]-lr*self.gb[i]
            w[i]=w[i]-lr*self.gw[i]

        

    #descent algorithm
    def grad_descent_finite(self,w,b,x,y,esp,lr,ep):

        for i in range(ep):
            self.grms(w,b,x,y,esp,lr)
            if i%10==0:

                print(self.error(w,b,x,y))