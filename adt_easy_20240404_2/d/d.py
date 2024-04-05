l,r=map(int,input().split())
s=input()

begin=s[:l-1]
end=s[r:]
mid=s[l-1:r][::-1]

# print(begin)
# print(end)
# print(mid)
print(''.join(begin+mid+end))