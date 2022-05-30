import matplotlib.pyplot as plt

class Graphics:

    def __init__(self,data):
        self.data=data
    
    def printG(self):
        plt.scatter(self.data[:,0],self.data[:,1])
        plt.show