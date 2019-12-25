'''
Name -  Siddhant Bhardwaj
Contributors - Vibhor Mehta,Abhishek Agarwal
'''
import numpy as np
def sums(array):
    x,y = array.shape[0],array.shape[1]
    return(np.sum(array,axis = 1),np.sum(array,axis = 0),np.sum(array))
    
def fvr(a,order = "C"):
   
    if order.upper() == "C":
        return(a.T.reshape((a.size,),order = "F"))
    elif order.upper() == "F":
        return(a.T.reshape((a.size,),order = "C"))
        
def znm(a,rows = True):
    l = []
    if rows:
        for row in a:
            row1 = [row[x] if x == np.argmax(row) else 0 for x in range(len(row))]
            l.append(row1)
        return(np.array(l))
    
    for col in a.T:
        col1 = [col[x] if x == np.argmax(col) else 0 for x in range(len(col))]
        l.append(col1)
    return(np.array(l).T)
    
def concentrate(a,n):
    r,c = a.shape[0],a.shape[1]
    for k in range(0,r,n):
        for l in range(0,c,n):
            d = a[k:k + n, l:l + n]
            value = d.sum()
            d[:,:] = 0
            d[(n-1)//2,(n-1)//2] = value
           
    return(a.copy())
    
def check_sdk(a):
    if all([check_rows("row(s)",a),check_rows("column(s)",a.T),check_squares(a)]):
       print("OK!")
       
def make_board(s):
    board = np.empty((9,9),dtype="int8")
    for r in range(9):
        for c in range(9):
            while not ('0' <= s[0] <= '9'):
                s = s[1:]
            board[r,c] = s[0]
            s = s[1:]

    return board
    
def check_19(a):
    return sorted(a) == list(range(1,10))
    
def check_rows(which,board):
    
    lst = []
    correct = list(range(1,10))
    for row in range(9):
        if not check_19(board[row]):
           lst.append(str(row + 1))
    if lst != []:
       print(f"Bad {which}: " + " ".join(lst))
    return lst == []

def check_squares(board):
    bad = []
    for r in range(0,9,3):
        for c in range(0,9,3):
            square = board[r:r+3,c:c+3]
            if not check_19(square.flatten()):
                bad.append(f"{r+1,c+1}")
    if bad != []:
       print(f"Bad square(s): " + " ".join(bad))
    return bad == []
                                

        

 




def q1():
   return """
   In order to obtain how many columns we need given N values and R rows, the way
   to find that out would be np.array(range(N)).reshape(R,N//R)
   
   Example from interaction:
    >>> import numpy as np
    >>> np.array(range(12)).reshape(3,12//3)
    array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
       
    """
    
def q2():
    return """
    The said method is .cumsum() which cumulatively sums up all the items in the ndarray.
    
    Example of interaction:
    >>> a = np.array(range(10)).cumsum()
>>> a
array([ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)
   """
   
def q3():
    return """
    
    a = np.arange(100,125).reshape(5,5)
    
    Translation - It creates an ndarray of row and column size equal to 5 respectively
    and the values in the array are in the range from 100 to 124.
    
    
    a += 5
    
    Translation - It adds 5 to all items in the ndarray a.
    
    print(a[-3:,1:])
    
    Translation - This line prints the portion of the ndarray a from the third last row onwards and the 2nd column onwards.
    
    a[:,a.shape[1]//2] = a.sum()
    
    Translation - The line places the sum of the entire array in that column of the array which is the middle most column of the array.
    
    """
    
def q4():
    return """
    How is numpy different from pandas ?
    """
    
