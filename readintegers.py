f=open('integers.txt', 'r')
theSum=0
for index in f:
    theSum=theSum+int(index)
print(theSum)
#print(index)
#print(f.read())
f.close()