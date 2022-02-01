def div(ix, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i]/const

def sub(ix, iy, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i] - iy[i]*const



la = [0,3.5,3.4,0]
lb = [1,1,-1,0]
lc = [3.4,-3.5,0,4.2]
ld = [3.4,-3.5,0,4.2]

if la[0] != 1:
    if la[0] == 0:
        if lb[0] != 0:
            la, lb = lb, la
        elif lc[0] != 0:
            la, lc = lc, la
    div(la, 0)

if lb[0] != 0:
    sub(lb, la, 0)
    
if lb[1] != 1:
    if lb[1] == 0:
        if lc[1] != 0:
            lb, lc = lc, lb
            
    div(lb, 1)
 
if lc[0] != 0:
    sub(lc, la, 0)

if lc[1] != 0:
    sub(lc, lb, 1)

if lc[2] != 1:
    div(lc, 2)

if ld[0] != 0:
    sub(ld, la, 0)

if ld[1] != 0:
    sub(ld, lb, 1)

if ld[2] != 0:
    sub(ld, lc, 2)

if ld[3] != 1:
    div(lc, 3) 

ic = float(round(lc[3], 2))
ib = float(round((lb[3] - lb[2]*ic),2))
ia = float(round((la[3] - (la[1]*ib + la[2]*ic)), 2))
print(la, lb, lc, ld)