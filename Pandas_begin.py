import numpy as np
import pandas as pd


# array = np.array([[1,2,3], [4,5,6], [7,8,9]])

# df = pd.DataFrame (np.arange(20).reshape(5,4), index = ['row1', 'row2', 'row3','row4', 'row5'], columns = ['col1', 'col2', 'col3', 'col4'], dtype= np.int64)

# print(df.head (2))       #PRINTS THE 1st ROW   default takes till 5 

# print(df.tail (2))       #PRINTS THE LAST 2 ROWS

# df_1 = pd.DataFrame({'col1' : [1,2,3], 'col2' : [4,5,6]})     #  DICTIONARY PRINTING 
# print (df_1)

# print (type(df))             #PRINTS THE TYPE OF THE DATAFRAME

# print (df.info())            #PRINTS THE INFO OF THE DATAFRAME

# print (df.describe())          PRINTS THE MEAN, COUNT, STD, MIN, 25%, 50%, 75%, MAX

# print (df[['col1']])         #PRINTS ELEMENTS OF THE FIRST COLUMN

# print (df[['col1', 'col2']])       #PRINTS ELEMENTS OF THE FIRST AND SECOND COLUMN

# print (df.loc[['row1']])          # PRINTS ELEMENT OF THE FRIST ROW

# print (df.loc[['row1', 'row2']])     PRINTS ELEMENTS OF THE FIRST AND SECND ROW

# print  (df.iloc[2:4])            #PRINTS ROWS AFTER 2 TILL 4

# print (df.iloc[2:4, 0:3])                #PRINTS ROWS AFTER 2 TILL 4 AND COLUMNS AFTER 0 TILL 3

# print (np.arange(20).reshape(5,4))

# print (df.iloc[2:4, 0:3].values)         # RETURNS THE ARRAY OF ELEMENTS OF ROWS AFTER 2 TILL 4 AND COLUMNS AFTER 0 TILL 3

# df = pd.DataFrame(data = [[4,np.nan,3], [5,np.nan,5], [6,np.nan,7]], index = ['row1','row2','row3'], columns = ['col1', 'col2', 'col3'])       #CREATES A ARRAY OF COL2 ELEMENRTS HAVING NULL

# print (df.isnull())           # PRINTS TRUE FOR NULL ELEMENTS

# print (df['col1'].value_counts())         #PRINTS THE NO OF TIME OF OCCURANCE OF ELEMENTS IN COLUMN 1

# print (df[['col1','col2']].max())             #PRINTS THE MAXIMUM ELEMENT OF THE COLUMNs

# print (df['col1'].unique())         #PRINTS THE UNIQUE ELEMENTS THUS REMOVING THE REPEAATING ELEMTNS OF COLUMN 1

# print (df['col1'].nunique())         #PRINTS THE NON UNIQUE ELEMENTS THUS REMOVING THE REPEAATING ELEMTNS OF COLUMN 1

# print (df.sum())              #PRINTS THE SUM OF ALL ELEMENTS 

# print (df.isnull().sum())         # PRINTS THE COUNT OF NULL ELEMENTS EACH COLUMN


# Series: When we select either a column or a row
# DataFrame : When we select multiple number of rows and columns 


# print (df)


