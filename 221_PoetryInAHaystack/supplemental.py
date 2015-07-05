def markovLetter(filename):
    with open(filename, "r") as inputFile:
        transMat = [[0]*26 for i in range(26)]
        divisor = [0]*26
        for line in inputFile:
            for word in line.upper().split(' '):
                for i in range(len(word)-1):
                    cur = ord(word[i])-65
                    nex = ord(word[i+1])-65
                    if (cur < 26 and nex < 26 and cur > -1 and nex > -1):
                        divisor[cur] += 1
                        transMat[cur][nex] += 1
        for i in range(26):
            for j in range(26):
                if divisor[i] != 0:
                    transMat[i][j] /= divisor[i]
        return transMat
				

def impbigrams(filename):
    impDict = {value[0]: value[1:] for value in ['zzyxwvutsrqponmlkjihgfedcba', 'yzyxwvutsrqponmlkjhgfedcba', 'xzyxwvutsrqponmlkjihgfedcba', 'wzyxwvutsrqpomlkjgfdcba', 'vzyxwvtsrqponmlkjihgfdcba', 'uzyxwvuqomkjihfedcba', 'tzyxwvtsqpnmkjigfedcba', 'szyxwvurqpnmlkjhgfdcba', 'rzxwvutqpnmlkjihgfdcb', 'qzyxwvutsrqponmlkjihgfedcba', 'pzyxwvutsqpnmlkjihgfdcba', 'ozyxsqpolkjihecba', 'nzxwvurqpnmlkjihfcba', 'mzyxwvutsrqponmlkjihgfdcb', 'lzyxwvurqponmkjihgcba', 'kzyxwvutsrqponmlkjhgfedcba', 'jzyxwvutsrqpnmlkjihgfedcba', 'izyxwvusqpomkjihgfba', 'hzyxwvsrqponmlkjhgfdcb', 'gzyxwvutqpnmlkjigfdcba', 'fzyxwvtsqpnmlkjhgfdcba', 'ezxwvtqpomkjihgfecb', 'dzyxwvutsrqpnmlkjhgfcb', 'czyxwvutsrqpnmlkjigfedcba', 'bzyxwvutsqponmlkjihgfedcba', 'azxwusrqpomlkjihgfba']}
    print(impDict)
    with open(filename, "r") as inputFile:
        for line in inputFile:
            linescore = 1;
            for word in line.lower().split(' '):
                for i in range(len(word)-1):
                    if (word[i] in impDict) and ( word[i+1] in impDict[word[i]]):
                        linescore = -1
                        break
                if linescore == -1:
                    continue
            if (linescore == 1):
                print(line)