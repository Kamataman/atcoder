h=int(input())
i=0
plant_h=2**i
while h>=plant_h:
    i+=1
    plant_h+=2**i
i+=1
print(i)