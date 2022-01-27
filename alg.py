def div(ix, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i]/const

def sub(ix, iy, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i] - iy[i]*const
        
ib = [1,1,-1,0]
ia = [0,3.5,3.4,0]
ic = [3.4,-3.5,0,4.2]

if ia[0] != 1:
    if ia[0] == 0:
        if ib[0] != 0:
            ia, ib = ib, ia
        elif ic[0] != 0:
            ia, ic = ic, ia
    div(ia, 0)

if ib[0] != 0:
    sub(ib, ia, 0)
    
if ib[1] != 1:
    if ib[1] == 0:
        if ic[1] != 0:
            ib, ic = ic, ib
            
    div(ib, 1)
 
if ic[0] != 0:
    sub(ic, ia, 0)

if ic[1] != 0:
    sub(ic, ib, 1)

if ic[2] != 1:
    div(ic, 2)
    
ic = float(round(ic[3], 2))
ib = float(round((ib[3] - ib[2]*ic),2))
ia = float(round((ia[3] - (ia[1]*ib + ia[2]*ic)), 2))
print(ia, ib, ic)