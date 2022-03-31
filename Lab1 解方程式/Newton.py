from cmath import sin
import math

epsilon = math.pow(10, -6)

#function 1
def f1(x):
    return x*x - 2*x - 5

def f1_differential(x):
    return x - 2

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

def Newton(a, b, f):
    if f(a)*f(b) >= 0:
        print("Try another a and b")
    else:
        m = (a*f(b) - b*f(a)) / (f(b)-f(a))
        old_m = m
        while abs(m-old_m) >= epsilon:
            if f(a)*f(m) < 0:
                b = m
            else:
                a = m
            # update m
            m = (a*f(b) - b*f(a)) / (f(b)-f(a))
        print("False Position solution is", m)


def main():
    f1_a = -2
    f1_b = -1
    print("Function1: x*x - 2*x - 5")
    Newton(f1_a, f1_b, f1)

    print("---------------------------------------------------------------")

    f2_a = 3
    f2_b = 4
    print("Function2: -x*x*x + 29")
    Newton(f2_a, f2_b, f2)

    print("---------------------------------------------------------------")

    f3_a = 0
    f3_b = 1
    print("Function3: exp(x) - 5*x + 2")
    Newton(f3_a, f3_b, f3)


if __name__ == '__main__':
	main()