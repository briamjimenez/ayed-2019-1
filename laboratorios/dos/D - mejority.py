from sys import stdin

def numero(lista):
    cont=0
    for i in lista:
        if i== i+1:
            cont+=1
            return False  
        else:
            return True 
    print(cont)

def main():
    num=int(stdin.readline().strip())
    lista=[int(x)for x in stdin.readline().strip().split(" ")]
    print(numero(lista))
main()
    
