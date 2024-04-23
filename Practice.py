import numpy as np

# array  =np.arange(15). reshape (5,3)      CREATES A HOMOGENOUS MATRIX AND RESHAPE SHAPE THE 1D ARRAY INTO THE DESRIED DIMENESION MENTIONED IN THE BREACKETS

# print (array.ndim)       GIVES THE DIMESNISON OF THE ARRAY i.e. 1D, 2D, 3D etc.

# print (array.max())      GIVES THE MAXIMUM ELEMENT IN THE ARRAY

# print (array.dtype)      GIVES THE DATATYPE OF THE ARRAY

# print (array.shape)      GIVES THE ORDER OF THE MATRIX

# array = np.array ([[1,2,3], 
#                    [4,5,6], 
#                    [7,1,0]])  


# array = np.identity(5)   CREATES THE IDENTITY MATRIX OF THE GIVEN ORDER

# array = np.zeros(6).reshape (2,3)      CREATES A 1D ARRAY WITH ZEROS COUNTED WITHIN THE BRACKETS (ARRAY CREATED HAS A FLOAT DATATYPE)

# print (array.sum(axis= 1))       GIVES SUM OF ALL ELEMENTS IN A ROWISE FORMAT AND WHEN (AXIS = 0): GIVES SUM IN A COLUMN WISE MANNER

# print (array.T)          GIVES THE TRANSPOSE OF A MATRIX


# arr = array.flat
# for item in arr:
#     print (item)        HELP US TO ACCESS EACH AND EVERY ELEMENT FROM TEH ARRAY IN AN ITERABLE FORMAT



# print (array.size)        GIVES THE TOTAL NUMBER OF ELEMENTS 

# print (array.argsort())     GIVES THE INDEX OF THE ARRAY ELEMENTS FOR EACH ROW ACCORING TO THEIR MAGNITUDE (EX: ROW 1= [1,3,2] IT WILL RETURN [0,2,1] BUT FRO [1,2,3] IT WILL RETURN [0,1,2])
  
# print(array.nbytes)      GIVES TEH TOTAL SIZE OF THE ARRAY ( SUPPOSE FOR A 3X3 MATRIX CONTAINING INTEGER DATATYPE IT WILL RETURN 36 { 4(SIZE OF INT) * 9(NUMBER OF ELEMENTS IN THE ARRAY)})

# print (array.ravel())    CREATE A MULTIDIMENSIONAL ARRAY INTO A 1D ARRAY

# print (array.argmax())     GIVES THE INDEX OF THE MAXIMUM ELEMENT AFTER RAVELLING THE ARRAY TO 1D AND SIMILAR IS WITH argmin(): GIVES THE INDEX OF THE LOWEST ELEMENT

# print (array.argmax(axis =0))      GIVES THE INDEX OF THE LARGEST ELEMENT OF EACH COLUMN AND AXIS = 1 GIVES THE INDEX OF THE HIGEHST ELEMENT OF EACH ROW
 
# arr = np.array ([[2,3,1], [1,1,1], [0,0,0]])

# print (arr+array)          GIVES THE SUM OF 2 ARRAYS

# print ([2,3]+[4,1])          CONCATENATES THE TWO MATRIX AND MAKES THEM ONE

# print (np.linspace (1,5,4))       PRINTS 4 ELEMEENTS FROM 1 TO 5 HAVING EQUAL SPACES

# print (np.sqrt (array))     GIVES THE SQUARE ROOT OF EACH ELEMETNS OF THE ARRAY

# print (np.where (array>5))      RETURNS A TUPLE OF ELEMENTS GREATER THAN 5

# print (np.count_nonzero(array))       GIVES THE NUMBER OF NONZERO ELEMENTS IN TEH ARRAY in a tuple

# array[1,2] = 0

# print (np.nonzero(array))         GIVES US DIFFERENT TUPLES FOR DIFFERENT DIMENSIONS WHICH ARE NON-ZERO 

# print (np.itemsize())           GIVES THE DATATYPE DIVIDED BY 8

# print (array)