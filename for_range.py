exp = [230, 23, 432, 143, 323, 234, 2343, 23]
total =0
for i in range(len(exp)):
    print ('Month:' ,(i+1) ,'Expense:' ,exp[i])
    total =total +exp[i]

print( "Total" ,total)