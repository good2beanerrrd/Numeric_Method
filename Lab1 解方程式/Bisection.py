from cmath import sin
import math

epsilon = math.pow(10, -6)
epoch = math.pow(10, 8)

#function 1
def f1(x):
    return x*x - 2*x - 5

#function 2
def f2(x):
    return -x*x*x + 29

#function 3
def f3(x):
    return math.exp(x) - 5*x + 2

#function 4
def f4(x):
    return math.exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24

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


def main():
    f1_a = -2
    f1_b = -1
    print("Function1: x*x - 2*x - 5")
    Bisection(f1_a, f1_b, f1)

    print("---------------------------------------------------------------")

    f2_a = 3
    f2_b = 4
    print("Function2: -x*x*x + 29")
    Bisection(f2_a, f2_b, f2)

    print("---------------------------------------------------------------")

    f3_a = 0
    f3_b = 1
    print("Function3: exp(x) - 5*x + 2")
    Bisection(f3_a, f3_b, f3)

    print("---------------------------------------------------------------")

    f4_a = 3
    f4_b = 2
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)

    print("---------------------------------------------------------------")

    f4_a = 2
    f4_b = 1
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)

    print("---------------------------------------------------------------")

    f4_a = 1
    f4_b = 0
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)

    print("---------------------------------------------------------------")

    f4_a = -2
    f4_b = 0
    print("Function4: exp(1.63*x*sin(x)) - 2.38*x*x - 3.6*x + 1.24")
    print("a=", f4_a, ", b=", f4_b)
    Bisection(f4_a, f4_b, f4)

if __name__ == '__main__':
	main()