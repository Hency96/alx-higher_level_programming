#!/bin/bash

def square_matrix_simple(matrix=[]):
X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       matrix[i][j] = X[i][j] * Y[i][j]

return (matrix)
