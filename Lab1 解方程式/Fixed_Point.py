from cmath import sin
import math

epsilon = math.pow(10, -6)
epoch = math.pow(10, 8)

#function 1
def f1(x):
    return x*x - 2*x - 5

def g1(x):
    return (-x*x + 5) / 2

#function 2
def f2(x):
    return -x*x*x + 29

def g2(x):
    return math.pow(29, 1/3)

#function 3
def f3(x):
    return math.exp(x) - 5*x + 2

def g3(x):
    return (math.exp(x) + 2) / 5


def Fixed_Position(x1, f, g):
    cnt = 0
    x2 = g(x1)
    while abs(x1 - x2) >= epsilon and cnt <= epoch:
        cnt += 1
        x1 = x2
        x2 = g(x1)
    print("Fixed_Position Method solution is", x2)


def main():
    f1_a = -2
    print("Function1: x*x - 2*x - 5")
    Fixed_Position(f1_a, f1, g1)

    print("---------------------------------------------------------------")

    f2_a = 3
    print("Function2: -x*x*x + 29")
    Fixed_Position(f2_a, f2, g2)

    print("---------------------------------------------------------------")

    f3_a = 0
    print("Function3: exp(x) - 5*x + 2")
    Fixed_Position(f3_a, f3, g3)


if __name__ == '__main__':
	main()