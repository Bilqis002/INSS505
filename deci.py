f=open('decimal.txt','r')
#read=r
#write=w
#append=a
add=0
for index in f:
    add=add+float(index)
print(add)
f.close()

#print(getcwd())

f=open('decimal.txt','a')
f.write('\n12.0')
f.close()
#f.write('12.0',end=)

