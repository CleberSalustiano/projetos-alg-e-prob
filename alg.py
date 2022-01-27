def forInput():
  ic = [[],[],[]]
  for i in range(0,3):
    for j in range (0,4):
        print('Digite o valor da coluna:', j, ' linha:',i)
        ic[i].append(int(input()))
  return ic
  
ic = [[1,1,-1,0], [0,3.5,3.4,0], [3.4,-3.5,0,4.2]]

if ic[1][0] != 0:
  if ic[0][0] != 0:
    turnZero = ic[0]
  elif ic[2][0] != 0:
    turnZero = ic[2]
  
  if (turnZero[0] != 1):
    turnZerofirst = turnZero[0]
    for i in range(0, len(turnZero)):
      turnZero[i] = turnZero[i]/turnZerofirst
  
  for i in range(0, len(turnZero)):
    ic[1][i] = ic[1][i] - turnZero[i]*ic[1][0]
if ic[1][1] != 1:
  i = 0
  value = ic[1][1]
  for element in ic[1]:
    ic[1][i] = float(round(element/value, 2))
    print(ic[1][i])
    i += 1

if ic[2][0] != 0:
  if ic[0][0] != 0:
    turnZero = ic[0]
  elif ic[1][0] != 0:
    turnZero = ic[1]
  
  if (turnZero[0] != 1):
    turnZerofirst = turnZero[0]
    for i in range(0, len(turnZero)):
      turnZero[i] = turnZero[i]/turnZerofirst
  
  for i in range(0, len(turnZero)):
    ic[2][i] = ic[2][i] - turnZero[i]*ic[2][0]
    
if ((ic[2][0] == 0 and ic[2][2] == 0) or (ic[2][1]==0 and ic[2][0] == 0)):
  print(ic)

elif ic[2][1] != 0:
  turnZero = ic[1]
  for i in range(0, len(turnZero)):
    ic[2][i] = ic[2][i] - turnZero[i]*ic[2][1]


  if ic[2][2] != 1:
    i = 0
    value = ic[2][2]
    for element in ic[2]:
      ic[2][i] = float(round(element/value, 2))
      print(ic[2][i])
      i += 1