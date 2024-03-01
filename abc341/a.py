def funcA(n):
    s='1'
    for i in range(n):
        s=s+'01'
    return s

if __name__ == '__main__':
    n=int(input())
    print(funcA(n))