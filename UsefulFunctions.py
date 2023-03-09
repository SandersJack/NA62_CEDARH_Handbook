import numpy as np

class UsefulFunctions():
    
    def __init__(self, Cedar):
        self.cedarClass = Cedar
        
        
    def Tamm(self,lam):
        beta = np.sqrt(1-(0.497611/75)**2)
        eq = ((2*np.pi*(1/137))/lam**2)*(1-(1/(self.cedarClass.nindex(lam)**2*beta**2)))
        
        return eq