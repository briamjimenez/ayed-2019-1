# jolly jumpers
from sys import stdin


def jumper(array):
    size=len(array)
    jumps=set()
    if size == 1:
        return True
    for i in range(size-1):
        diff=abs(array[i+1]-array[i])
        if diff < size and diff >= 1:
            jumps.add(diff)
    if len(jumps)== size - 1:
        return True
    return False


def main():
    array=[int(x)for x in stdin.readline().strip().split(" ")]
    print(jumper(array))
main()
    
