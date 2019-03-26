
from sys import stdin

def vueltaPalabra(s,x):
     if len(s) == 0:
          return x
     else:
          x += s[-1]
          return vueltaPalabra(s[:-1],x)

def vuelta(x,t):
     if len(x) == 0:
          return t
     else:
          t.append(vueltaPalabra(x.pop(),""))
          return vuelta(x,t)
     
     
def main():
     s=(stdin.readline().strip().split())
     while s!=[]:
          r = vuelta(s,[])
          print(" ".join(r))
          s=(stdin.readline().strip().split())

main()
