from sys import stdin


def isHeap(arr, i, n):    
    if i > int((n - 2) / 2):  
        return True 
    if(arr[i] >= arr[2 * i + 1] and 
       arr[i] >= arr[2 * i + 2] and 
       isHeap(arr, 2 * i + 1, n) and
       isHeap(arr, 2 * i + 2, n)): 
        return True
    return False

def main():    
    arr = [int(x)for x in stdin.readline().strip().split(" ")]  
    n = len(arr) - 1
    if isHeap(arr, 0, n): 
        print("True") 
    else: 
        print("False") 
  
main()
