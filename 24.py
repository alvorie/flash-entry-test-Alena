f=open("hh.txt")
a=f.readline()
f.close()
k=0
mk=[0]*3
for i in range (0,len(a)-2,3):
    if (a[i] == 'C' or a[i] == 'D' or a[i] == 'F') and (a[i+1] == 'C' or a[i+1] == 'D' or a[i+1] == 'F') and (a[i+2]=='A' or a[i+2]=='O'):
        k+=1
        mk[0]= max(mk[0],k)
    else:
        k=0
for i in range (1,len(a)-2,3):
    if (a[i] == 'C' or a[i] == 'D' or a[i] == 'F') and (a[i+1] == 'C' or a[i+1] == 'D' or a[i+1] == 'F') and (a[i+2]=='A' or a[i+2]=='O'):
        k+=1
        mk[1]= max(mk[1],k)
    else:
        k=0
for i in range (2,len(a)-2,3):
    if (a[i] == 'C' or a[i] == 'D' or a[i] == 'F') and (a[i+1] == 'C' or a[i+1] == 'D' or a[i+1] == 'F') and (a[i+2]=='A' or a[i+2]=='O'):
        k+=1
        mk[2]= max(mk[2],k)
    else:
        k=0
print(max(mk))