from cmath import sin
import math

epsilon = math.pow(10, -6)
epoch = math.pow(10, 8)

#function 5
def f5_x(x):
    return 6*x*x - 12.5*x - 16

def f5_y(y):
    return 0.5*y*y - 22.5*y - 17

def g5_x(x):
    return 16 / (6*x-12.5)

def g5_y(y):
    return 17 / (0.5*y-22.5)

def Fixed_Point(x1, y1, g1, g2):
    cnt = 0
    x2 = g1(x1)
    while abs(x1 - x2) >= epsilon and cnt <= epoch:
        cnt += 1
        x1 = x2
        x2 = g1(x1)
    
    cnt = 0
    y2 = g1(y1)
    while abs(y1 - y2) >= epsilon and cnt <= epoch:
        cnt += 1
        y1 = y2
        y2 = g2(y1)
    print("Fixed_Point Method solution is x = ", x2, ", y = ", y2)


def main():
    f5_x = -2
    f5_y = -2
    print("Function5: 6*x*x - 12.5*x - 16")
    Fixed_Point(f5_x, f5_y, g5_x, g5_y)

if __name__ == '__main__':
	main()