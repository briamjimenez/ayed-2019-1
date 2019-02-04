from sys import stdin
import time


def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        linea_ant = pascal(n-1)
        for i in range(len(linea_ant)-1):
            line.append(linea_ant[i] + linea_ant[i+1])
        line += [1]
        print(*linea_ant)
    return line


def main():
    stard=time.time()
    n=int(stdin.readline().strip())
    print(*pascal(n))
    end=time.time()
    p=end-stard
    print(p/1000)
main()
