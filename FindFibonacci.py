# Finds n fibonacci numbers.

def generatefibo(n):
    fibo = [0,1]
    i=2
    while(True):
        fibo.append(fibo[i-1]+fibo[i-2])
        if len(fibo) == n:
            break
        i+=1
    return fibo

def Fibonacci(max):
    fibo = generatefibo(max)
    for number in fibo:
        print(number)

if __name__ == "__main__":
    Fibonacci(int(input("How many Fibonacci numbers do you want? ")))

