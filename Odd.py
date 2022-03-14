# Generate odd numbers between (a,b) including b.

def odd_numbers(a, b):
    if a % 2 == 0:
        a += 1
    for i in range(a, b+1, 2):
        yield i

if __name__ == '__main__':
    for i in odd_numbers(int(input("Enter a: ")), int(input("Enter b: "))):
        print(i)
