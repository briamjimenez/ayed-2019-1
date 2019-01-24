from sys import stdin

def merge_sort(lista):
  global res 
  if len(lista) == 1:
      return lista
  mid = len(lista) // 2
  L, R = lista[: mid], lista[mid: ]
  A = merge_sort(L)
  B = merge_sort(R)
  res = []
  i = j = 0
  while i < len(A) and j < len(B):
    if A[i] < B[j]:
      res.append(A[i])
      i += 1
    else:
      res.append(B[j])
      j += 1
  while i < len(A):
    res.append(A[i])
    i += 1
  while j < len(B):
    res.append(B[j])
    j += 1
  return res 

def resul(res):
    p=res[-1]*res[-2]
    return p


def main():
  global res
  lista = [int(x) for x in stdin.readline().strip().split(" ")]
  merge_sort(lista)
  print(resul(res))
main()


