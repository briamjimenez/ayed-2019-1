from heapq import heappop,heappush,heapify

numbers = [int(x) for x in input().split()]
galletas= [int(x) for x in input().split()]

contador_galletas = int(numbers[0])
min_dul = int(numbers[1])

heapify(galletas)

def galletas(galletas, min_dul):
    fC = 0
    try:
        while galletas[0] < min_dul:
            fC+=1
            c1 = heappop(galletas)
            c2 = heappop(galletas)
            nueva_galleta=(1*c1)+(2*c2)
            heappush(galletas,nueva_galleta)
        print(fC)
    except:
        print("-1")

    
galletas(galletas, min_dul)
