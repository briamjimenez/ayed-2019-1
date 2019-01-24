import json


# TODO Complete!
from sys import stdin 


def torres_hanoi(n,o,d,aux):
    if n > 0:
        torres_hanoi(n-1,o,aux,d)
        print("torre"+ str(o)+"hasta torre" + str(d))
        torres_hanoi(n-1,aux,d,o)
n=int(stdin.readline().strip())
torres_hanoi(n,1,3,2)
        


def hanoi(n):
    return []



if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            hanoi(n)
        print('OK!')
