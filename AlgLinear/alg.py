def div(ix, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i]/const

def sub(ix, iy, x):
    const = ix[x]
    for i in range(0, len(ix)):
        ix[i] = ix[i] - iy[i]*const

def verifMatriz(matriz):
    for line in matriz:
        if len(matriz) + 1 != len(line):
            print('Digite uma matriz válida para solução de todos os valores')
            exit() 
    print('Matriz válida')

def returnLines(matriz):
    if len(matriz) == 2:
        la = [matriz[0][0], matriz[0][1], matriz[0][2],0,0]
        lb = [matriz[1][0], matriz[1][1], matriz[1][2],0,0]
        lc = [0,0,0,0,0]
        ld = [0,0,0,0,0]
    elif len(matriz) == 3:
        la = [matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],0]
        lb = [matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3],0]
        lc = [matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],0]
        ld = [0,0,0,0,0]
    elif len(matriz) == 4:
        la = matriz[0]
        lb = matriz[1]
        lc = matriz[2]
        ld = matriz[3]
    la,lb,lc,ld = lineLadder(la,lb,lc,ld)
    return la,lb,lc,ld

def lineLadder(la,lb,lc,ld):
    if la[0] == 0:
        if lb[0] != 0:
            la, lb = lb, la
        elif lc[0] != 0:
            la, lc = lc, la
    div(la, 0)

    if lb[0] != 0:
        sub(lb, la, 0)
        
    if lb[1] == 0:
        if lc[1] != 0:
            lb, lc = lc, lb    
    div(lb, 1)

    if lc != [0,0,0,0,0]:
        if lc[0] != 0:
            sub(lc, la, 0)

        if lc[1] != 0:
            sub(lc, lb, 1)
        
        if ld != [0,0,0,0,0]:
            if lc[2] != 1:
                if lc[2] == 0:
                    if ld[2] != 0:
                        lc, ld = ld, lc
            div(lc, 2)
        else: 
            div(lc, 2)

    if ld != [0,0,0,0,0]:
        if ld[0] != 0:
            sub(ld, la, 0)
        if ld[1] != 0:
            sub(ld, lb, 1)
        if ld[2] != 0:
            sub(ld, lc, 2)
        div(lc, 3) 
    return la,lb,lc,ld

def findCurrent(la,lb,lc,ld):
    if lc == [0,0,0,0,0] and ld == [0,0,0,0,0]:
        ib = float(round(lb[2],2))
        ia = float(round(la[2] - la[1]*ib, 2))
        ic = 'a'
        idd = 'a' 
    elif ld == [0,0,0,0,0]:
        ic = float(round(lc[3], 2))
        ib = float(round((lb[3] - lb[2]*ic),2))
        ia = float(round((la[3] - (la[1]*ib + la[2]*ic)), 2))
        idd = 'a'
    else:
        idd = ldd[4]
        ic = float(round(lc[4] - lc[3]*idd,2))
        ib = float(round(ib[4] - (lb[3]*idd + lb[2]*ic),2))
        ia = float(round(lb[4] - (lb[3]*idd + lb[2]*ic + lb[1]*ib),2)) 

    if ic == 'a' and idd == 'a':
        print('Ia =', ia, '\nIb =', ib)
    elif idd == 'a':
        print('Ia =', ia, '\nIb =', ib, '\nIc =', ic)
    else:
        print('Ia =', ia, '\nIb =', ib, '\nIc =', ic, '\nId =', idd)
    return ia,ib,ic,idd

matriz = [[0,3.5,3.4,0],  
          [1,1,-1,0], 
          [3.4,-3.5,0,4.2]]

verifMatriz(matriz)
la, lb, lc, ld = returnLines(matriz)
ia, ib, ic, idd = findCurrent(la, lb, lc, ld)

