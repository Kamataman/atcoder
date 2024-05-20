s=list(input())

ans = [i for i in s if i!= 'a' and i!= 'e' and i!= 'i' and i!= 'o' and i!= 'u']
print(''.join(ans))