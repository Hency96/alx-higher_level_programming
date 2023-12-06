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

mat = matrix=[]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       mat[i][j] = X[i][j] * Y[i][j]

return (mat
