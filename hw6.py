"""
Name: Siddhant Bhardwaj
Contributors: Abhishek Agarwal,Vibhor Mehta,Sriharsha Madhira
"""

import pandas as pd
import numpy as np
def csv_to_dataframe(filename):
    '''
    This function reads a file and creates a dataframe and then returns it.
    '''
    df = pd.read_csv(filename,index_col = 0,decimal = ',')
    return(df)
    
def format_df(df):
    '''
    This function converted items in the Region column of the dataframe into title case and then stripped all leadinga dn
    trailing whitespace. Then, it changes the index by stripping all index countries of their whitespace and
    removing the Countries heading from the index.
    '''
    l = []
    df['Region']=  df['Region'].str.title()
    df['Region'] =  df['Region'].str.strip()
    for item in df.index:
        l.append(item.strip())
    df.set_index(np.array(l),inplace = True)
    
def growth_rate(df):
    '''
    This function creates a new column which subtracts the death rate of a 
    country from its birth rate in order to obtain the growth rate.
    '''
    df['Growth Rate'] =  df['Birthrate'] - df['Deathrate']
    
    
def dod(p, r):     
    num_yrs = 0     
    while p > 2:         
        p = p + p * r / 1000          
        num_yrs += 1     
    return num_yrs 
    
def years_to_extinction(df):
    '''
    This creates a new column which documents how long it would take a country to
    go extinct if it has a negative population growth rate. It creates a NaN series and then replaces
    those values with the no. of years to go extinct if the growth rate is negative.
    '''
    df['Years to Extinction'] =  np.NaN
    for m in df.index:
        x = df.index.get_loc(m)
       
        if df.iloc[x,-2] < 0:
            y = dod(df.iloc[x,1],df.iloc[x,-2])
            df.iloc[x,-1] = y
        
def dying_countries(df):
    '''
    This creates a new Series with all the countries that have some years to go extinct
    and gives the Series in an ascending order.    
    '''
    y = df['Years to Extinction'].dropna().sort_values()
    return(y)
    
def main():
    '''
    This main function creates a dataframe from countries_of_the_world.csv file, formats it
    , adds the growth_rate and years_to_extinction columns and then prints the top 5
    countries to go extinct.
    '''
    df = pd.read_csv('countries_of_the_world.csv',index_col = 0,decimal = ',')   
    format_df(df)
    growth_rate(df)
    years_to_extinction(df)
    y = df['Years to Extinction'].dropna().sort_values().head(5)
    for i in y.index:
        print(str(i) + ': ' + str(y[i]) + " Years to Extinction")