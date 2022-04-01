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


def main():
    f1_a = -3
    f1_b = -1
    print("Function1: x*x - 2*x - 5")
    False_Position(f1_a, f1_b, f1)

    print("---------------------------------------------------------------")

    f2_a = 3
    f2_b = 4
    print("Function2: -x*x*x + 29")
    False_Position(f2_a, f2_b, f2)

    print("---------------------------------------------------------------")

    f3_a = 0
    f3_b = 1
    print("Function3: exp(x) - 5*x + 2")
    False_Position(f3_a, f3_b, f3)


if __name__ == '__main__':
	main()