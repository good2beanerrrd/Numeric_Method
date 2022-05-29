from tracemalloc import start
import numpy as np
import math
import matplotlib.pyplot as plt

#自訂題 f(x) = 2x^2 - x + 1
n = 5      # number of the data

X = np.array([ 0.0, 1.0, 0.5, -3.0, -1.5])
Y = np.array([ 1.0, 2.0, 1.0, 22.0, 7.0])

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
    minError = error(1)
    bestChoice = 1

    for i in range (1, n):
        cur_error = error(i)
        print("\nP%d(x)'s"%i, " error is %f\n"%cur_error)
        if cur_error < minError:
            minError = cur_error
            bestChoice = i

    print("The best choice is P%d(x)" %bestChoice)      #印出幾次式是最好的

if __name__ == '__main__':
    main()