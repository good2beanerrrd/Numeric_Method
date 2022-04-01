from cmath import sin
import math

epsilon = math.pow(10, -6)
epoch = math.pow(10, 6)

#function 1
def f1(x):
    return x*x - 2*x - 5

def g1(x):
    return 5 / (x-2)

def f1_differential(x):
    return 2*x - 2

#function 2
def f2(x):
    return -x*x*x + 29

def g2(x):
    return math.pow(29, 1/3)

def f2_differential(x):
    return -3*x*x

#function 3
def f3(x):
    return math.exp(x) - 5*x + 2

def g3(x):
    return (math.exp(x) + 2) / 5

def f3_differential(x):
    return math.exp(x) - 5

#function 4
def f4(x):
    return math.exp(1.63*x*math.sin(x)) - 2.38*x*x - 3.6*x + 1.24

def g4(x):
    return (math.exp(1.63*x*math.sin(x)) + 1.24) / (2.38*x + 3.6)

def f4_differential(x):
    return 1.63*math.exp(1.63*x*math.sin(x))*(math.sin(x)+x*math.cos(x))-2*2.38*x - 3.6

def Fixed_Point(x1, f, g):
    cnt = 0
    x2 = g(x1)
    while abs(x1 - x2) >= epsilon and cnt <= epoch:
        cnt += 1
        x1 = x2
        x2 = g(x1)
    print("Fixed_Point Method solution is", x2, ", taking ", cnt, " steps.")

def Bisection(a, b, f):
    if f(a)*f(b) >= 0:
        print("You have not assumed right a and b\n")
    else:
        cnt = 0
        while abs(a-b) >= 2*epsilon and cnt < epoch:
            cnt += 1
            m = (a+b)/2
            if f(a)*f(m) < 0:
                b = m
            else:
                a = m
        print("Bisection solution is", (a+b)/2, ", taking ", cnt, " steps.")

def False_Position(a, b, f):
    if f(a)*f(b) >= 0:
        print("You have not assumed right a and b\n")
    else:
        m = (a*f(b) - b*f(a)) / (f(b)-f(a))
        old_m = m
        cnt = 0
        while abs(m-old_m) > epsilon:
            cnt += 1
            if f(a)*f(m) < 0:
                b = m
            else:
                a = m
            # update m
            m = (a*f(b) - b*f(a)) / (f(b)-f(a))
        print("False Position solution is", m, ", taking ", cnt, " steps.")

def Secant(x1, x2, f):
    cnt = 0
    while abs(x1 - x2) >= epsilon and cnt < epoch:
        x3 = (x1*f(x2) - x2*f(x1)) / (f(x2) - f(x1))
        x1 = x2
        x2 = x3
    print("Secant Method solution is", x2, ", taking ", cnt, " steps.")

def Newton(x, f, df):
    init_x = x
    delta = -(f(x) / df(x))
    x += delta
    cnt = 0
    while abs(delta) >= epsilon and cnt < epoch:
        cnt += 1
        delta = -(f(x) / df(x))
        x += delta
    print("Newton method solution is", x, "initial input x is ", init_x, ", taking ", cnt, " steps.")

def main():
    f1_a = -3
    f1_b = -1
    f1_x_init = -3
    print("Function1: x*x - 2*x - 5")
    Bisection(f1_a, f1_b, f1)
    False_Position(f1_a, f1_b, f1)
    Fixed_Point(f1_a, f1, g1)
    Secant(f1_a, f1_b, f1)
    Newton(f1_x_init, f1, f1_differential)

    print("---------------------------------------------------------------")

    # f2_a = 3
    # f2_b = 4
    # f2_x_init = 2
    # print("Function2: -x*x*x + 29")
    # Bisection(f2_a, f2_b, f2)
    # False_Position(f2_a, f2_b, f2)
    # Fixed_Position(f2_a, f2, g2)
    # Secant(f2_a, f2_b, f2)
    # Newton(f2_x_init, f2, f2_differential)

    # print("---------------------------------------------------------------")

    # f3_a = 0
    # f3_b = 1
    # f3_x_init = 0
    # print("Function3: exp(x) - 5*x + 2")
    # Bisection(f3_a, f3_b, f3)
    # False_Position(f3_a, f3_b, f3)
    # Fixed_Position(f3_a, f3, g3)
    # Secant(f3_a, f3_b, f3)
    # Newton(f3_x_init, f3, f3_differential)

    f4_a = -3
    f4_b = -2
    f4_x_init = -2
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)
    False_Position(f4_a, f4_b, f4)
    Fixed_Point(f4_a, f4, g4)
    Secant(f4_a, f4_b, f4)
    Newton(f4_x_init, f4, f4_differential)
    print("---------------------------------------------------------------")

    f4_a = 0
    f4_b = 0.9
    f4_x_init = 0
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)
    False_Position(f4_a, f4_b, f4)
    Fixed_Point(f4_a, f4, g4)
    Secant(f4_a, f4_b, f4)
    Newton(f4_x_init, f4, f4_differential)

    print("---------------------------------------------------------------")

    f4_a = 0.9
    f4_b = 2
    f4_x_init = 1
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)
    False_Position(f4_a, f4_b, f4)
    Fixed_Point(f4_a, f4, g4)
    Secant(f4_a, f4_b, f4)
    Newton(f4_x_init, f4, f4_differential)

    print("---------------------------------------------------------------")

    f4_a = 2
    f4_b = 3
    f4_x_init = 2
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)
    False_Position(f4_a, f4_b, f4)
    Fixed_Point(f4_a, f4, g4)
    Secant(f4_a, f4_b, f4)
    Newton(f4_x_init, f4, f4_differential)

if __name__ == '__main__':
	main()