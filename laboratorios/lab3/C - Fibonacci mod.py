from sys import stdin
import time 


def fibonacci(n, m):
    if n <= 1:
        return n
    array= [0, 1]
    anteriosMod = 0
    normalMod = 1
    for i in range(n - 1):
        temporalMod = anteriosMod
        anteriosMod = normalMod % m
        normalMod = (temporalMod + normalMod) % m
        array.append(normalMod)
        if normalMod == 1 and anteriosMod == 0:
            index = (n % (i + 1))
            return array[index]
    return normalMod
def main():
    stard=time.time()
    n=int(stdin.readline().strip())
    m=int(stdin.readline().strip())
    print(fibonacci(n,m))
    end=time.time()
    p=end-stard
    print("El tiempo es : "+str(p/1000))
main()

