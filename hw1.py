'''
Name - Siddhant Bhardwaj

'''


def middle(v):
    for i in range(len(v)):
        if i == 1:
            return v[i]
            
def around(n,interval = None):
    result = []
    if interval != None:
        result.extend([n-interval,n,n+interval])
    else:
        result.extend([n-1,n,n+1])
    return tuple(result)
    
def second_biggest(l):
    x = max(l)
    l.remove(x)
    y = max(l)
    return y
    
def contains(m,v):
    l = []
    for r in m:
        for c in r:
            l.append(c)
    if v in l:
        return True
    else:
        return False
        
def get_column(m,v,reverse = None):
    l = []
    if reverse == None or reverse == False:
        for r in range(len(m)):
            for c in range(len(m[r])):
                if c == v:
                    l.append(m[r][c])
                
    else:
        for r in reversed(range(len(m))):
            for c in range(len(m[r])):
                if c == v:
                    l.append(m[r][c])
                elif -c == v:
                    l.append(m[r][-c])
    return(l)
    
def biggest(m):
    l = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            l.append(m[r][c])
    x = max(l)
    return(x)
    
def indices_biggest(m):
    l = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] == biggest(m):
                l.append((r,c))
    return l
    
def indices_divisible_by_3(m):
    l = []
    for r in range(len(m)):
        for c in range(len(m[r])):
            if (r + c) % 3 == 0:
                l.append(m[r][c])
    return l
    
def corners(m):
    r = len(m)
    c = len(m[0])
    l = []
    l.extend([m[0][0],m[0][c-1],m[r-1][c-1],m[r-1][0]])
    return tuple(l)
    
def create_matrix(s):
    a = []
    z = []
    m = []
    x = s.split("/")
    for item in x:
        y = item.split(" ")
        a.append(y)
    for x1 in a:
        x1 = [item for item in x1 if item != '']
        z.append(x1)
    for z1 in z:
        z1 = [int(item) for item in z1]
        m.append(z1)
    return(m)
        
    
def sort_int_string(s):
    a = ''
    x = []
    v = s.split(' ')
    if len(v) > 1:
        for element in v:
            v = [element for element in v if (element != '') and (element != '\n')]
    for element in v:
        x= [element.replace('\t','') for element in v]
    if len(v) > 1:
        x = sorted([int(element) for element in x])
    
    for element in x:
        if (x[0] == element):
            a = a + str(element) + ' '
        elif (x[len(x) - 1] == element):
            a = a + str(element) + ' '
        else:
            a = a + '' + str(element) + ' '
    a = a.rstrip()
    if len(v) > 1:
        return(a)
    elif len(v) == 0:
        return('')
    else:
        for element in v:
            if element.isdigit():
                return(s)
            else:
                return('')
                
def is_diagonal(m):
    if len(m) == 1:
        return True
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i != j) and (m[i][j] != 0):
                return False
                
    return True
    
def is_upper_triangular(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (i > 0) and (j == i - 1):
                if m[i][j] != 0:
                    return False
    return True
    
def print_nzp(m):
    l = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                l.append('z')
            elif m[i][j] < 0:
                l.append('n')
            else:
                l.append('p')
    
    
    print('+' + '-' * ((2 * len(m[0])) - 1) + '+')
    for i in range(0,len(l),len(m[0])):
        print("|" + " ".join(l[i:i + len(m[0])]) + "|")
    print('+' + '-' * ((2 * len(m[0])) - 1) + '+')
    
    
def estimated_hours():
    return(15)
    
def observations():
    return '''
    I learnt more in this assignment than in all previous assignments.
    I especially enjoyed doing problems that forced me to take into account
    multiple challenges. I noticed my weak spots in the is_diagonal function
    and the is_upper_triangular function.
    
    I also applied many things that I had known before but never used and so the experience 
    was made novel by ths fact. I also used multiple built-in methods and utilized them to write smaller 
    code than I had previousy written.
    
    I enjoyed the office hours and truly look forward to Mr.Mitchell's guidance in future classes and 
    assignments. His lucid explanation cleared a lot of my doubts and misconceptions and also
    gave a strong ground to various concepts that I had only superficially understood before.
    
    I was also pleasantly surprised by the newer methods that I learnt about to test specific functions 
    in the powershell and employed them frequently to understand the issues facing me in the code. It was 
    also helpful since it let me focus on the code at hand without being distracted by the other problems in 
    the HW assignment.
    
   '''
   
   
    