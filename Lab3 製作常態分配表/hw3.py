import math

def f(x):
    return (1/math.sqrt(2*math.pi)) * math.exp(-x*x/2)

# Simpson's 1/3 Rule
# 參數x是normal dist.中積分的z
# 參數n是要切成幾份
def simpson(x, n):
    sum = 0
    delta = x/n     #delta = x/n = (b-a)/n = h

    for x in range(0, n+1):      #分成n份
        if x==0 or x==n :
            sum += f(x*delta)
        
        elif x%2 == 1:
            sum += 4*f(x*delta)
        
        elif x%2 == 0:
            sum += 2*f(x*delta)
    
    return sum*delta/3

def main():
    n = 100     #要切的間隔數
    offset = 0.001      #方便計算.001~.009 如果要算.00n時 改這個變數即可
    for i in range (500):
        print(round(simpson(0.01*i+offset, n)+0.5, 6))      #四捨五入到小數點後第六位

if __name__ =='__main__':
    main()