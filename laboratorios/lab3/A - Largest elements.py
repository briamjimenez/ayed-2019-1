from sys import stdin
import time 


def mergeSort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k]=lefthalf[i]
                i=i+1
            else:
                lista[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            lista[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            lista[k]=righthalf[j]
            j=j+1
            k=k+1



def main():
    stard=time.time()
    cadena_1=[int(x)for x in stdin.readline().strip().split(" ")]
    lista=[int(x)for x in stdin.readline().strip().split(" ")]
    mergeSort(lista)
    lista.reverse()
    if len(lista)>=10:
        print(lista[:10])
    else:
        print(lista)
    end=time.time()
    p=end-stard
    print(p/1000)
main()
