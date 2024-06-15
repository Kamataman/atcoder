n=int(input())

import numpy
def createCarpet(level):
    if level==0:
        return [['#']]
    else:
        c=createCarpet(level-1)
        grid=3**(level-1)
        center=[['.']*grid for _ in range(grid)]
            
        carpet_upbottom=numpy.concatenate((c,c,c),axis=1)
        carpet_center=numpy.concatenate((c,center,c),axis=1)
        carpet=numpy.concatenate((carpet_upbottom,carpet_center,carpet_upbottom),axis=0)
        return carpet

carpet=createCarpet(n)
for c in carpet:
    print(''.join(c))