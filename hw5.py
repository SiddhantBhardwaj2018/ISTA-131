
'''
Name -  Siddhant Bhardwaj
Contributors -  Vibhor Mehta, Rob Lucha, Abhishek Agarwal
'''


import pandas as pd
from datetime import timedelta  

def read_frame():
    df = pd.read_csv('sunrise_sunset.csv',index_col = 0, names = ['Jan_r','Jan_s','Feb_r','Feb_s','Mar_r','Mar_s','Apr_r','Apr_s','May_r','May_s','Jun_r','Jun_s','Jul_r','Jul_s','Aug_r','Aug_s','Sep_r','Sep_s','Oct_r','Oct_s','Nov_r','Nov_s','Dec_r','Dec_s'],dtype = str)
    return(df)
    
def get_series(df):
    mths = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    rise = pd.concat([df[m + '_r'] for m in mths])
    set = pd.concat([df[m + '_s'] for m in mths])
    rise.dropna(inplace = True)
    set.dropna(inplace = True)
    date = pd.date_range('010118','123118')
    set.index = date
    rise.index = date
    return rise, set
    
def longest_day(rise,set):
    '''
    
    '''
    rise_new = rise.astype(int)
    set_new = set.astype(int)
    diff = set_new - rise_new 
    return(diff.idxmax(),str(diff[diff.idxmax()]))

def sunrise_dif(rise,timestamp):
    '''
    
    '''
    rise_new = rise.astype(int)// 100 * 60 +  rise.astype(int) % 100
    
    before_90 = timestamp - timedelta(90)
    after_90 = timestamp + timedelta(90)
    return(rise_new.loc[before_90] - rise_new.loc[after_90]) 
    