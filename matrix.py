import random

def generate_random_matrix(rowN = 3, colN = 3):
    matrix = []
    for i in range(rowN):
        row = []
        for j in range(colN):
            row.append(random.randint(1,100))
        matrix.append(row)    
    return matrix        

def get_column_sum(matrix, col_Id = 0):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][col_Id]
    return sum    

def get_row_average(matrix, row_Id = 0):
    av, rowN = 0, len(matrix[0])

    for i in range(rowN):
        av += matrix[row_Id][i]
    return av/rowN    


example_matrix = generate_random_matrix(4,7)

print('\nMatrix:')
for i in example_matrix:
    print(i)

sum = get_column_sum(example_matrix, 1)
print('\nSum of the given column: ', sum)

average = get_row_average(example_matrix, 0)
print('\nAverage of the given row: ', format(average, '.3f') )
