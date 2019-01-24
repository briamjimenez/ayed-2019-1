import json

# TODO Complete!

from sys import stdin
def contar_vocales(cad,voc,cons):
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
        elif c == "b " or c == "d" or c == "f" or c == "g" or c == "h" or c == "j" or c == "k" or c == "l" or c == "m" or c == "n" or c == "ñ" or c == "p" or c == "q" or c == "r" or c == "s" or c == "t" or c == "v" or c == "x" or c == "y" or c == "z" or c == "B" or c == "D" or c == "F" or c == "G" or c == "H"or c == "J" or c == "K" or c == "L" or c == "M" or c == "N" or c == "Ñ" or c == "P" or c == "Q" or c == "R" or c == "S" or c == "T" or c == "V" or c == "X" or c == "Y" or c == "Z":
            cons+=1
    return voc,cons

def main():
    voc = 0
    cons = 0
    cad = str(stdin.readline().strip().strip())
    if cad=="":
        return None 
    elif voc > cons:
        return True
    else:
        return False

    contar_vocales(cad,voc,cons)
main()

def has_more_vowels(s):
    return False

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
