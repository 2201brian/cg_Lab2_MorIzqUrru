import matplotlib.pyplot as plt
import numpy as np

class Utilities_line:
    def __init__ (self,p1,p2):
        self.x1=p1[0]
        self.x2=p2[0]
        self.y1=p1[1]
        self.y2=p2[1]

    def basicIncrementalAlgo(self):
            m=(self.y2-self.y1)/(self.x2-self.x1)
            if abs(m)>1:
                print("Error: pendiente mayor a 1")
            else:
                x=self.x1
                y=self.y1
                listPs=[[x,y]]
                while round(y)!=self.y2:
                    x=x+1
                    y=y+m
                    listPs.append([x,round(y)])
                return listPs
    
    def digitalDiferentialAnalyzer(self):
        dx=self.x2-self.x1
        dy=self.y2-self.y1
        y=self.y1
        x=self.x1
        if abs(dx)> abs(dy):
            steps=abs(dx)
        else:
            steps=abs(dy)
        xinc=dx/steps
        yinc=dy/steps
        listPs=[[x,y]]
        while round(x)!=self.x2:
            x=x+xinc
            y=y+yinc
            listPs.append([round(x),round(y)])
        return listPs

    def bresenhams(self):
        dx=self.x2-self.x1
        dy=self.y2-self.y1
        y=self.y1
        x=self.x1
        pk=2*dy-dx
        listPs=[[x,y]]
        while x!=self.x2:
            if pk>=0:
                pk=pk+2*dy-2*dx
                x=x+1
                y=y+1
                listPs.append([x,y])
            else:
                pk=pk+2*dy
                x=x+1
                listPs.append([x,y])
        return listPs





class Graphics:

    def __init__(self,data):
        self.data=np.array(data)
    
    def printG(self):
        plt.scatter(self.data[:,0],self.data[:,1])
        plt.show

line1=Utilities_line([-1,1],[3,3])
dots_basic=line1.basicIncrementalAlgo()
dots_dda=line1.digitalDiferentialAnalyzer()
graph=Graphics(dots_basic)
graph.printG()
print("basic incremental:",dots_basic)
print("dda:",dots_dda)
print(Utilities_line([3,4],[7,9]).basicIncrementalAlgo())
print(Utilities_line([3,4],[7,9]).digitalDiferentialAnalyzer())
print(Utilities_line([3,4],[7,9]).bresenhams())
#print(Utilities_line([9,18],[14,22]).bresenhams())