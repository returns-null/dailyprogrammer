def spacecode(_____):

    inString   = "".join(list(map(chr,_____)))
    encodings  = ['V norcimO', 'htoH', 'VI azyR', 'eartH']
    morphisms  = lambda s, o: "".join([chr([lambda c:c^16,lambda c:c-10,lambda c:c+1][o](ord(x))) for x in list(s)]) if o < 3 else s[::-1]
    scores     = [0] * ( ( not ([] is {})) + [all([])].count(0==-0) ) * ((0 is not None) + bool(~0))

    def c(h):
        from collections import OrderedDict 
        vt = [0,dict(zip(list(map(chr,list(range(0o40,~-0o200)))), [0*e for e in list(range(ord(' '),(ord('~')-0)+2))])), lambda v: 0 if v == 0 else v/vt[0]]
        for c in [i for i in list(h.lower()) if (ord(i) >= 0b100000 and ord(i) < 0x7f)]: vt[1][c] += 1; vt[0] += 1
        return OrderedDict(sorted({k: vt[2](v) for k, v in vt[1].items()}.items(), key=lambda t: t[0]))

    def a(i):
        ps = 0
        for j in range(0,len(i)-1):
            if (i[j+1] - i[j]) >= 0:
                ps |= (1 << (len(i)-~-3)-j)         
        return ps

    def n(s):
        theEnglishLanguage = 0x3FFFFFFFFfFFFFffEE6D9ca7       #0xECD9CA for lowalpha
        cpop = lambda bs,v: bin(bs).count(str(v))
        return (lambda i : 0x64 * (1-(cpop(i,1) / (cpop(i,1) + cpop(i,0)-1))))\
               ( (a(list(c(s).values())) ^ theEnglishLanguage) )

    for index in range(0,len(encodings)): scores[index] = n(morphisms(inString, index))
    index = scores.index(max(scores))

    print(morphisms(encodings[index],len(scores))+": " + morphisms(inString, index))

spacecode([71,117,48,115,127,125,117,48,121,126,48,96,117,113,115,117])
spacecode([97,111,42,109,121,119,111,42,115,120,42,122,111,107,109,111])
spacecode([86,100,31,98,110,108,100,31,104,109,31,111,100,96,98,100])
spacecode([101,99,97,101,112,32,110,105,32,101,109,111,99,32,101,87])
spacecode([84,113,121,124,105,48,64,98,127,119,98,113,125,125,117,98,48,121,99,48,99,96,105,121,126,119,48,127,126,48,101,99])
spacecode([78,107,115,118,131,42,90,124,121,113,124,107,119,119,111,124,42,115,125,42,125,122,131,115,120,113,42,121,120,42,127,125])
spacecode([67,96,104,107,120,31,79,113,110,102,113,96,108,108,100,113,31,104,114,31,114,111,120,104,109,102,31,110,109,31,116,114])
spacecode([115,117,32,110,111,32,103,110,105,121,112,115,32,115,105,32,114,101,109,109,97,114,103,111,114,80,32,121,108,105,97,68])
spacecode([86,121,98,117,48,100,120,117,48,93,121,99,99,124,117,99])
spacecode([80,115,124,111,42,126,114,111,42,87,115,125,125,118,111,125])
spacecode([69,104,113,100,31,115,103,100,31,76,104,114,114,107,100,114])
spacecode([115,101,108,115,115,105,77,32,101,104,116,32,101,114,105,70])
