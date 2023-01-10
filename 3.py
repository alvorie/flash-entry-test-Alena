a='polina'
mas=[]
for s1 in a:
    for s2 in a:
        for s3 in a:
            for s4 in a:
                for s5 in a:
                    for s6 in a:
                        for s7 in a:
                            if s1!='a':
                                s=s1+s2+s3+s4+s5+s6+s7
                            if s.count('p')==1 and s.count('a')==1:
                                mas.append(s)
mas=set(mas)
print(len(mas))