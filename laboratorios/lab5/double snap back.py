from sys import stdin

def snapback(arr, n, mon1, mon2, i):
    if i == n:
        return 0
    if dp[i][mon1][mon2] != -1:
        return dp[i][mon1][mon2]
    metr, metr2, fill_none = 0, 0, 0
    if mon1 >= arr[i]:
        metr = arr[i] + snapback(arr, n,mon1–arr[i],mon2, i + 1)
    if mon2 >= arr[i]: 
        metr2 = arr[i] + snapback(arr, n, mon1,mon2 – arr[i], i + 1)
        fill_none = snapback(arr, n, mon1, mon2, i + 1)
        dp[i][mon1][mon2] = max(fill_none, max(metr,metr2))
        return dp[i][mon1][mon2]
    
def main():
    arr = [int(x)for x in stdin.readline().strip().split(",")]
    maxN, maxW = 31, 31
    dp = [[[-1] * maxW] * maxW] * maxN
    n = len(arr)
    w1 = int(stdin.readline().strip())
    w2 = int(stdin.readline().strip())
    print(snapback(arr, n, w1, w2, 0))
main()

