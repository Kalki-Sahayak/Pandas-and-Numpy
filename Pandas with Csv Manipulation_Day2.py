import pandas as pd
import numpy as np
from io import StringIO

'''df = pd.DataFrame(
    {
        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
    }
)'''        #IN SERIES TEH FIRST ARGUMENT IS FOR COLUMNS AND HTE REST ARGUMENTS IS FOR ROW NAME ETC.

# row = df.iloc[1]                              #SELECTS ROW 1
# print (row)

# column = df["two"]                              #SELECTS COLUMN 1


# print(df.sub(row, axis="columns"))            #MAKES THE ELEMENTS OF THE SPECIFIED ROW TO 0.
# print(df.sub(row, axis=1))                    #MAKES THE ELEMENTS OF AXIS = 1 0.

# print(df.sub(column, axis="index"))             #MAKES THE ELEMENTS OF THE SPECIFIED COLUMN TO 0.
# print (df.sub(column, axis=0))

# dfmi = df.copy()                             #COPIES TEH DATAFRAME

# dfmi.index = pd.MultiIndex.from_tuples([(1,'a'), (1,'b'), (1,'c'), (2,'a')], names = ['first', 'second'])        #MULTIINDEX DATAFRAME

# column = df['one']
# print(dfmi.sub(column, axis=0, level="second"))                     #MAKES THE ELEMENT OF THE COLUMN 1 0

# print(dfmi)                       #PRINTS THE COPIED DATA FRAME   



# df2 = df.copy()



# df2.loc["a","three"] = 1.0              #SETS THE VALUE OF DF2[a][three] == 1.0000000

# print (df)

# print(df + df2)                         #ADDS TEH ELEMENTS OF THE TWO DATAFRAMES

# print (df2)                             #PRITNS THE SECIND DATAFRAME


'''COMPRAING VALUES OF TWO DATAFRAMES (EQUALS TO , GREATER THAN, LESS THAN, GREATER THAN EQUALS, LESS THAN EQUALS)'''
# df = pd.DataFrame (np.arange(20).reshape(5,4), index = ['row1', 'row2', 'row3','row4', 'row5'], columns = ['col1', 'col2', 'col3', 'col4'], dtype= np.int64)
# print (df)
# df2 = df.copy()
# df2.loc['row1', 'col3'] = 0


# print (df.gt(df2))                  #CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS GREATER TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.
# print (df.eq(df2))                    ##CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS EQAUL TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.
# print(df.ne(df2))                  #CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS NOT EQAUL TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.
# print(df.lt(df2))                   #CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS LESS THAN TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.
# print(df.le(df2))                   #CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS LESS THAN EQAUL TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.
# print(df.ge(df2))                   #CHECKS WETHER THE PARTICULAR ELEMENT OF A DATA IS GREATER THAN EQAUL TO ANOTHER DATA ON THE SAME POSITION OF ANOTHER DATAFRAME.

'''df = pd.DataFrame (np.arange(20).reshape(5,4), index = ['row1', 'row2', 'row3','row4', 'row5'], columns = ['col1', 'col2', 'col3', 'col4'], dtype= np.int64)
print (df.empty)                #CHECKS WEATHER THE DATAFRAME IS EMPTY OR NOT'''

# print((df>0). all())            #CHECKS IF EVERY ELEMENT IS COLUMN SATISFIES THE CONDITION OR NOT

# print((df>0).any())             #CHECK IF ANY ELEMENTS IN THE COLUMN SATISFIES THE CONDITION OR NOT

'''df = pd.DataFrame(np.array([[-1,2,3],[-1,-1,-1]]), index=['row1', 'row2'], columns= ['col1', 'col2', 'col3'])
print(df)
print((df>0).any().any())           #GIVES THE FINAL VALUE IF ANY OF .any() IS TRUE, FINAL VALUE IS TRUE OTHERWISE FALSE'''

# print(df + df == df * 2)              #CHECKS 2+2 = 2*2 (SIMILARLY: DF+DF = DF*2)

# df1 = pd.DataFrame({"col": ["foo", 0, np.nan]})

# df2 = pd.DataFrame({"col": [np.nan, 0, "foo"]}, index=[2, 1, 0])

# print(df1.equals(df2))               #CHECKS WHETHER THE DATA FRAME df1 and df2 are equal or not  '''IF THE DATAS ARE JUMBLED UP IN ANY ONE DATAFRAME WHICH IS BEING COMPARED AND INDEXING IS ALSO JUMBLED IN CORRESPONDING TO THE DATAS IN THE DATAFRAME BUT LOGICALLY THEY AREA EQUAL TO THE DATAFRAME TO WHICH IT IS COMPARED THEN IT WILL GIVE FALSE'''

# print(df1.equals(df2.sort_index()))     #CHECK WHETEHER TEH 2 DATAFRAMES ARE EQUAL OR NOT AFTER SORTING THE INDEX


# print(pd.Series(["foo", "bar", "baz"]) == pd.Index(["foo", "bar", "qux"]))              #CHECKS WHETHER THE ELEMENTS ARE EQUAL TO THE INDEX OF THE ELEMENTS

# df1 = pd.DataFrame({"A": [1.0, np.nan, 3.0, 5.0, np.nan], "B": [np.nan, 2.0, 3.0, np.nan, 6.0]})

# df2 = pd.DataFrame({"A": [5.0, 2.0, 4.0, np.nan, 3.0, 7.0],"B": [np.nan, np.nan, 3.0, 4.0, 6.0, 8.0]})

# print(df1)
# print(df2)
# print (df1.combine_first(df2))             #COMBINING TWO DATAFRAME AND REPLACING THE NULL VALUES WITH NULL ELEMNTS

#GENERAL DATAFRAME COMBINER
'''def combiner(x, y):
    return np.where(pd.isnull(x), y, x)


print(df1.combine(df2, combiner))'''    #DID NOT UNDERSTAND

# df= pd.DataFrame(np.random.randn(12).reshape (4,3), index = ['a', 'b', 'c', 'd'], columns = ['1', '2', '3'])
# print (df)

# print(df.mean(0))      #GIVES THE MEAN ALONG THE COLUMN
# print (df.mean(1))     #GIVES THE MEAN ALONG THE ROWS

'''df = pd.DataFrame(
       {
              "one" : pd.Series(np.random.randn(3), index = ['a', 'b', 'c']),
              "two" : pd.Series(np.random.randn(4), index = ['a', 'b', 'c', 'd']),
              "three" : pd.Series(np.random.randn(3), index = ['b', 'c', 'd'])
       }
)'''

# print (df.sum(0, skipna=False))     #IF A COLUMN IN THE DATAFRAME HAS A NULL INTEGER THEN TEH SUM OF THE COLUMMN BECOMS 0
# df.sum(axis=1, skipna=True)         #IF A COLUMN IN THE DATAFRAME HAS A NULL INTEGER THEN TEH SUM OF THE ROW IS SHOWED IGNORING THE NULL ELEMENT


'''Description

count : Number of non-NA observations

sum: Sum of values

mean : Mean of values

median : Arithmetic median of values

min : Minimum

max : Maximum

mode : Mode

abs : Absolute Value

prod : Product of values

std : Bessel-corrected sample standard deviation

var : Unbiased variance

sem : Standard error of the mean

skew : Sample skewness (3rd moment)

kurt : Sample kurtosis (4th moment)

quantile : Sample quantile (value at %)     

cumsum : Cumulative sum

cumprod : Cumulative product

cummax : Cumulative maximum

cummin : Cumulative minimum'''



# # Create a sample DataFrame
# data = {'A': [1, 2, 3, 4, 5]}
# df = pd.DataFrame(data)

# # Calculate the median (50th percentile)
# median = df['A'].quantile(0.5)

# # Calculate the 25th and 75th percentiles
# q1 = df['A'].quantile(0.25)
# q3 = df['A'].quantile(0.75)

# print("Median:", median)
# print("25th percentile (Q1):", q1)
# print("75th percentile (Q3):", q3)


'''LOWER QUANTILE : (n+1)/4th obs
UPPER QUNATILE    : 3(n+1)/4 th obs'''

# df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
# print(df1)

# print (df1.idxmin(axis=0))                  ##GIVES THE ROW HAVING THE MAXIMUM ELEMNT TO THE CORRESPONDING COLUMN

# print(df1.idxmax(axis=1))                    #GIVES THE COLUMN HAVING THE MAXIMUM ELEMNT TO THE CORRESPONDING ROW


# data = np.random.randint(0, 7, size=50)
# print (data)

# s = pd.Series(data)

# print(s.value_counts())              #COUNTS THE FREQUENCY OF EACH ELEMENT



'''data = {"a": [1, 2, 2, 4], "b": ["x", "x", "y", "y"]}

frame = pd.DataFrame(data)

print(frame['a'].value_counts())''' #COUNTS THE FREQUIENCY OF EACH ELEMENT IN COLUMN 'a'


# s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])

# print (s5.mode())     #ELEMENT HAVING THE HIGHEST FREQUENCY


# df5 = pd.DataFrame(
#     {
#         "A": np.random.randint(0, 7, size=50),
#         "B": np.random.randint(-10, 15, size=50),
#     }
# )

# print (df5.mode())       #GIVES TEH FREQUENCY OF THE ELEMENT WITH MAXIMUM OCCURENCE IN COLUMN A AND B