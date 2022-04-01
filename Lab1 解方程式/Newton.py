from cmath import sin
import math

epsilon = math.pow(10, -6)

#function 1
def f1(x):
    return x*x - 2*x - 5

def f1_differential(x):
    return 2*x - 2

#function 2
def f2(x):
    return -x*x*x + 29

def f2_differential(x):
    return -3*x*x

#function 3
def f3(x):
    return math.exp(x) - 5*x + 2

def f3_differential(x):
    return math.exp(x) - 5

def Newton(x, f, df):
    init_x = x
    delta = -(f(x) / df(x))
    x += delta
    while abs(delta) >= epsilon:
        delta = -(f(x) / df(x))
        x += delta
    print("Newton method solution is", x, "initial input x is ", init_x)


def main():
    f1_x_init = -3
    print("Function1: x*x - 2*x - 5")
    Newton(f1_x_init, f1, f1_differential)

    print("---------------------------------------------------------------")

    f2_x_init = 2
    print("Function2: -x*x*x + 29")
    Newton(f2_x_init, f2, f2_differential)

    print("---------------------------------------------------------------")

    f3_x_init = 0
    print("Function3: exp(x) - 5*x + 2")
    Newton(f3_x_init, f3, f3_differential)


if __name__ == '__main__':
	main()