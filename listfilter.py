listONE = [0,3,4,0,22,1]
listTWO = [n for n in listONE if n > 0]
print(listTWO)

listTHREE = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']
listFOUR = [cl for cl in listTHREE if 'ITEC' in cl]
print(listFOUR)

listFIVE = [0, 10, 4, 0, 32]
listSIX = [n * 2 for n in listFIVE if n > 0]
print(listSIX)
