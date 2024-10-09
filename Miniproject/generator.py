import numpy as np
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


count = 0 

class Generator():

    def __init__(self):
        self.x_final=np.array([])
        self.y_final=[]
        self.eq=''

    def show(self):
        global count
        count = count + 1
        plt.plot(self.x_final,self.y_final,color='red',label='y = '+self.eq,linewidth=2)
        plt.plot([0,0],[-50000,50000],color='black',linewidth=1.5)
        plt.plot([-50000,50000],[0,0],color='black',linewidth=1.5)
        plt.xlabel('x-axis -->')
        plt.ylabel('y-axis -->')
        plt.legend()
        plt.grid()
        plt.savefig(r'static\test{}.png'.format(count))
        plt.clf()
        

class Polynomial(Generator):

    def draw(self,eq):
        self.eq=eq
        self.x_final=np.linspace(-500,500,1000)
        for i in range(len(self.x_final)):
            x=self.x_final[i]
            self.y_final.append(eval(eq))
        plt.xlim(-100,100)
        plt.ylim(-9999,9999)
        self.show()

  
class Trignometric(Generator):

    def draw(self,eq):
        self.eq=eq
        self.x_final=np.linspace(-9,9,1000)
        for i in range(len(self.x_final)):
            x=self.x_final[i]
            self.y_final.append(eval('np.{}'.format(eq)))
        plt.xlim(-9,9)
        plt.ylim(-4,4)
        self.show()

class Logarithmic(Generator):

    def draw(self,eq):
        self.eq=eq
        self.x_final=np.linspace(0.0001,1000,10000)
        for i in range(len(self.x_final)):
            x=self.x_final[i]
            self.y_final.append(eval('np.{}'.format(eq)))
        plt.xlim(-2,15)
        plt.ylim(-5,5)
        self.show()


class Exponential(Generator):

    def draw(self,eq):
        self.eq=eq
        self.x_final=np.linspace(-500,500,10000)
        for i in range(len(self.x_final)):
            x=self.x_final[i]
            self.y_final.append(eval(eq))
        plt.xlim(-5,10)
        plt.ylim(-100,750)
        self.show()




