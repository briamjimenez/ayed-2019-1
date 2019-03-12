from sys import stdin



def painting(n, k) : 
    total = k 
    mod = 1000000007 
    h = 0
    diff = k 
    for i in range(2, n + 1) :  
        h = diff  
        diff = total * (k - 1)  
        diff = diff % mod  
        total = (h + diff) % mod  
    return total    

def main():
    n=int(stdin.readline().strip())
    k=int(stdin.readline().strip())
    print(painting(n, k))
main()
