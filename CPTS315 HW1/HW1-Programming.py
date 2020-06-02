c1 = {}
c2 = {}
c3 = {}

L1 = []
L2 = []
L3 = []

F1 = {}



s = 3


#file = open("test.txt", "r")
#file = open("browsingdata.txt", "r")

def itemcount1():
    file = open("browsingdata.txt", "r")
    for line in file:
        for word in line.split():
            c1[word] = c1.get(word, 0) + 1
    file.close()

def filter1(s):
    for item in c1:
        if (c1.get(item) > s):
            L1.append(item)

def pairmaker1(L, M):
    i = -1
    while (i <= (len(L) - 1)):
        i += 1
        j = i+1
        while (j <= (len(L) - 1)):
            M.append(L[i]+' '+L[j])
            j += 1

def itemcount2(L, c2):
    file = open("browsingdata.txt", "r")
    for line in file:
        i = 0
        while (i <= (len(L) - 1)):
            x, y = L[i].split()
            if (x in line) and (y in line):
                c2[L[i]] = c2.get(L[i], 0) + 1
            i += 1
    file.close()

def filter2(s):
    for item in c2:
        if (c2.get(item) > s):
            L3.append(item)

def confPair():
    for item in L3:
        x, y = item.split()
        D = c2[item]
        N = c1[x]
        conf = ((c2[item]) / (c1[x]))
        F1[item] = conf

def print1():
    x = sorted(F1, key=F1.get, reverse=True)
    i = 0
    print('OUTPUT A')
    while (i != 5):
        print(x[i],' ', F1[x[i]])
        i += 1
    
    
    
        

itemcount1()
filter1(s)
pairmaker1(L1, L2)
itemcount2(L2, c2)
filter2(s)
confPair()
print1()







    
