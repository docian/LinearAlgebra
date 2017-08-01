'''
Created on Jul 27, 2017

@author: docian
'''
from math import sqrt 
from math import degrees
from numpy import arccos

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
    
    def times_scalar(self, m):
        if type(m) == 'int' or 'long' or 'float':
            res = []
            for it in self.coordinates:
                res.append(it*m.coordinates[0])
            self.coordinates = res
            return self
        
    def magnitude(self):
        m = 0
        for it in self.coordinates:
            m+=it**2
        return sqrt(m)
    
    def normalize(self):
        try:
            m = Vector([1/self.magnitude()])
            return self.times_scalar(m)
        except ZeroDivisionError:
            raise("cannot normalize vector")
     
    def dot(self, w):
        if type(w) !=  Vector:
            raise TypeError('data is not a vector')
        if self.len != w.len:
            raise TypeError('not the same length for the objects')
        pair  = zip(self.coordinates,w.coordinates)
        dot_prod = [i[0]*i[1] for i in pair]
        return sum(dot_prod)
    
    def angle(self,w, in_degrees = False):
        if type(w) !=  Vector:
            raise TypeError('data is not a vector')
        if self.len != w.len:
            raise TypeError('not the same length for the objects')
        if in_degrees:
            try:
                return degrees(arccos(self.dot(w)/(self.magnitude()*w.magnitude())))
            except:
                ZeroDivisionError("One of the vectors is null")
        else:
            try:
                return arccos(self.dot(w)/(self.magnitude()*w.magnitude())) 
            except:
                ZeroDivisionError("One of the vectors is null")     
               
    def __str__(self):
        return "Vector:{0} of length:{1}".format(self.coordinates, self.len)
        
    def parallel_proj(self, b):
        if type(b) !=  Vector:
            raise TypeError('data is not a vector')
        if self.len != b.len:
            raise TypeError('not the same length for the objects')
        try:
            return self.dot(b)/b.magnitude()
        except:
            ZeroDivisionError("base vector is null vector")
            
    def orthogonal_proj(self,b):
        if type(b) !=  Vector:
            raise TypeError('data is not a vector')
        if self.len != b.len:
            raise TypeError('not the same length for the objects')        
        return sqrt(self.magnitude()**2-(self.parallel_proj(b))**2)
                
if __name__ =='__main__':
    v = Vector([3.039,1.879])
    b = Vector([0.825,2.036])
    print "magnitude of v:{}".format(v.magnitude())
    print "angle between a={} and b={} is:{} degrees".format(v,b,v.angle(b, True))
    print "paralel projection of v={} on b={} is:{}".format(v,b,v.parallel_proj(b))
    print "orthogonal projection of v={} on b={} is:{}".format(v,b,v.orthogonal_proj(b))
    
    