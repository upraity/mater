#Matrix 

class Matrix:
    
    def __init__(matrix, nums: list[list[int, float]]):
        if not all(len(nums[0]) == len(l) for l in nums):
            raise Exception("Invalid Matrix formate")
        
        matrix.rows = len(nums)
        matrix.columns = len(nums[0])
        matrix.shape = (matrix.rows, matrix.columns)
        matrix.values = nums
        
    def __str__(matrix):
        return str(matrix.values).replace(" ", "").replace("[[", "").replace("],[", "\n").replace(",", " ").replace("]]", "")
    
    def __repr__(matrix):
        return "<Matrix object " + str(matrix.rows) + "x" + str(matrix.columns) +  ">"
            
    def __eq__(matrix, B):
        return matrix.values == B.values
    
    def __add__(matrix, B):
        if matrix.shape != B.shape:
            raise Excaption("Matrix can't be added of defrent sizes.")
        C = Matrix([[0]*B.columns for _ in range(B.rows)])
        for i in range(C.rows):
            for j in range(C.columns):
                C.values[i][j] = matrix.values[i][j] + B.values[i][j]
        return C
    
    def __min__(matrix, B):
        if matrix.shape != B.shape:
            raise Excaption("Matrix can't be added of defrent sizes.")
        C = Matrix([[0]*B.columns for _ in range(B.rows)])
        for i in range(C.rows):
            for j in range(C.columns):
                C.values[i][j] = matrix.values[i][j] - B.values[i][j]
        return C
    
    def __mul__(matrix, B):
        if type(B) == type(0):
            C = Matrix([[0]*matrix.rows for _ in range(matrix.columns)])
            for i in range(C.rows):
                for j in range(C.columns):
                    C.values[i][j] = matrix.values[i][j] * B
            return C
        
        elif type(B) == type(matrix):
            if matrix.columns != B.rows:
                raise Exception("Matrix can't be multipyeid")
            
            C = Matrix([[0]*matrix.rows for _ in range(B.columns)])
            
            for i in range(matrix.rows):
               for j in range(B.columns):
                   for k in range(matrix.rows):
                       C.values[i][j] += matrix.values[i][k] * B.values[k][j]
            return C
        else:
            raise Exception("Matrix cant be multipyt with, " + str(type(B)))
    
    def add(matrix, B):
        if len(matrix.values[0]) != len(B[0]) or len(matrix.values) != len(B):
            raise Excaption("Matrix can't be added of defrent sizes.")
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                matrix.values[i][j] = matrix.values[i][j] + B[i][j]
    
    def sub(matrix, B):
        if len(matrix.values[0]) != len(B[0]) or len(matrix.values) != len(B):
            raise Excaption("Matrix can't be subtracted of defrent sizes.")
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                matrix.values[i][j] = matrix.values[i][j] - B[i][j] 
    
    def mul(matrix, B):
        if type(B) == type(0):
            C = Matrix([[0]*matrix.rows for _ in range(matrix.columns)])
            for i in range(C.rows):
                for j in range(C.columns):
                    matrix.values[i][j] = matrix.values[i][j] * B
        elif type(B) == type(Matrix):
            if matrix.columns != B.rows:
                raise Exception("Matrix can't be multipyeid")
            
            C = Matrix([[0]*matrix.rows for _ in range(B.columns)])
            
            for i in range(matrix.rows):
               for j in range(B.columns):
                   for k in range(matrix.rows):
                       C.values[i][j] += matrix.values[i][k] * B.values[k][j]
            matrix = C
        else:
            raise Exception("Matrix cant be multiplied with", str(type(B)))
    
    def row(matrix, index: int):
        if index >= matrix.rows or index < 0: raise ValueErorr("Row index out of range")
        return matrix.values[index]
    
    def column(matrix, index: int):
        if index >= matrix.columns or index < 0: raise ValueErorr("Column index out of range")
        return  [r[index] for r in matrix.values]
    
    def add_row(matrix, row: list, index=None):
        if len(row) != matrix.columns:
            raise Exception("Row must be the size of metrix columns")
        if not all(type(e) == type(0) or type(e) == type(0.0) for e in row):
            raise Exception("Matrix elemnts can only be of type int or float")
        if not index: index = matrix.columns
        matrix.values.insert(index, row)
        matrix.rows += 1
    
    def add_column(matrix, column: list, index=None):
        if len(column) != matrix.rows:
            raise Exception("Columns must be the size of metrix rows")
        if not all(type(e) == type(0) or type(e) == type(0.0) for e in column):
            raise Exception("Matrix elemnts can only be of type int or float")
        if not index: index = matrix.columns
        for r, e in enumerate(column):
            matrix.values[r].insert(index, e)
        matrix.columns += 1