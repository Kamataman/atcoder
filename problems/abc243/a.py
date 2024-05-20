v,a,b,c=map(int,input().split())

remain=v
while True:
    if remain-a<0:
        print("F")
        break
    else:
        remain=remain-a
        if remain-b<0:
            print("M")
            break
        else:
            remain=remain-b
            if remain-c<0:
                print("T")
                break
            else:
                remain=remain-c