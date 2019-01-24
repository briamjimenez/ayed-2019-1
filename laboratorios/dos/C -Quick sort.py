from sys import stdin
def quickSort(alist):
    """parte la lista en 2 """
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
        
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    """toma un punto de pivote y comienza a organizar """
    pivotvalue = alist[first]
    leftmark = first+1  
    rightmark = last    
    done = False
    while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
 
def main():
    num=int(stdin.readline().strip())
    alist =[str(x)for x in stdin.readline().strip().split(" ")]
    quickSort(alist)
    print(*alist)
main()
