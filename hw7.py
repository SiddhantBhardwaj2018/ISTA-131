"""
Name: Siddhant Bhardwaj
Contributors: Abhishek Agarwal,Vibhor Mehta
"""

import pandas as pd
import numpy as np
import datetime as datetime
def get_data():
    '''
    This function returns a series from the "N_seaice_extent_daily_v3.0.csv" data .
    '''
    df = pd.read_csv("N_seaice_extent_daily_v3.0.csv",usecols = [0,1,2,3],skiprows = [0,1],names = ['Year', 'Month', 'Day', 'Extent'])
    df['Date'] = pd.to_datetime(df[['Year','Month','Day']])
    data = [i for i in df.Extent]
    column = [pd.Timestamp(i) for i in df.Date]
    s = pd.Series(data, column)
    s = (s.asfreq('D'))
    return(s)
    
def clean_data(s):
    '''
    Ths function cleans the data from the series and alters it in place by adding the missing data.
    '''
    for i in range (len(s.index)):
        if np.isnan(s[i]):
            if ( not(np.isnan(s[i-1])) and not(np.isnan(s[i+1])) ):
                   s[i] = ( s[i-1] + s[i+1]) / 2
    for i in range (len(s.index)):
        if np.isnan(s[i]):
            if (s.index[i].month == 2 and s.index[i].day == 29):
                s[i] = 0.0
            else:
                date_lastyr = datetime.datetime(s.index[i].year -  1, s.index[i].month, s.index[i].day)
                value_lastyr = s[date_lastyr]
                date_nextyr = datetime.datetime(s.index[i].year +  1, s.index[i].month, s.index[i].day)
                value_nextyr = s[date_nextyr]
                s[i] = (value_lastyr + value_nextyr) /2
                
def get_column_labels():
    '''
    This function returns a list of strings that form te column labels of the dataframe.
    '''
    return(["0101", "0102", "0103", "0104", "0105", "0106", "0107", "0108", "0109", "0110", "0111", "0112", "0113", "0114", "0115", "0116", "0117", "0118", "0119", "0120", "0121", "0122", "0123", "0124", "0125", "0126", "0127", "0128", "0129", "0130", "0131", "0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209", "0210", "0211", "0212", "0213", "0214", "0215", "0216", "0217", "0218", "0219", "0220", "0221", "0222", "0223", "0224", "0225", "0226", "0227", "0228", "0301", "0302", "0303", "0304", "0305", "0306", "0307", "0308", "0309", "0310", "0311", "0312", "0313", "0314", "0315", "0316", "0317", "0318", "0319", "0320", "0321", "0322", "0323", "0324", "0325", "0326", "0327", "0328", "0329", "0330", "0331", "0401", "0402", "0403", "0404", "0405", "0406", "0407", "0408", "0409", "0410", "0411", "0412", "0413", "0414", "0415", "0416", "0417", "0418", "0419", "0420", "0421", "0422", "0423", "0424", "0425", "0426", "0427", "0428", "0429", "0430", "0501", "0502", "0503", "0504", "0505", "0506", "0507", "0508", "0509", "0510", "0511", "0512", "0513", "0514", "0515", "0516", "0517", "0518", "0519", "0520", "0521", "0522", "0523", "0524", "0525", "0526", "0527", "0528", "0529", "0530", "0531", "0601", "0602", "0603", "0604", "0605", "0606", "0607", "0608", "0609", "0610", "0611", "0612", "0613", "0614", "0615", "0616", "0617", "0618", "0619", "0620", "0621", "0622", "0623", "0624", "0625", "0626", "0627", "0628", "0629", "0630", "0701", "0702", "0703", "0704", "0705", "0706", "0707", "0708", "0709", "0710", "0711", "0712", "0713", "0714", "0715", "0716", "0717", "0718", "0719", "0720", "0721", "0722", "0723", "0724", "0725", "0726", "0727", "0728", "0729", "0730", "0731", "0801", "0802", "0803", "0804", "0805", "0806", "0807", "0808", "0809", "0810", "0811", "0812", "0813", "0814", "0815", "0816", "0817", "0818", "0819", "0820", "0821", "0822", "0823", "0824", "0825", "0826", "0827", "0828", "0829", "0830", "0831", "0901", "0902", "0903", "0904", "0905", "0906", "0907", "0908", "0909", "0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919", "0920", "0921", "0922", "0923", "0924", "0925", "0926", "0927", "0928", "0929", "0930", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1022", "1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120", "1121", "1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231"])
        

def extract_df(s):
    '''
    This function takes a the series and creates a new dataframe with the years as the row labels and the strings from column_labels as 
    the columns and then fills in the dataframe  with the appropriate values.
    '''
    col = get_column_labels()
    ind = [i for i in range ( 1979 , 2019)]
    df2 = pd.DataFrame(data = np.NaN , index = ind , columns = col , dtype = np.float64)
    for i in df2.index:
        for j in df2.columns:
            time_prev = datetime.datetime(int(i), int(j[:2]), int(j[2:]))
            if (time_prev in s.index):
                df2.loc[ i , j] = s[time_prev]
    return df2
    
def extract_2019(s):
    '''
    This function returns a series containing the data for 2019 with dates as labels and 
    '''
    dt = [s[i] for i in s.index[14677:]]
    ind  = [i for i in  s.index[14677:]]
    s_2019 = pd.Series(data  = dt , index = ind,dtype = np.float64)
    return(s_2019)
    
def main():
    '''
    This data obtains the data we need, then cleans it and stores it to disk in the files - 'data_79_18.csv' and  'data_2019.csv'
    '''
    ser = get_data()
    clean_data(ser)
    df = extract_df(ser)
    ser_19  = extract_2019(ser)
    df.to_csv( path_or_buf = 'data_79_18.csv' )
    ser_19.to_csv( path_or_buf = 'data_2019.csv' )
    
main()