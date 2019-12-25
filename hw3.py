'''
Name - Siddhant Bhardwaj

'''
class Jar:
    def __init__(self,N):
        self.capacity = N
        self.space = 0

    def add(self,n):
        if (self.space + n) <= self.capacity:
            self.space += n
        else:
            self.space = self.capacity

    def is_full(self):
        return self.capacity == self.space 

    def __repr__(self):
        return(f"Jar({self.space}/{self.capacity})")    
        


class Counter():
    def __init__(self, nm):
        self._name= nm
        self._count= 0
        self._reset_count = 0
        self.l = []
        self.max_count = 0
        self.click_count = 0
        
    def click(self):
        self._count += 1
        self.l.append(self._count)
        self.max_count = max(self.l)
        self.click_count += 1
    
    def print(self):
        print(f"{self._name}'s count is {self._count}")
    
    def reset(self):
        self._count= 0 
        self._reset_count += 1
        
    
    def count(self):
        return self._count
    
    def is_zero(self):
        return self._count== 0
    
    def __str__(self):
        return f"Counter{self._name}: {self._count}"
    
   
    def name(self):
        return(self._name)
    
    def rename(self,new_name):
        self._name = new_name
        
    def stats(self):
        d = {"clicks": self.click_count, 'max-count': self.max_count ,'resets': self._reset_count}
        
        return(d)
        
    def __repr__(self):
        return f"Counter(name={self._name}, count={self._count})"
    

def fill_interior(array,n):
    x,y = array.shape[0], array.shape[1]
    array[1:x-1,1:y-1] = n
    

def paint_edges(array,color = None):
    x,y = array.shape[0],array.shape[1]
    if color == None:
        array[0,0:y-1] = 1
        array[1:x,0] = 4
        array[0:x-1,y-1] = 2
        array[x-1,1:y] = 3
    else:
        array[0,0:] = color
        array[0:,0] =  color
        array[-1,:] = color
        array[:,-1] = color
        
        
class CounterGroup:
    def __init__(self):
        self.c = {}
        
    def add(self,n):
        if n.name() in self.c:
           return False
        self.c[n.name()] = n 
        return True

    def c2(self):
        l = []
        for ch1,v in sorted(self.c.items()):
            l.append(v)
        return l 
        
    def click_all(self):
        for click in self.c.values():
            click.click()
            
    def znz(self):
        zeroes1 = []
        another = []
        for key in self.c2():
            if key.count() == 0:
               zeroes1.append(key)
            else:
               another.append(key)
               
        return (zeroes1,another)

    def __str__(self):
        l = []
        for ch in self.c2():
            l.append(ch.name())
        return f"|{','.join(l)}|"

    def __repr__(self):
        if len(self.c) == 0:
            return "|<empty>|"
        l = []
        for key in self.c2():
            l.append(repr(key))
        return f"|{','.join(l)}|" 


class Matrix:
    
    def __init__(self,matrix):
        self._m = matrix
        
    def shape(self):
        return (len(self._m),len(self._m[0]))
    
    def get(self,row,col):
        return self._m[row][col]
    
    def set(self,row,col,value):
        self._m[row][col] = value
    
    def __repr__(self):
        result = ""
        row2,col2 = self.shape()
        for r in range(row2):
            line = ""
            for c in range(col2):
                line += f"{self._m[r][c]:4d}"
                
        result += line[:-1] + "\n"
        
        return result[:-1]
        
    def __len__(self):
        ro,cls = self.shape()
        return ro * cls
        
    def __contains__(self,col):
        for ro in self._m:
            if col in ro:
               return True
        return False
    
    def __str__(self):
        row,col = self.shape()
        return f"{row}x{col} Matrix"


def q1():
    return """

>>> import numpy as np
>>> x = np.array([[1,2,3],[4,5]])
>>> x
array([list([1, 2, 3]), list([4, 5])], dtype=object)
>>> x.ndim
1
>>> x.shape
(2,)
>>> x.size
2

When you create an ndarray with np.array but you provide a list of lists where inner lists don't have same length, it doesn't create 
an error. 

The .ndim method results in 1 meaning that it has an array dimension of 1 and has a size of 2 and a shape of 2.

"""

def q2():
    return """

>>> a = np.array([1, 2, 3], dtype='int32')
>>> a.dtype = 'int8'
>>> a
array([1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0], dtype=int8)
>>> a.nbytes
12
>>> a.dtype = 'int16'
>>> a
array([1, 0, 2, 0, 3, 0], dtype=int16)
>>> a.nbytes
12
>>> a.dtype = 'int64'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.
>>> a.dtype = 'float32'
>>> a
array([1.e-45, 3.e-45, 4.e-45], dtype=float32)
>>> a.nbytes
12
>>> a.dtype = 'float64'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: When changing to a larger dtype, its size must be a divisor of the total size in bytes of the last axis of the array.

We notice that when a.dtype is assigned to any value less than 32 or equal to 32 whether in int or float, it raises no ValueError and changes the 
contents of the list accordingly. However, when we try to change dtype to a higher value like 64, it raises a ValueError.also, size of array in terms of bytes does not change with 
change in dtype.

    """
    
def q3():
    return """

>>> d = {1:'banana',2:'apple',3:'tasty'}
>>> d.keys()
dict_keys([1, 2, 3])
>>> d[4] = 'cake'
>>> d
{1: 'banana', 2: 'apple', 3: 'tasty', 4: 'cake'}
>>> d.keys()
dict_keys([1, 2, 3, 4])


Thus, by changing the object produced, we have shown that d.keys() shows a view of the dictiionary keys.
"""

def q4():
    return """
    
a = Counter("test") - creates a counter class with name "test"

a.click() - Resetable object which counts the number of times the Counter object has been clicked.

f([Counter("a"),Counter("b")]) - Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f([Counter("a"),Counter("b")])
NameError: name 'f' is not defined 

The given python code could not be executed because f is not defined.

print([Counter("a"),Counter("b")][0]) - Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(Counter("a"),Counter("b")[0])
TypeError: 'Counter' object is not subscriptable

The given Python code tried to print the Counter object but could not be done because it was not subscriptable.

"""

def q5():
    return """
    
    Why does list slicing produce a view in np.array() ?
    
    """
    
def estimated_hours():
    return 10
    
def observations():
    return """
    
    Not using loops in the HW assignments actually made me write shorter code than before.
    
    """

