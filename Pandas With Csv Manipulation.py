#PERFROM THIS FILE OUT OF THE NUMPY AND PANDAS FOLDER



from io import StringIO
import pandas as pd
import numpy as np

    #WHENEVER WE READ A CSV FILE IT TURNS INTO A DATAFRAME
    # StringIO is a in memory file object which contain a lot of data
# By default comma s a seperator

'''df= pd.read_csv('mercedesbenz.csv')'''


# print (df.head())
# print (df.tail())


# print (df['Name'])              #PRINTS THE COLUMN OF NAME 
# print (df)
# print (df['ID'])

# print (df['ID'][df['X6']=='j'])            #PRINTS THE IDS CORRESPONDING TO THE COLUMN X6 WHOSE VALUE IS EQUALS TO J

# print (df)

'''data = ('col1, col2, col3\n'
        'x,y,2\n'
        'a,b,3\n'
        'c,d,4')'''           #CREATS A STRING FOR THE CSV FILE

# print(type (data))            #PRINTS THE TYPE OF DATA 

# df= (pd.read_csv(StringIO(data)))          #CONVERTS THE STRING TO IN MEMORY FILE

# print(pd.read_csv(StringIO(data)))           #CONVERTS THE DATA INTO CSV FILE IN MEMORY

# print (df.iloc[:4,0:2])             #CONVERTS THE DATA INTO CSV FILE IN MEMORY

# print (pd.read_csv(StringIO(data), usecols=['col1', 'col3']))                 #PRINTS THE DESRIED COLUMNS OF THE FILE

# print (pd.read_csv(StringIO(data), index_col=0))           #REMOVES THE INDEXING OF HTE CSV FILE FROM WHILE DISPLAYING IT IN THE TERMINAL 

# print (df.to_csv('1st.csv', index = False))         #SAVES THE CSV FILE AND REMOVES THE INDEXING INSIDE FILE WITH THE ELEMENTS
# print (pd.read_csv('1st.csv'))


"""data = ('a, b, c, d\n'
        '2,3,4,5\n'
        '6,7,8,9\n'
        '10,11,12, 14')"""

# df = pd.read_csv(StringIO(data))  #CONVERTES THE DTYPE TO OBJECT i.e. STRING 
                                    #IF AN ELEMENT IF ABSENT IN THE COLUMN IT IS SHOWN AS NaN

# print (pd.read_csv(StringIO(data)))

# print (df.isnull())
# print (df.info())
# print (df.describe())
# print (df.isnull().sum())

# print (df['a'][0])                  #PRINTS THE VALUE VALUE OF THE df[1][0]

# print (df.to_csv('1st.csv', index = False))
# print (pd.read_csv('1st.csv', usecols=['b', 'c'], index_col=0))                   #USES THE COLUMN 0 i.e THE index COLUMN AS THE INDEXES OF THE FILE

#https://download.bls.gov/pub/time.series/cu/cu.item           #WEBSITE OF A LARGE CSV FILE 

# print (pd.read_csv('meow.csv', sep = '\t'))


"""EXTRACTING THE ELEMETNS FROM A CSV FILE TO A NUMPY ARRAY TO ACCESS THEM 
ar_ele = df.iloc[2:18, 3:10]

arr = np.array(ar_ele)


for item in arr.flat:
    print (item)"""


# index = pd.date_range("1/1/2000", periods=8)            #GENERATES DATES FOR THE GIVEN PERIOD


'''df=pd.DataFrame({"Name":['Ashok','Iman','MJ'],"Salary":["34k","NIL","56k"],"Age":[23,24,"no_data"]})
df.to_csv('Souvagya.csv', index= False)
print (pd.read_csv('Souvagya.csv', index_col=0))'''


