from cmath import sin
import math

epsilon = math.pow(10, -6)

#function 1
def f1(x):
    return x*x - 2*x - 5

#function 2
def f2(x):
    return -x*x*x + 29

#function 3
def f3(x):
    return math.exp(x) - 5*x + 2

def Secant(x1, x2, f):
    while abs(x1 - x2) >= epsilon:
        x3 = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))
        x1 = x2
        x2 = x3
    print("Secant Method solution is", x2)


def main():
    f1_a = -3
    f1_b = -1
    print("Function1: x*x - 2*x - 5")
    Secant(f1_a, f1_b, f1)

    print("---------------------------------------------------------------")

    f2_a = 3
    f2_b = 4
    print("Function2: -x*x*x + 29")
    Secant(f2_a, f2_b, f2)

    print("---------------------------------------------------------------")

    f3_a = 0
    f3_b = 1
    print("Function3: exp(x) - 5*x + 2")
    Secant(f3_a, f3_b, f3)


if __name__ == '__main__':
	main()