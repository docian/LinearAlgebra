'''
Created on Jul 27, 2017

@author: docian
'''

class Vector(object):
    '''
    classdocs
    '''


    def __init__(self, coords):
        '''
        Constructor
        '''
        if coords == None:
            raise ValueError
        self.coordinates = tuple(coords)
        self.len = len(self.coordinates)
    
    def __add__(self, w):
        if type(w) != type(self):
            raise TypeError
        if self.len !=  w.len:
            raise ValueError('vectors length are different')
        res=[]
        for i in range(self.len):            
            res.append(self.coordinates[i] + w.coordinates[i])
        self.coordinates = res
        return self
    
    def __sub__(self,w):
        if type(w) != type(self):
            raise TypeError
        if self.len !=  w.len:
            raise ValueError('vectors length are different')
        res=[]
        for i in range(self.len):            
            res.append(self.coordinates[i] - w.coordinates[i])
        self.coordinates = res
        return self 
    
    def __mul__(self, m):
        if type(m) == 'int' or 'long' or 'float':
            res = []
            for it in self.coordinates:
                res.append(it*m.coordinates[0])
            self.coordinates = res
            return self
               
    def __str__(self):
        return "Vector:{0} of length:{1}".format(self.coordinates, self.len)
        
        
if __name__ =='__main__':
    a = Vector([8.218,-9.341])
    b = Vector([-1.129,2.111])
    print "sum:{}".format(a+b)
    a = Vector([7.119,8.215])
    b = Vector([-8.223,0.878])
    print "diff:{}".format(a-b)
    a = Vector([7.41])
    b = Vector([1.671,-1.012,-0.318])
    v = b*a
    print "mul:{}".format(v)

    