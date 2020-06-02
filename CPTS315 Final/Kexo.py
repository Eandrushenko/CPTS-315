#Global Variables
planets = []

#Center list (K=4)
c1 = []
c2 = []
c3 = []
c4 = []

#Scores for Euclidean Centers
s1 = []
s2 = []
s3 = []
s4 = []

#hold the centers
h1 = []
h2 = []
h3 = []
h4 = []

#Function Definitions
def init():
    file = open("exoplanet.csv", "r")
    for line in file:
        x = line.split(',')
        i = 1
        while (i < 17):
            x[i] = float(x[i])
            i = i+1
        planets.append(x)
    file.close()

def makecenters(center1, center2, center3, center4, h1, h2, h3, h4):
    a = planets[423]
    b = planets[422]
    c = planets[424]
    d = planets[425]
    center1.append(a)
    center2.append(b)
    center3.append(c)
    center4.append(d)
    h1 = a
    h2 = b
    h3 = c
    h4 = d
    return center1, center2, center3, center4, h1, h2, h3, h4

def euclid(exo):
    psum = 0
    i = 1
    while (i < 17):
        psum += (exo[i]**2)
        i = i+1
    psum = psum**0.5
    return psum

def updatecenter(c):
    s = []
    i = 0
    while (i < 18):
        s.append(0)
        i = i + 1
    i = 1
    while (i < 17):
        for items in c:
            s[i] = s[i] + items[i]
        s[i] = s[i] / len(c)
        i = i + 1
    return s
        
def cluster(c1, c2, c3, c4, new):
    s1 = updatecenter(c1)
    s2 = updatecenter(c2)
    s3 = updatecenter(c3)
    s4 = updatecenter(c4)
    e1 = euclid(s1)
    e2 = euclid(s2)
    e3 = euclid(s3)
    e4 = euclid(s4)
    newitem = euclid(new)
    e1 = abs(newitem - e1)
    e2 = abs(newitem - e2)
    e3 = abs(newitem - e3)
    e4 = abs(newitem - e4)
    if ((e1 <= e2) and (e1 <= e3) and (e1 <= e4)):
        c1.append(new)
    elif ((e2 <= e1) and (e2 <= e3) and (e2 <= e4)):
        c2.append(new)
    elif ((e3 <= e1) and (e3 <= e2) and (e3 <= e4)):
        c3.append(new)
    elif((e4 <= e1) and (e4 <= e2) and (e4 <= e3)):
        c4.append(new)
    return c1, c2, c3, c4

def clusterALL(c1, c2, c3, c4, item):
    for things in item:
        c1, c2, c3, c4 = cluster(c1, c2, c3, c4, things)
    return c1, c2, c3, c4

def putback(h1, h2, h3, h4, item):
    item.append(h1)
    item.append(h2)
    item.append(h3)
    item.append(h4)
    return item

def check(c1, c2, c3, c4, item):
    if item in c1:
        c1.remove(item)
    elif item in c2:
        c2.remove(item)
    elif item in c3:
        c3.remove(item)
    elif item in c4:
        c4.remove(item)
    c1, c2, c3, c4 = cluster(c1, c2, c3, c4, item)
    return c1, c2, c3, c4

def checkALL(c1, c2, c3, c4, item):
    for things in item:
        c1, c2, c3, c4 = check(c1, c2, c3, c4, things)
    return c1, c2, c3, c4

def Ksearch(c1, c2, c3, c4, item):
    if item in c1:
       print("c1")
    if item in c2:
       print("c2")
    if item in c3:
       print("c3")
    if item in c4:
       print("c4")
    
        
    
#Run Code
init()
c1, c2, c3, c4, h1, h2, h3, h4 = makecenters(c1, c2, c3, c4, h1, h2, h3, h4)
c1, c2, c3, c4 = clusterALL(c1, c2, c3, c4, planets)
planets = putback(h1, h2, h3, h4, planets)
i = 0
c1, c2, c3, c4 = checkALL(c1, c2, c3, c4, planets)
Ksearch(c1, c2, c3, c4, planets[3367]) #Earth
Ksearch(c1, c2, c3, c4, planets[3317]) #Kepler-22b

#len(planets)
#len(c1) + len(c2) + len(c3) + len(c4)
s1 = updatecenter(c1)
s2 = updatecenter(c2)
s3 = updatecenter(c3)
s4 = updatecenter(c4)
e1 = euclid(s1)
e2 = euclid(s2)
e3 = euclid(s3)
e4 = euclid(s4)




