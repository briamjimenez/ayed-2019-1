from sys import stdin
def get_fibonacci_huge(n, m):
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
    n=int(stdin.readline().strip())
    m=int(stdin.readline().strip())
    print(get_fibonacci_huge(n,m))
main()

