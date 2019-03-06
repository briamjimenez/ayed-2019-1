from sys import stdin

def funcion(S, m, n): 
    matriz = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        matriz[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = matriz[i - S[j]][j] if i-S[j] >= 0 else 0
            y = matriz[i][j-1] if j >= 1 else 0
            matriz[i][j] = x + y 
    return matriz[n][m-1] 

def main():    
    n = int(stdin.readline().strip())
    arr = [int(x)for x in stdin.readline().strip().split(",")] 
    m = len(arr) 
    print(funcion(arr, m, n)) 
main()
