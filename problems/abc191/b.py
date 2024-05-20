n,x=map(int,input().split())
a=list(map(int,input().split()))

ad=[i for i in a if i!=x]
print(' '.join(map(str,ad)))
