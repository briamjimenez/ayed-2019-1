import json


# TODO Complete!!

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

def reverse(text):
    r = vuelta(text.split(),[]) 
    return (" ".join(r))


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')


