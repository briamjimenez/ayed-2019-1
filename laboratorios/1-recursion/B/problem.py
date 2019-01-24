import json


# TODO Complete!


from sys import stdin

def cadena(lista):
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)

    return pares+impares
def main():
    lista=[int(x) for x in stdin.readline().strip().split(",")]
    print(cadena(lista))


main()


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
