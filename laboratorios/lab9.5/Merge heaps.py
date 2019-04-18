def MaxHeapify(arr, n, idx):
    if idx >= n:
        return
    l = 2 * idx + 1
    r = 2 * idx + 2
    Max = 0
    if l < n and arr[l] > arr[idx]:
        Max = l
    else:
        Max = idx
    if r < n and arr[r] > arr[Max]:
        Max = r
    if Max != idx:
        arr[Max], arr[idx] = arr[idx], arr[Max]


def buildMaxHeap(arr, n):
    for i in range(int(n / 2)):
        MaxHeapify(arr, n, i)


def mergeHeaps(merged, a, b, n, m):
    for i in range(n):
        merged[i] = a[i]
    for i in range(m):
        merged[n + i] = b[i]
def main():
    a = [10, 5, 6, 2]
    b = [12, 7, 9]
    n = len(a)
    m = len(b)
    merged = [0] * (m + n)
    mergeHeaps(merged, a, b, n, m)
    listafin=merged
    listafin.sort(reverse=True)
    print(listafin)
main()









