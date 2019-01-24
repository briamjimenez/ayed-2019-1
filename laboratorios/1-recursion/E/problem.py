import json


# TODO Complete!
def super_d(n,k):
    pro=str(n*k)
    while len(pro)>1:
        cont = 0
        for i in pro:
            cont+=int(i)
        pro = str(cont)
    print(pro)  

def super_digit(n, k):
    super_d(n,k)
    return 0


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}"
        print('OK!')
