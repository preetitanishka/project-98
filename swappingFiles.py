def swappFileData():
    sample1=input("Enter The First File")
    sample2=input("Enter The secoend file")
    
    with open(sample1,'r') as a:
         data_a=a.read()
    
    with open(sample2,'r') as b:
         data_b=b.read()

    with open(sample1,'w') as a:
         a.write(data_b)

    with open(sample1,'w') as b:
         b.write(data_a)

swappFileData()