Python=[9,22,27,32,35,'Python']
JavaScript=[8,18,12,6,15,'JavaScript']
Twitter=[10,18,26,16,12,'Twitter']
GitHub=[2,6,17,5,10,'GitHub']
Gephi=[11,16,14,10,9,'Gephi']
GeoNames=[2,4,3,1,8,'GeoNames']
Transkribus=[0,1,2,1,8,'Transkribus']
Excel=[5,9,3,6,7,'Excel']
MySQL=[0,6,9,5,7,'MySQL']
CollateX=[3,4,7,3,6,"CollateX"]
Natural_Language_Toolkit=[3,4,7,3,6,"Natural_Langage_Toolkit"]
Omeka=[4,9,11,14,6,"Omeka"]
PostgreSQL=[2,3,3,1,6,"PostgreSQL"]
stylo=[4,13,6,6,6,"stylo"]
Bootstrap=[1,3,4,1,5,"Bootstrap"]
Drupal=[1,6,5,2,5,"Drupal"]
eXist_db=[0,4,2,2,5,"eXist_db"]
Google_Books=[6,8,8,4,5,"Google_Books"]
TextGrid=[5,7,2,0,5,"TextGrid"]
tools=[Python,JavaScript,Twitter,GitHub,Gephi,GeoNames,Transkribus,Excel,MySQL,CollateX,Natural_Language_Toolkit,Omeka,PostgreSQL,stylo,Bootstrap,Drupal,eXist_db,Google_Books,TextGrid]
tool=input("Enter tool name: ")

for i in tools:
    if str(tool) in i:
        print("2015: "+str(i[0]))
        print("2019: "+str(i[-2]))
        print("Sum: "+str(sum(i[:-1])))
