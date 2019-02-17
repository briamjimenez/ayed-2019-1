from sys import stdin





def is_prime(numero):
    for o in numero :
        is_prime_2(o)

def is_prime_2(o):
    d = 2
    while d * d <= o:
        if o % d == 0:
            print ("no")
            return
        d += 1
    print("si")



##def primality(numero):
##    for o in numero:
##        cont = 0
##        veri= False
##        for i in range(1,o+1):
##            if (o% i)==0:
##               cont = cont+ 1
##            if cont >= 3:
##                veri=True
##                break
##    
##        if cont==2 or veri==False:
##            print (str(o)+"si")
##            for k in range(len(numero)):
##                pass
##        else:
##            print (str(o)+"no")
            
def main():
    p=int(stdin.readline().strip())
    numero = [int(x) for x in stdin.readline().strip().split(" ")]
##    primality(numero)
    is_prime(numero)
main()











