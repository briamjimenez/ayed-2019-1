from sys import stdin

def Friends(n): 
    matrix = [0 for i in range(n + 1)] 
    for i in range(n + 1): 
        if(i <= 2): 
            matrix[i] = i 
        else: 
            matrix[i] = matrix[i - 1] + (i - 1) * matrix[i - 2] 
    return matrix[n] 
  
def main():
    n = int(stdin.readline().strip())
    print(Friends(n))
main()
