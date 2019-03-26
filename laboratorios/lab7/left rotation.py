from sys import stdin

def leftRotaE(numbers,n):
    numbersaytemp=[0]
    for i in range(n-1):
        numbers[i]=numbers[i+1]
    numbers[n-1]=numbersaytemp

def leftRota(numbers,d,n):
    for i in range(d):
        leftRotaE(numbers,n)

def main():
    numbers=[int(x)for x in stdin.readline().strip().split(" ")]
    d=int(stdin.readline().strip())
    n=numbers[-1]
    leftRota(numbers,d,n)
    def printaarr(numbers,size):
        for i in range(size):
            print("%d" % numbers[i],end=" ")
    printaarr(numbers,n)
main()
