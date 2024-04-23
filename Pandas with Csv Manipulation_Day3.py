import pandas as pd
import numpy as np
from io import StringIO


'''df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3]
)


df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7]
)


df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },index=[8, 9, 10, 11]
)'''


# frames = [df1, df2, df3]

# print (pd.concat(frames))                   #CONCATS THE DATAFRAMES '''AFTER CRATING A LIST OF DATAFRAMES'''

'''concat() makes a full copy of the data, and iteratively reusing concat() can create unnecessary copies. Collect all DataFrame or Series objects in a list before using concat().

frames = [process_your_file'''

'''df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7]
)'''


# result = pd.concat([df1, df4], axis=1)
# print (result)                            #CONCATS TEH DATAFRAMES ROWWISE PATTERN

#OUTPUT    
'''    A    B    C    D    B    D    F
   0   A0   B0   C0   D0  NaN  NaN  NaN
   1   A1   B1   C1   D1  NaN  NaN  NaN
   2   A2   B2   C2   D2   B2   D2   F2
   3   A3   B3   C3   D3   B3   D3   F3
   6  NaN  NaN  NaN  NaN   B6   D6   F6
   7  NaN  NaN  NaN  NaN   B7   D7   F7'''


# result = pd.concat([df1, df4], axis=1, join="inner")
# print (result)       #GIVES THE INTERSECTION OF TEHE ROWS THAT ARE IN COMMON



#OUTPUT
'''   A   B   C   D   B   D   F
   2  A2  B2  C2  D2  B2  D2  F2
   3  A3  B3  C3  D3  B3  D3  F3'''

# result = pd.concat([df1, df4], axis=1).reindex(df1.index)
# print(result)                               #REINDEXIFIES ANY DATAFRAME WITH RESPECT TO DATAFRAME 1

#OUTPUT
'''    A   B   C   D    B    D    F
    0  A0  B0  C0  D0  NaN  NaN  NaN
    1  A1  B1  C1  D1  NaN  NaN  NaN
    2  A2  B2  C2  D2   B2   D2   F2
    3  A3  B3  C3  D3   B3   D3   F3'''


# result =pd.concat([df1, df4],ignore_index=True, sort=True)
# print(result)                           #REINDEXIFIES THE INDEXES FROM 0 TO N-1

#OUTPUTS
'''    A   B    C   D    F
    0   A0  B0   C0  D0  NaN
    1   A1  B1   C1  D1  NaN
    2   A2  B2   C2  D2  NaN
    3   A3  B3   C3  D3  NaN
    4  NaN  B2  NaN  D2   F2
    5  NaN  B3  NaN  D3   F3
    6  NaN  B6  NaN  D6   F6
    7  NaN  B7  NaN  D7   F7'''


# s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")

# result = pd.concat([df1, s1], axis=1)
# print (result)                      #CONCATS THE SERIES AND THE DATAFRAME


'''    A   B   C   D   X
    0  A0  B0  C0  D0  X0
    1  A1  B1  C1  D1  X1
    2  A2  B2  C2  D2  X2
    3  A3  B3  C3  D3  X3'''



# result = pd.concat(frames, keys=["x", "y", "z"])
# print(result)           #SETS THE INDEXES ACCORDING TO THE DIFFERENT DARTAFRAMES         


#OUTPUT
'''        A    B    C    D
    x 0    A0   B0   C0   D0
      1    A1   B1   C1   D1
      2    A2   B2   C2   D2
      3    A3   B3   C3   D3
    y 4    A4   B4   C4   D4
      5    A5   B5   C5   D5
      6    A6   B6   C6   D6
      7    A7   B7   C7   D7
    z 8    A8   B8   C8   D8
      9    A9   B9   C9   D9
      10  A10  B10  C10  D10
      11  A11  B11  C11  D11'''


# s3 = pd.Series([0, 1, 2, 3], name="foo")

# s4 = pd.Series([0, 1, 2, 3])

# s5 = pd.Series([0, 1, 4, 5])

# print(pd.concat([s3, s4, s5], axis=1)) # concat 3 pd series wrt axis
# print(pd.concat([s3, s4, s5], axis=1, keys = ['red', 'blue', 'yelllow'])) # Same as above, specifying the keys



#OUTPUT
'''    foo  0  1
    0    0  0  0
    1    1  1  1
    2    2  2  4
    3    3  3  5
    red  blue  yelllow
    0    0     0        0
    1    1     1        1
    2    2     2        4
    3    3     3        5'''


# s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])

# result = pd.concat([df1, s2.to_frame().T]'''Converts the series to a df''', ignore_index=True)
# print (result)                              # Concatenates the 2 dataframes and prints the transpose



#OUTPUT
'''    A   B   C   D
    0  A0  B0  C0  D0
    1  A1  B1  C1  D1
    2  A2  B2  C2  D2
    3  A3  B3  C3  D3
    4  X0  X1  X2  X3'''


left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)


# result = pd.merge(left, right, on="key")             # Merge the 2 dataframes on basis of key values
# print(result)


# OUTPUT
'''    key   A   B   C   D
    0  K0  A0  B0  C0  D0
    1  K1  A1  B1  C1  D1
    2  K2  A2  B2  C2  D2
    3  K3  A3  B3  C3  D3'''


import pandas as pd

# Create two DataFrames
# df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# df2 = pd.DataFrame({'A': [1, 7, 8], 'C': [9, 10, 11]})

# # Merge the two DataFrames using an inner join
# df3 = pd.merge(df1, df2, on='A', how='inner')             # Merges the dataframes wrt to the common element either in A or B or C

# print(df1)
# print(df2)
# # Print the merged DataFrame
# print(df3)

#OUTPUT     #THE CORRESPONDING ELEMENTS FOR THE COMMON ELEMENT ARE ALSO DISPLAYED
'''    A  B
    0  1  4
    1  2  5
    2  3  6
    A   C
    0  1   9
    1  7  10
    2  8  11
    A  B  C
    0  1  4  9'''



# left = pd.DataFrame({"A": [1, 2], "B": [2, 2]})

# right = pd.DataFrame({"A": [4, 5, 6], "B": [2, 2, 2]})

# result = pd.merge(left, right, on="A", how="outer")

# print(result)