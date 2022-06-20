from tracemalloc import start
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

n = 39      # number of the data

X = np.array([ 0.00, 0.28, 0.59, 0.75, 0.98, 1.22, 1.36, 1.48, 1.60, 1.89, 2.07, 2.31
            , 2.40, 2.59, 2.69, 2.86, 3.13, 3.23, 3.34, 3.53, 3.67, 3.97, 4.06, 4.36, 4.61
            , 4.82, 5.08, 5.27, 5.41, 5.58, 5.83, 6.00, 6.17, 6.34, 6.67, 6.96, 7.28, 7.52, 7.62])

Y = np.array([ 1.0000, 1.3701, 1.8627, 2.0407, 2.1221, 1.9428, 1.7405, 1.5105, 1.2743, 0.7626
        , 0.5833, 0.5698, 0.6337, 0.8588, 1.0117, 1.2924, 1.6524, 1.7431, 1.8034, 1.8156, 1.7658
        , 1.5646, 1.5059, 1.3668, 1.3343, 1.3324, 1.2953, 1.2178, 1.1321, 1.0115, 0.8706, 0.8452
        , 0.9072, 1.0625, 1.5445, 1.9695, 2.1181, 1.9244, 1.7809])

def get_coefficient(m):
    dim = m + 1     #矩陣的維度
    A = np.zeros((dim, dim))
    B = np.zeros((dim, 1))

    A[0][0] = n
    #求矩陣Ａ
    for i in range (dim):
        for j in range (dim):
            for x in X:
                if i!=0 and j!=0:
                    A[i][j] += pow(x, (i+j))
    
    #求矩陣B
    for i in range (dim):
        for j in range (n):
            B[i] += Y[j] * pow(X[j], i)

    #return x of Ax = b
    return np.linalg.solve(A, B)

#m次多項式
def Pm(m, x):
    #get the coefficients of Pm
    coeff = get_coefficient(m)  
    ans = 0     #P(m)代入x之值
    for i in range (m+1):
        ans += coeff[i] * math.pow(x, i)
    #回傳m次多項式代入x之值
    return ans

#計算誤差
def error(m):
    e = 0
    for i in range (n):
        e += (Pm(m, X[i])-Y[i])**2

    return math.sqrt(e / (n-m))

def main():
    maxY = Pm(30, X[0])
    bestChoice = 0

    for i in range(1, n):
        cur_y = Pm(30, X[i])
        if cur_y > maxY:
            maxY = cur_y
            bestChoice = i

    print("The smallest is %d" %bestChoice) 

if __name__ == '__main__':
    main()