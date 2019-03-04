from sys import stdin


def uniquePathsWithObstacles(A): 
    paths = [[0]*len(A[0]) for i in A] 
    if A[0][0] == 0: 
        paths[0][0] = 1
      
    for i in range(1, len(A)): 
        if A[i][0] == 0:
                paths[i][0] = paths[i-1][0] 
              
    for j in range(1, len(A[0])): 
        if A[0][j] == 0:
                paths[0][j] = paths[0][j-1] 
              
    for i in range(1, len(A)): 
      for j in range(1, len(A[0])): 
  
        if A[i][j] == 0: 
          paths[i][j] = paths[i-1][j] + paths[i][j-1] 
    
    return paths[-1][-1] 
  
def main():
    matriz_entrada=str(stdin.readline().strip())

    var=matriz_entrada[1:-1]
    var_2=var.split("], ")
    A=[[int(j) for j in i.replace("[","").replace("]","").split(", ")] for i in var_2]
    for i in range(len(A)):
        for j in range(len(A[i])):
            pass
    for j in A:
        print(*j)
    print(uniquePathsWithObstacles(A))
main()
