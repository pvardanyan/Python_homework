import random

class Matrix:
    __matrix = []
    def __init__(self, n = 3, m = 3):
        self.__n = n
        self.__m = m
        a,b = input("Input the range of random numbers to be generated (integers with a space): ").split(" ")
        for i in range(n):
            row = []
            for j in range(m):
                row.append(random.randint(int(a),int(b)))
            self.__matrix.append(row)

    def print_matrix(self):
        for i in self.__matrix:
            print(i)

    def calc_mean(self):
        sum = 0
        for i in self.__matrix:
            for j in i:
                sum += j
        return sum / (self.__n * self.__m)

    def sum_of_given_row(self, row):
        sum = 0
        for i in self.__matrix[row]:
            sum += i
        return sum

    def average_of_given_column(self, col):
        sum = 0
        for i in range(self.__n):
            sum += self.__matrix[i][col]
        return sum / self.__n        

    def print_submatrix(self, *args):
        col1,col2,row1,row2 = args
        for i in range(row2 - row1 + 1):
            for j in range(col2 - col1 + 1):
                print(self.__matrix[row1 + i][col1 + j], end="  ")
            print()
                
#Assume that given numbers are from 0 to max(n,m)
matrix_obj = Matrix(3,4)
#print matrix
matrix_obj.print_matrix()

print(f"\nMean is: {matrix_obj.calc_mean():.2f}")
print(f"Sum of a given row is: {matrix_obj.sum_of_given_row(2)}")
print(f"Average of a given column is: {matrix_obj.average_of_given_column(1):.2f}")
#print submatrix with array
matrix_obj.print_submatrix(0,1,0,2)
