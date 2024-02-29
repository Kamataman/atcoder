n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

m = int(input())
op = [str(input()) for i in range(m)]

q = int(input())
a = [0]*q
b = [0]*q
for i in range(q):
    a[i], b[i] = map(int, input().split())
    b[i] -= 1

# 初期状態の分mを1増やす
m += 1
ax, bx, cx, ay, by, cy = ([0]*m, [0]*m, [0]*m, [0]*m, [0]*m, [0]*m)
ax[0] = 1
by[0] = 1

# op
for j in range(1, m):
    # opとmでindexがずれる
    if op[j-1][0] == '1':
        ax[j], bx[j], cx[j], ay[j], by[j], cy[j] = (
            ay[j-1], by[j-1], cy[j-1], -ax[j-1], -bx[j-1], -cx[j-1])
    elif op[j-1][0] == '2':
        ax[j], bx[j], cx[j], ay[j], by[j], cy[j] = (
            -ay[j-1], -by[j-1], -cy[j-1], ax[j-1], bx[j-1], cx[j-1])
    elif op[j-1][0] == '3':
        p = int(op[j-1].split()[1])
        ax[j], bx[j], cx[j], ay[j], by[j], cy[j] = (
            -ax[j-1], -bx[j-1], -cx[j-1]+2*p, ay[j-1], by[j-1], cy[j-1])
    elif op[j-1][0] == '4':
        p = int(op[j-1].split()[1])
        ax[j], bx[j], cx[j], ay[j], by[j], cy[j] = (
            ax[j-1], bx[j-1], cx[j-1], - ay[j-1], -by[j-1], -cy[j-1]+2*p)
'''
print(ax)
print(bx)
print(cx)
print(ay)
print(by)
print(cy)
'''
# query
for i in range(q):
    xb = x[b[i]]
    yb = y[b[i]]
    print("%d %d" % (ax[a[i]]*xb+bx[a[i]]*yb +
                     cx[a[i]], ay[a[i]]*xb+by[a[i]]*yb+cy[a[i]]))
