#Global Variables
planets = []

#Center list (K=4)
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
c10 = []
c11 = []
c12 = []
c13 = []
c14 = []
c15 = []
c16 = []
c17 = []
c18 = []
c19 = []
c20 = []
c21 = []
c22 = []
c23 = []
c24 = []
c25 = []
c26 = []
c27 = []
c28 = []
c29 = []
c30 = []


#Scores for Euclidean Centers
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []
s10 = []
s11 = []
s12 = []
s13 = []
s14 = []
s15 = []
s16 = []
s17 = []
s18 = []
s19 = []
s20 = []
s21 = []
s22 = []
s23 = []
s24 = []
s25 = []
s26 = []
s27 = []
s28 = []
s29 = []
s30 = []

#hold the centers
h1 = []
h2 = []
h3 = []
h4 = []
h5 = []
h6 = []
h7 = []
h8 = []
h9 = []
h10 = []
h11 = []
h12 = []
h13 = []
h14 = []
h15 = []
h16 = []
h17 = []
h18 = []
h19 = []
h20 = []
h21 = []
h22 = []
h23 = []
h24 = []
h25 = []
h26 = []
h27 = []
h28 = []
h29 = []
h30 = []

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

def makecenters(center1, center2, center3, center4, center5, center6, center7, center8, center9, center10, center11, center12, center13, center14, center15, center16, center17, center18, center19, center20, center21, center22, center23, center24, center25, center26, center27, center28, center29, center30, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30):
    a = planets[423]
    b = planets[422]
    c = planets[424]
    d = planets[425]
    e = planets[426]
    f = planets[427]
    g = planets[428]
    h = planets[429]
    i = planets[430]
    j = planets[431]
    k = planets[432]
    l = planets[433]
    m = planets[434]
    n = planets[435]
    o = planets[436]
    p = planets[437]
    q = planets[438]
    r = planets[439]
    s = planets[440]
    t = planets[441]
    u = planets[442]
    v = planets[443]
    w = planets[444]
    x = planets[445]
    y = planets[446]
    z = planets[447]
    aa = planets[448]
    bb = planets[449]
    cc = planets[450]
    dd = planets[451]
    center1.append(a)
    center2.append(b)
    center3.append(c)
    center4.append(d)
    center5.append(e)
    center6.append(f)
    center7.append(g)
    center8.append(h)
    center9.append(i)
    center10.append(j)
    center11.append(k)
    center12.append(l)
    center13.append(m)
    center14.append(n)
    center15.append(o)
    center16.append(p)
    center17.append(q)
    center18.append(r)
    center19.append(s)
    center20.append(t)
    center21.append(u)
    center22.append(v)
    center23.append(w)
    center24.append(x)
    center25.append(y)
    center26.append(z)
    center27.append(aa)
    center28.append(bb)
    center29.append(cc)
    center30.append(dd)
    h1 = a
    h2 = b
    h3 = c
    h4 = d
    return center1, center2, center3, center4, center5, center6, center7, center8, center9, center10, center11, center12, center13, center14, center15, center16, center17, center18, center19, center20, center21, center22, center23, center24, center25, center26, center27, center28, center29, center30, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30

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
        a = len(c)
        if (a == 0):
            a = 1
        s[i] = s[i] / a
        i = i + 1
    return s
        
def cluster(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, new):
    s1 = updatecenter(c1)
    s2 = updatecenter(c2)
    s3 = updatecenter(c3)
    s4 = updatecenter(c4)
    s5 = updatecenter(c5)
    s6 = updatecenter(c6)
    s7 = updatecenter(c7)
    s8 = updatecenter(c8)
    s9 = updatecenter(c9)
    s10 = updatecenter(c10)
    s11 = updatecenter(c11)
    s12 = updatecenter(c12)
    s13 = updatecenter(c13)
    s14 = updatecenter(c14)
    s15 = updatecenter(c15)
    s16 = updatecenter(c16)
    s17 = updatecenter(c17)
    s18 = updatecenter(c18)
    s19 = updatecenter(c19)
    s20 = updatecenter(c20)
    s21 = updatecenter(c21)
    s22 = updatecenter(c22)
    s23 = updatecenter(c23)
    s24 = updatecenter(c24)
    s25 = updatecenter(c25)
    s26 = updatecenter(c26)
    s27 = updatecenter(c27)
    s28 = updatecenter(c28)
    s29 = updatecenter(c29)
    s30 = updatecenter(c30)
    e1 = euclid(s1)
    e2 = euclid(s2)
    e3 = euclid(s3)
    e4 = euclid(s4)
    e5 = euclid(s5)
    e6 = euclid(s6)
    e7 = euclid(s7)
    e8 = euclid(s8)
    e9 = euclid(s9)
    e10 = euclid(s10)
    e11 = euclid(s11)
    e12 = euclid(s12)
    e13 = euclid(s13)
    e14 = euclid(s14)
    e15 = euclid(s15)
    e16 = euclid(s16)
    e17 = euclid(s17)
    e18 = euclid(s18)
    e19 = euclid(s19)
    e20 = euclid(s20)
    e21 = euclid(s21)
    e22 = euclid(s22)
    e23 = euclid(s23)
    e24 = euclid(s24)
    e25 = euclid(s25)
    e26 = euclid(s26)
    e27 = euclid(s27)
    e28 = euclid(s28)
    e29 = euclid(s29)
    e30 = euclid(s30)
    newitem = euclid(new)
    e1 = abs(newitem - e1)
    e2 = abs(newitem - e2)
    e3 = abs(newitem - e3)
    e4 = abs(newitem - e4)
    e5 = abs(newitem - e5)
    e6 = abs(newitem - e6)
    e7 = abs(newitem - e7)
    e8 = abs(newitem - e8)
    e9 = abs(newitem - e9)
    e10 = abs(newitem - e10)
    e11 = abs(newitem - e11)
    e12 = abs(newitem - e12)
    e13 = abs(newitem - e13)
    e14 = abs(newitem - e14)
    e15 = abs(newitem - e15)
    e16 = abs(newitem - e16)
    e17 = abs(newitem - e17)
    e18 = abs(newitem - e18)
    e19 = abs(newitem - e19)
    e20 = abs(newitem - e20)
    e21 = abs(newitem - e21)
    e22 = abs(newitem - e22)
    e23 = abs(newitem - e23)
    e24 = abs(newitem - e24)
    e25 = abs(newitem - e25)
    e26 = abs(newitem - e26)
    e27 = abs(newitem - e27)
    e28 = abs(newitem - e28)
    e29 = abs(newitem - e29)
    e30 = abs(newitem - e30)
    if ((e1 <= e2) and (e1 <= e3) and (e1 <= e4) and (e1 <= e5) and (e1 <= e6) and (e1 <= e7) and (e1 <= e8) and (e1 <= e9) and (e1 <= e10) and (e1 <= e11) and (e1 <= e12) and (e1 <= e13) and (e1 <= e14) and (e1 <= e15) and (e1 <= e16) and (e1 <= e17) and (e1 <= e18) and (e1 <= e19) and (e1 <= e20) and (e1 <= e21) and (e1 <= e22) and (e1 <= e23) and (e1 <= e24) and (e1 <= e25) and (e1 <= e26) and (e1 <= e27) and (e1 <= e28) and (e1 <= e29) and (e1 <= e30)):
        c1.append(new)
    elif ((e2 <= e1) and (e2 <= e3) and (e2 <= e4) and (e2 <= e5) and (e2 <= e6) and (e2 <= e7) and (e2 <= e8) and (e2 <= e9) and (e2 <= e10) and (e2 <= e11) and (e2 <= e12) and (e2 <= e13) and (e2 <= e14) and (e2 <= e15) and (e2 <= e16) and (e2 <= e17) and (e2 <= e18) and (e2 <= e19) and (e2 <= e20) and (e2 <= e21) and (e2 <= e22) and (e2 <= e23) and (e2 <= e24) and (e2 <= e25) and (e2 <= e26) and (e2 <= e27) and (e2 <= e28) and (e2 <= e29) and (e2 <= e30)):
        c2.append(new)
    elif ((e3 <= e2) and (e3 <= e1) and (e3 <= e4) and (e3 <= e5) and (e3 <= e6) and (e3 <= e7) and (e3 <= e8) and (e3 <= e9) and (e3 <= e10) and (e3 <= e11) and (e3 <= e12) and (e3 <= e13) and (e3 <= e14) and (e3 <= e15) and (e3 <= e16) and (e3 <= e17) and (e3 <= e18) and (e3 <= e19) and (e3 <= e20) and (e3 <= e21) and (e3 <= e22) and (e3 <= e23) and (e3 <= e24) and (e3 <= e25) and (e3 <= e26) and (e3 <= e27) and (e3 <= e28) and (e3 <= e29) and (e3 <= e30)):
        c3.append(new)
    elif ((e4 <= e2) and (e4 <= e1) and (e4 <= e3) and (e4 <= e5) and (e4 <= e6) and (e4 <= e7) and (e4 <= e8) and (e4 <= e9) and (e4 <= e10) and (e4 <= e11) and (e4 <= e12) and (e4 <= e13) and (e4 <= e14) and (e4 <= e15) and (e4 <= e16) and (e4 <= e17) and (e4 <= e18) and (e4 <= e19) and (e4 <= e20) and (e4 <= e21) and (e4 <= e22) and (e4 <= e23) and (e4 <= e24) and (e4 <= e25) and (e4 <= e26) and (e4 <= e27) and (e4 <= e28) and (e4 <= e29) and (e4 <= e30)):
        c4.append(new)
    elif ((e5 <= e2) and (e5 <= e1) and (e5 <= e3) and (e5 <= e4) and (e5 <= e6) and (e5 <= e7) and (e5 <= e8) and (e5 <= e9) and (e5 <= e10) and (e5 <= e11) and (e5 <= e12) and (e5 <= e13) and (e5 <= e14) and (e5 <= e15) and (e5 <= e16) and (e5 <= e17) and (e5 <= e18) and (e5 <= e19) and (e5 <= e20) and (e5 <= e21) and (e5 <= e22) and (e5 <= e23) and (e5 <= e24) and (e5 <= e25) and (e5 <= e26) and (e5 <= e27) and (e5 <= e28) and (e5 <= e29) and (e5 <= e30)):
        c5.append(new)
    elif ((e6 <= e2) and (e6 <= e1) and (e6 <= e3) and (e6 <= e4) and (e6 <= e5) and (e6 <= e7) and (e6 <= e8) and (e6 <= e9) and (e6 <= e10) and (e6 <= e11) and (e6 <= e12) and (e6 <= e13) and (e6 <= e14) and (e6 <= e15) and (e6 <= e16) and (e6 <= e17) and (e6 <= e18) and (e6 <= e19) and (e6 <= e20) and (e6 <= e21) and (e6 <= e22) and (e6 <= e23) and (e6 <= e24) and (e6 <= e25) and (e6 <= e26) and (e6 <= e27) and (e6 <= e28) and (e6 <= e29) and (e6 <= e30)):
        c6.append(new)
    elif ((e7 <= e2) and (e7 <= e1) and (e7 <= e3) and (e7 <= e4) and (e7 <= e5) and (e7 <= e6) and (e7 <= e8) and (e7 <= e9) and (e7 <= e10) and (e7 <= e11) and (e7 <= e12) and (e7 <= e13) and (e7 <= e14) and (e7 <= e15) and (e7 <= e16) and (e7 <= e17) and (e7 <= e18) and (e7 <= e19) and (e7 <= e20) and (e7 <= e21) and (e7 <= e22) and (e7 <= e23) and (e7 <= e24) and (e7 <= e25) and (e7 <= e26) and (e7 <= e27) and (e7 <= e28) and (e7 <= e29) and (e7 <= e30)):
        c7.append(new)
    elif ((e8 <= e2) and (e8 <= e1) and (e8 <= e3) and (e8 <= e4) and (e8 <= e5) and (e8 <= e6) and (e8 <= e7) and (e8 <= e9) and (e8 <= e10) and (e8 <= e11) and (e8 <= e12) and (e8 <= e13) and (e8 <= e14) and (e8 <= e15) and (e8 <= e16) and (e8 <= e17) and (e8 <= e18) and (e8 <= e19) and (e8 <= e20) and (e8 <= e21) and (e8 <= e22) and (e8 <= e23) and (e8 <= e24) and (e8 <= e25) and (e8 <= e26) and (e8 <= e27) and (e8 <= e28) and (e8 <= e29) and (e8 <= e30)):
        c8.append(new)
    elif ((e9 <= e2) and (e9 <= e1) and (e9 <= e3) and (e9 <= e4) and (e9 <= e5) and (e9 <= e6) and (e9 <= e7) and (e9 <= e8) and (e9 <= e10) and (e9 <= e11) and (e9 <= e12) and (e9 <= e13) and (e9 <= e14) and (e9 <= e15) and (e9 <= e16) and (e9 <= e17) and (e9 <= e18) and (e9 <= e19) and (e9 <= e20) and (e9 <= e21) and (e9 <= e22) and (e9 <= e23) and (e9 <= e24) and (e9 <= e25) and (e9 <= e26) and (e9 <= e27) and (e9 <= e28) and (e9 <= e29) and (e9 <= e30)):
        c9.append(new)
    elif ((e10 <= e2) and (e10 <= e1) and (e10 <= e3) and (e10 <= e4) and (e10 <= e5) and (e10 <= e6) and (e10 <= e7) and (e10 <= e8) and (e10 <= e9) and (e10 <= e11) and (e10 <= e12) and (e10 <= e13) and (e10 <= e14) and (e10 <= e15) and (e10 <= e16) and (e10 <= e17) and (e10 <= e18) and (e10 <= e19) and (e10 <= e20) and (e10 <= e21) and (e10 <= e22) and (e10 <= e23) and (e10 <= e24) and (e10 <= e25) and (e10 <= e26) and (e10 <= e27) and (e10 <= e28) and (e10 <= e29) and (e10 <= e30)):
        c10.append(new)
    elif ((e11 <= e2) and (e11 <= e3) and (e11 <= e4) and (e11 <= e5) and (e11 <= e6) and (e11 <= e7) and (e11 <= e8) and (e11 <= e9) and (e11 <= e10) and (e11 <= e10) and (e11 <= e12) and (e11 <= e13) and (e11 <= e14) and (e11 <= e15) and (e11 <= e16) and (e11 <= e17) and (e11 <= e18) and (e11 <= e19) and (e11 <= e20) and (e11 <= e21) and (e11 <= e22) and (e11 <= e23) and (e11 <= e24) and (e11 <= e25) and (e11 <= e26) and (e11 <= e27) and (e11 <= e28) and (e11 <= e29) and (e11 <= e30)):
        c11.append(new)
    elif ((e12 <= e1) and (e12 <= e3) and (e12 <= e4) and (e12 <= e5) and (e12 <= e6) and (e12 <= e7) and (e12 <= e8) and (e12 <= e9) and (e12 <= e10) and (e12 <= e11) and (e12 <= e11) and (e2 <= e13) and (e12 <= e14) and (e12 <= e15) and (e12 <= e16) and (e12 <= e17) and (e12 <= e18) and (e12 <= e19) and (e12 <= e20) and (e12 <= e21) and (e12 <= e22) and (e12 <= e23) and (e12 <= e24) and (e12 <= e25) and (e12 <= e26) and (e12 <= e27) and (e12 <= e28) and (e12 <= e29) and (e12 <= e30)):
        c12.append(new)
    elif ((e13 <= e2) and (e13 <= e1) and (e13 <= e4) and (e13 <= e5) and (e13 <= e6) and (e13 <= e7) and (e13 <= e8) and (e13 <= e9) and (e13 <= e10) and (e13 <= e11) and (e13 <= e12) and (e13 <= e12) and (e13 <= e14) and (e13 <= e15) and (e13 <= e16) and (e13 <= e17) and (e13 <= e18) and (e13 <= e19) and (e13 <= e20) and (e13 <= e21) and (e13 <= e22) and (e13 <= e23) and (e13 <= e24) and (e13 <= e25) and (e13 <= e26) and (e13 <= e27) and (e13 <= e28) and (e13 <= e29) and (e13 <= e30)):
        c13.append(new)
    elif ((e14 <= e2) and (e14 <= e1) and (e14 <= e3) and (e14 <= e5) and (e14 <= e6) and (e14 <= e7) and (e14 <= e8) and (e14 <= e9) and (e14 <= e10) and (e14 <= e11) and (e14 <= e12) and (e14 <= e13) and (e14 <= e13) and (e14 <= e15) and (e14 <= e16) and (e14 <= e17) and (e14 <= e18) and (e14 <= e19) and (e14 <= e20) and (e14 <= e21) and (e14 <= e22) and (e14 <= e23) and (e14 <= e24) and (e14 <= e25) and (e14 <= e26) and (e14 <= e27) and (e14 <= e28) and (e14 <= e29) and (e14 <= e30)):
        c14.append(new)
    elif ((e15 <= e2) and (e15 <= e1) and (e15 <= e3) and (e15 <= e4) and (e15 <= e6) and (e15 <= e7) and (e15 <= e8) and (e15 <= e9) and (e15 <= e10) and (e15 <= e11) and (e15 <= e12) and (e15 <= e13) and (e15 <= e14) and (e15 <= e14) and (e15 <= e16) and (e15 <= e17) and (e15 <= e18) and (e15 <= e19) and (e15 <= e20) and (e15 <= e21) and (e15 <= e22) and (e15 <= e23) and (e15 <= e24) and (e15 <= e25) and (e15 <= e26) and (e15 <= e27) and (e15 <= e28) and (e15 <= e29) and (e15 <= e30)):
        c15.append(new)
    elif ((e16 <= e2) and (e16 <= e1) and (e16 <= e3) and (e16 <= e4) and (e16 <= e5) and (e16 <= e7) and (e16 <= e8) and (e16 <= e9) and (e16 <= e10) and (e16 <= e11) and (e16 <= e12) and (e16 <= e13) and (e16 <= e14) and (e16 <= e15) and (e16 <= e15) and (e16 <= e17) and (e16 <= e18) and (e16 <= e19) and (e16 <= e20) and (e16 <= e21) and (e16 <= e22) and (e16 <= e23) and (e16 <= e24) and (e16 <= e25) and (e16 <= e26) and (e16 <= e27) and (e16 <= e28) and (e16 <= e29) and (e16 <= e30)):
        c16.append(new)
    elif ((e17 <= e2) and (e17 <= e1) and (e17 <= e3) and (e17 <= e4) and (e17 <= e5) and (e17 <= e6) and (e17 <= e8) and (e17 <= e9) and (e17 <= e10) and (e17 <= e11) and (e17 <= e12) and (e17 <= e13) and (e17 <= e14) and (e17 <= e15) and (e17 <= e16) and (e17 <= e16) and (e17 <= e18) and (e17 <= e19) and (e17 <= e20) and (e17 <= e21) and (e17 <= e22) and (e17 <= e23) and (e17 <= e24) and (e17 <= e25) and (e17 <= e26) and (e17 <= e27) and (e17 <= e28) and (e17 <= e29) and (e17 <= e30)):
        c17.append(new)
    elif ((e18 <= e2) and (e18 <= e1) and (e18 <= e3) and (e18 <= e4) and (e18 <= e5) and (e18 <= e6) and (e18 <= e7) and (e18 <= e9) and (e18 <= e10) and (e18 <= e11) and (e18 <= e12) and (e18 <= e13) and (e18 <= e14) and (e18 <= e15) and (e18 <= e16) and (e18 <= e17) and (e18 <= e17) and (e18 <= e19) and (e18 <= e20) and (e18 <= e21) and (e18 <= e22) and (e18 <= e23) and (e18 <= e24) and (e18 <= e25) and (e18 <= e26) and (e18 <= e27) and (e18 <= e28) and (e18 <= e29) and (e18 <= e30)):
        c18.append(new)
    elif ((e19 <= e2) and (e19 <= e1) and (e19 <= e3) and (e19 <= e4) and (e19 <= e5) and (e19 <= e6) and (e19 <= e7) and (e19 <= e8) and (e19 <= e10) and (e19 <= e11) and (e19 <= e12) and (e19 <= e13) and (e19 <= e14) and (e19 <= e15) and (e19 <= e16) and (e19 <= e17) and (e19 <= e18) and (e19 <= e18) and (e19 <= e20) and (e19 <= e21) and (e19 <= e22) and (e19 <= e23) and (e19 <= e24) and (e19 <= e25) and (e19 <= e26) and (e19 <= e27) and (e19 <= e28) and (e19 <= e29) and (e19 <= e30)):
        c19.append(new)
    elif ((e20 <= e2) and (e20 <= e1) and (e20 <= e3) and (e20 <= e4) and (e20 <= e5) and (e20 <= e6) and (e20 <= e7) and (e20 <= e8) and (e20 <= e9) and (e20 <= e11) and (e20 <= e12) and (e20 <= e13) and (e20 <= e14) and (e20 <= e15) and (e20 <= e16) and (e20 <= e17) and (e20 <= e18) and (e20 <= e19) and (e20 <= e19) and (e20 <= e21) and (e20 <= e22) and (e10 <= e23) and (e20 <= e24) and (e20 <= e25) and (e20 <= e26) and (e20 <= e27) and (e20 <= e28) and (e20 <= e29) and (e20 <= e30)):
        c20.append(new)
    elif ((e21 <= e2) and (e21 <= e3) and (e21 <= e4) and (e21 <= e5) and (e21 <= e6) and (e21 <= e7) and (e21 <= e8) and (e21 <= e9) and (e21 <= e10) and (e21 <= e11) and (e21 <= e12) and (e21 <= e13) and (e21 <= e14) and (e21 <= e15) and (e21 <= e16) and (e21 <= e17) and (e21 <= e18) and (e21 <= e19) and (e21 <= e20) and (e21 <= e20) and (e21 <= e22) and (e21 <= e23) and (e21 <= e24) and (e21 <= e25) and (e21 <= e26) and (e1 <= e27) and (e1 <= e28) and (e21 <= e29) and (e21 <= e30)):
        c21.append(new)
    elif ((e22 <= e1) and (e22 <= e3) and (e22 <= e4) and (e22 <= e5) and (e22 <= e6) and (e22 <= e7) and (e22 <= e8) and (e22 <= e9) and (e22 <= e10) and (e22 <= e11) and (e22 <= e12) and (e22 <= e13) and (e22 <= e14) and (e22 <= e15) and (e22 <= e16) and (e22 <= e17) and (e22 <= e18) and (e22 <= e19) and (e22 <= e20) and (e22 <= e21) and (e22 <= e21) and (e22 <= e23) and (e22 <= e24) and (e22 <= e25) and (e22 <= e26) and (e22 <= e27) and (e22 <= e28) and (e22 <= e29) and (e22 <= e30)):
        c22.append(new)
    elif ((e23 <= e2) and (e23 <= e1) and (e23 <= e4) and (e23 <= e5) and (e23 <= e6) and (e23 <= e7) and (e23 <= e8) and (e23 <= e9) and (e23 <= e10) and (e23 <= e11) and (e23 <= e12) and (e23 <= e13) and (e23 <= e14) and (e23 <= e15) and (e23 <= e16) and (e23 <= e17) and (e23 <= e18) and (e23 <= e19) and (e23 <= e20) and (e23 <= e21) and (e23 <= e22) and (e23 <= e22) and (e23 <= e24) and (e23 <= e25) and (e23 <= e26) and (e23 <= e27) and (e23 <= e28) and (e23 <= e29) and (e23 <= e30)):
        c23.append(new)
    elif ((e24 <= e2) and (e24 <= e1) and (e24 <= e3) and (e24 <= e5) and (e24 <= e6) and (e24 <= e7) and (e24 <= e8) and (e24 <= e9) and (e24 <= e10) and (e24 <= e11) and (e24 <= e12) and (e24 <= e13) and (e24 <= e14) and (e24 <= e15) and (e24 <= e16) and (e24 <= e17) and (e24 <= e18) and (e24 <= e19) and (e24 <= e20) and (e24 <= e21) and (e24 <= e22) and (e24 <= e23) and (e24 <= e23) and (e24 <= e25) and (e24 <= e26) and (e24 <= e27) and (e24 <= e28) and (e24 <= e29) and (e24 <= e30)):
        c24.append(new)
    elif ((e25 <= e2) and (e25 <= e1) and (e25 <= e3) and (e25 <= e4) and (e25 <= e6) and (e25 <= e7) and (e25 <= e8) and (e25 <= e9) and (e25 <= e10) and (e25 <= e11) and (e25 <= e12) and (e25 <= e13) and (e25 <= e14) and (e25 <= e15) and (e25 <= e16) and (e25 <= e17) and (e25 <= e18) and (e25 <= e19) and (e25 <= e20) and (e25 <= e21) and (e25 <= e22) and (e25 <= e23) and (e25 <= e24) and (e25 <= e24) and (e25 <= e26) and (e25 <= e27) and (e25 <= e28) and (e25 <= e29) and (e25 <= e30)):
        c25.append(new)
    elif ((e26 <= e2) and (e26 <= e1) and (e26 <= e3) and (e26 <= e4) and (e26 <= e5) and (e26 <= e7) and (e26 <= e8) and (e26 <= e9) and (e26 <= e10) and (e26 <= e11) and (e26 <= e12) and (e26 <= e13) and (e26 <= e14) and (e26 <= e15) and (e26 <= e16) and (e26 <= e17) and (e26 <= e18) and (e26 <= e19) and (e26 <= e20) and (e26 <= e21) and (e26 <= e22) and (e26 <= e23) and (e26 <= e24) and (e26 <= e25) and (e26 <= e25) and (e26 <= e27) and (e26 <= e28) and (e26 <= e29) and (e26 <= e30)):
        c26.append(new)
    elif ((e27 <= e2) and (e27 <= e1) and (e27 <= e3) and (e27 <= e4) and (e27 <= e5) and (e27 <= e6) and (e27 <= e8) and (e27 <= e9) and (e27 <= e10) and (e27 <= e11) and (e27 <= e12) and (e27 <= e13) and (e27 <= e14) and (e27 <= e15) and (e27 <= e16) and (e27 <= e17) and (e27 <= e18) and (e27 <= e19) and (e27 <= e20) and (e27 <= e21) and (e27 <= e22) and (e27 <= e23) and (e27 <= e24) and (e27 <= e25) and (e27 <= e26) and (e27 <= e26) and (e27 <= e28) and (e27 <= e29) and (e27 <= e30)):
        c27.append(new)
    elif ((e28 <= e2) and (e28 <= e1) and (e28 <= e3) and (e28 <= e4) and (e28 <= e5) and (e28 <= e6) and (e28 <= e7) and (e28 <= e9) and (e28 <= e10) and (e28 <= e11) and (e28 <= e12) and (e28 <= e13) and (e28 <= e14) and (e28 <= e15) and (e28 <= e16) and (e28 <= e17) and (e28 <= e18) and (e28 <= e19) and (e28 <= e20) and (e28 <= e21) and (e28 <= e22) and (e28 <= e23) and (e28 <= e24) and (e28 <= e25) and (e28 <= e26) and (e28 <= e27) and (e28 <= e27) and (e28 <= e29) and (e28 <= e30)):
        c28.append(new)
    elif ((e29 <= e2) and (e29 <= e1) and (e29 <= e3) and (e29 <= e4) and (e29 <= e5) and (e29 <= e6) and (e29 <= e7) and (e29 <= e8) and (e29 <= e10) and (e29 <= e11) and (e29 <= e12) and (e29 <= e13) and (e29 <= e14) and (e29 <= e15) and (e29 <= e16) and (e29 <= e17) and (e29 <= e18) and (e29 <= e19) and (e29 <= e20) and (e29 <= e21) and (e29 <= e22) and (e29 <= e23) and (e29 <= e24) and (e29 <= e25) and (e29 <= e26) and (e29 <= e27) and (e29 <= e28) and (e29 <= e28) and (e29 <= e30)):
        c29.append(new)
    elif ((e30 <= e2) and (e30 <= e1) and (e30 <= e3) and (e30 <= e4) and (e30 <= e5) and (e30 <= e6) and (e30 <= e7) and (e30 <= e8) and (e30 <= e9) and (e30 <= e11) and (e30 <= e12) and (e30 <= e13) and (e30 <= e14) and (e30 <= e15) and (e30 <= e16) and (e30 <= e17) and (e30 <= e18) and (e30 <= e19) and (e30 <= e20) and (e30 <= e21) and (e30 <= e22) and (e30 <= e23) and (e30 <= e24) and (e30 <= e25) and (e30 <= e26) and (e30 <= e27) and (e30 <= e28) and (e30 <= e29) and (e30 <= e29)):
        c30.append(new)
    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30

def clusterALL(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, item):
    for things in item:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30 = cluster(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, things)
    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30

def putback(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30, item):
    item.append(h1)
    item.append(h2)
    item.append(h3)
    item.append(h4)
    item.append(h5)
    item.append(h6)
    item.append(h7)
    item.append(h8)
    item.append(h9)
    item.append(h10)
    item.append(h11)
    item.append(h12)
    item.append(h13)
    item.append(h14)
    item.append(h15)
    item.append(h16)
    item.append(h17)
    item.append(h18)
    item.append(h19)
    item.append(h20)
    item.append(h21)
    item.append(h22)
    item.append(h23)
    item.append(h24)
    item.append(h25)
    item.append(h26)
    item.append(h27)
    item.append(h28)
    item.append(h29)
    item.append(h30)
    return item

def check(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, item):
    if item in c1:
        c1.remove(item)
    elif item in c2:
        c2.remove(item)
    elif item in c3:
        c3.remove(item)
    elif item in c4:
        c4.remove(item)
    elif item in c5:
        c5.remove(item)
    elif item in c6:
        c6.remove(item)
    elif item in c7:
        c7.remove(item)
    elif item in c8:
        c8.remove(item)
    elif item in c9:
        c9.remove(item)
    elif item in c10:
        c10.remove(item)
    elif item in c11:
        c11.remove(item)
    elif item in c12:
        c12.remove(item)
    elif item in c13:
        c13.remove(item)
    elif item in c14:
        c14.remove(item)
    elif item in c15:
        c15.remove(item)
    elif item in c16:
        c16.remove(item)
    elif item in c17:
        c17.remove(item)
    elif item in c18:
        c18.remove(item)
    elif item in c19:
        c19.remove(item)
    elif item in c20:
        c20.remove(item)
    elif item in c21:
        c21.remove(item)
    elif item in c22:
        c22.remove(item)
    elif item in c23:
        c23.remove(item)
    elif item in c24:
        c24.remove(item)
    elif item in c25:
        c25.remove(item)
    elif item in c26:
        c26.remove(item)
    elif item in c27:
        c27.remove(item)
    elif item in c28:
        c28.remove(item)
    elif item in c29:
        c29.remove(item)
    elif item in c30:
        c30.remove(item)
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30 = cluster(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, item)
    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30

def checkALL(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, item):
    for things in item:
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30 = check(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, things)
    return cc1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30

def Ksearch(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, item):
    if item in c1:
       print("c1")
    if item in c2:
       print("c2")
    if item in c3:
       print("c3")
    if item in c4:
       print("c4")
    if item in c5:
       print("c5")
    if item in c6:
       print("c6")
    if item in c7:
       print("c7")
    if item in c8:
       print("c8")
    if item in c9:
       print("c9")
    if item in c10:
       print("c10")
    if item in c11:
       print("c11")
    if item in c12:
       print("c12")
    if item in c13:
       print("c13")
    if item in c14:
       print("c14")
    if item in c15:
       print("c15")
    if item in c16:
       print("c16")
    if item in c17:
       print("c17")
    if item in c18:
       print("c18")
    if item in c19:
       print("c19")
    if item in c20:
       print("c20")
    if item in c21:
       print("c21")
    if item in c22:
       print("c22")
    if item in c23:
       print("c23")
    if item in c24:
       print("c24")
    if item in c25:
       print("c25")
    if item in c26:
       print("c26")
    if item in c27:
       print("c27")
    if item in c28:
       print("c28")
    if item in c29:
       print("c29")
    if item in c30:
       print("c30")
        
    
#Run Code
init()
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30 = makecenters(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30)
c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30 = clusterALL(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, planets)
planets = putback(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30, planets)
#c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30 = checkALL(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, planets)
Ksearch(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, planets[3667])
    
#len(planets)
#len(c1) + len(c2) + len(c3) + len(c4)
#s1 = updatecenter(c1)
#s2 = updatecenter(c2)
#s3 = updatecenter(c3)
#s4 = updatecenter(c4)
#e1 = euclid(s1)
#e2 = euclid(s2)
#e3 = euclid(s3)
#e4 = euclid(s4)





