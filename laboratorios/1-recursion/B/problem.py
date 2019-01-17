import json


# TODO Complete!


def impar(lista,cont):
    impar=[]
    par=[]
    if cont == 0:
        return lista[cont]
    
    elif lista[cont] % 2 == 0:
        
        par.append(lista[cont])

    else:
        impar.append(lista[cont])
    return impar(lista,cont+1)
def arrange(numbers):
    
    return numbers


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
