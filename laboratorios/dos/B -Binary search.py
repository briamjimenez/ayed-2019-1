from sys import stdin



def binarySearch(alist, item, pasos ):
    print(alist,item)
    if len(alist) == 0:
        return -1
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            pasos=midpoint
            return pasos
        else:
            if item<alist[midpoint]:
                pasos+=midpoint
                return binarySearch(alist[:midpoint],item,pasos)
            else:
                return binarySearch(alist[midpoint+1:],item, pasos+midpoint)

def main():
    pasos=0
    item=int(stdin.readline().strip())
    alist=[int(x)for x in stdin.readline().strip().split(" ")]
    print(binarySearch(alist, item ,0))
    
main()

    
