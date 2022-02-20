
Python=[9,22,27,32,35,'Python']
JavaScript=[8,18,12,6,15,'JavaScript']
Twitter=[10,18,26,16,12,'Twitter']
GitHub=[2,6,17,5,10,'GitHub']
Gephi=[11,16,14,10,9,'Gephi']
GeoNames=[2,4,3,1,8,'GeoNames']
Transkribus=[0,1,2,1,8,'Transkribus']
Excel=[5,9,3,6,7,'Excel']
MySQL=[0,6,9,5,7,'MySQL']
tools=[Python,JavaScript,Twitter,GitHub,Gephi,GeoNames,Transkribus,Excel,MySQL]
       
for i in tools:
    print(i[-1])
    print("2015: "+str(i[0]))
    print("2019: "+str(i[-2]))
    print("Sum: "+str(sum(i[:-1])))
