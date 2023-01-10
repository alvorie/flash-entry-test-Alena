M = 5*15**0 + 3*15**2 + 2*15**3 + 2*15**5
# значит, х переводим в 10 cc как х*15, а у как у*15**4
N = 9*13 + 7*13**3 + 6*13**4
# значит, y переводим в 10 cc как y, а x как x*13**2
flag = 0
for a in range (1,100000):
    for x in range (13):
        for y in range (13):
            M1 = M + x*15 + y*15**4
            N1 = N + y + x*13**2
            if ((M1+a)%N1==0):
                print(a)
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        break