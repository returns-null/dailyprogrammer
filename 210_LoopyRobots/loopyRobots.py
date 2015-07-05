def loopyRobots(s):
    def n(c): return s.count(c)  
    z = lambda i: print("Loop detected! "+str(i)+\
                         ' cycle(s) needed to complete loop.')\
                         if i > 0 else print('No loop detected!') 
    m = lambda i: abs(i)%4

    a = 'SRL'
    o = 0
    p = [o,o]
    x = {0:o,1:1,2:o,3:-1}
    y = {0:1,1:o,2:-1,3:o}

    for c in s:
        if  c==a[0]:
            p[0]+=x[o]
            p[1]+=y[o]
        elif c==a[1]:
            o=m((o+1))
        elif c==a[2]:
            o=m((o-1))
    if (p[0]==p[1]==o):
        z(1)
    else:
        f=m(n(a[1]))-m(n(a[2]))
        if f==0:
            z(0)
        elif m(f)==2:
            z(2)
        else:
            z(4)
			
loopyRobots('SR')
loopyRobots('S')
loopyRobots('SRLLRLRLSSS')
>>> loopyRobots('SRLLRLRLSSSSSSRRRLRLR')
>>> loopyRobots('SRLLRLRLSSSSSSRRRLRLRSSLSLS')
>>> loopyRobots('LSRS')
>>> loopyRobots('RRRR')