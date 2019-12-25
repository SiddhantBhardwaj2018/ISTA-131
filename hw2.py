'''
Name - Siddhant Bhardwaj

'''
def first_last(lst):
    return((lst[0],lst[-1]))
    
def dups_dict(dct):
    lst = []
    for value in dct.values():
        for item in value:
            lst.append(item)
    if len(lst) == len(set(lst)):
        return False
    else:
        return True
        
def substr_in_values(dct,string1):
    lst = []
    
    for key in dct.keys():
        for item in dct[key]:
            if string1.lower() in item.lower():
                lst.append(key)
    lst = list(set(lst))
    return(sorted(lst))
    
import string
def four_lines():
    x = str()
    y = str()
    z = str()
    a = str()
    for element in string.ascii_uppercase:
        x += element
    print(x)
    for element1 in string.ascii_lowercase:
        y += element1
    print(y)
    for element2 in range(0,10):
        z += str(element2)
    print(z)
    for element3 in string.printable[62:77]:
        a += element3
    print(a)
    
    
    
def cp_range(string4):
    x = sorted(string4)
    y = ord(max(x))
    z = ord(min(x))
    return((z,y))
    
def mystery(lst):
    '''
    In this function, the program traverses through the list and 
    multiplies the character of first element of the tuple with the 
    integers expressed in binary or other forms and then returns 
    the resultant string.
    '''
    s = ''
    for item in lst:
        s += (chr(item[0]) * item[1])
    return(s)
    

def count_lets(s,all1 = False):
    d = {}
    d1 = {}
    lst = []
    s = sorted(''.join(item for item in s if item.isalnum()).lower())
        
    
       
    for element in s:
            if element not in d:
                d[element] = 1
            else:
                d[element] += 1
        
    
      
    for i in range(97,123):
            c = chr(i)
            if c in d:
                d1[c] = d[c]
            else:
                
                if all1: 
                    d1[c] = 0
    
    for key in d1:
            lst.extend([d1[key],key])
    return(lst)
  
def digit_val(d):
    if d.isdigit():
        return(ord(d) - ord('0'))
    elif d.isalpha():
        d = d.lower()
        return((ord(d) - ord('a')) + 10)
    else:
        return(None)
        
def my_int(s,base = 10):
    
    result = 0
    power = 0
    new = reversed(s)
    for digit in new:
        
        if digit == '-':
            result = (-result)
        elif base == 1:
            result += 1
        else:
            result += digit_val(digit) * base ** power
        power += 1
    return(result)
    

def binhex(n):
    x = bin(n)[2:]
    if len(x) % 4 != 0:
        x = '0' * ((4 - len(x)) % 4) + x
    bin_list = []
    hex_list = []
    for i in range(0,len(x),4):
        bits = x[i:i + 4]
        bin_list.append(bits)
        hex_list.append(f"{int(bits,2):4X}")
    final_string = " ".join(bin_list) + '\n' + " ".join(hex_list)
    return(final_string)    
        
        
def print_index(file):
    f = open(file)
    
    d = {}
    count = 0
    for line in f:
        count += 1
        for word in line.split():
            
            if word not in d:
               d[word] = []
           
            d[word].append(count)
    
    
    x = len(d)
  
    print(str(x) + " unique words: " + ", ".join(sorted(d)))
    print()
    for key in sorted(d):
        
        print(str(key) + ' : ' + str(sorted(set(d[key])))[1:-1])
    f.close()
    
def observations():
    return 
    
    '''
    I truly enjoyed working on these problems. I feel that I am improving with each of these HWs.
    I also appreciate the incredibly help that Mr.Mitchell and all the TAs have provided in clearing my doubts 
    regarding the HW. 
    
    The ord and chr() functions came in handy throughout the class and I learnt how to use the ASCII tables 
    multiple problems. I am also curious as to how Mr.Mitchell came up with a solution for four_lines in 2 
    loops and would like to know if it was possible to do it in one loop.
    
    '''
    
def hours():
    return(9)
    
    