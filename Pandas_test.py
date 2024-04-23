import pandas as pd
import numpy as np
from io import StringIO

data = ('col1, col2, col3\n'
        'x,y,2\n'
        'a,b,3\n'
        'c,d,4')   

print(pd.read_csv(StringIO(data)))

print (pd.read_csv(StringIO(data), usecols=['col1', 'col3']))