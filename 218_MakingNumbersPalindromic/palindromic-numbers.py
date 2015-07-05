def palin(n):
    o = n; k = 0; _=lambda s:str(s);
    while _(n) != _(n)[::-1]: n = int(_(n)[::-1])+n; k+=1 
    print(_(o) + " gets palindromic after " + _(k) + " steps: " + _(n))
while 1: l = input(); palin(int(l)) if len(l)>1 else exit(); 

def notbonus1():                  
    return list(filter(lambda n: str(n)==str(n)[::-1], list(range(1,1001))))

def bonus1():                       
    lookup = {}
    for i in range(1,1001):
        j = i
        if j in [196,295,394,493,592,689,691,788, 790, 879, 887, 978, 986]:
            continue
        while str(j) != str(j)[::-1]:
            j = int(str(j)[::-1])+j
        if j not in lookup:
            lookup[j] = list()
        lookup[j].append(i)


    palinSets = {(k,str(v)) for k,v in lookup.items()}
    return palinSets

def bonus2():
    intractable = []
    for i in range(1,1001):
        j = i; iterCnt = 0
        while str(j) != str(j)[::-1]:
            j = int(str(j)[::-1])+j
            iterCnt += 1
            if iterCnt == 10000:
                intractable.append(i)
                break
    return intractable