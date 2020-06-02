userID = 0
movieID = 0
rating = 0

x = 0

#test items start here
dict1 = {'hp1' : 4, 'tw' : 5, 'sw1' : 1}
dict2 = {'hp1' : 5, 'hp2' : 5, 'hp3' : 4}
dict3 = {'tw': 2, 'sw1' : 4, 'sw2' : 5}
mylist = []
mylist.append(dict1)
mylist.append(dict2)
mylist.append(dict3)
#test stuff ends here

#data is a list of dictionaries, each dictionary is defined as {movieID : rating}
data = []
normal = []
simlist = []
matchlist = []
reccomendlist = []

#get count of total users, and make a list of dictionaries
def setData():
    file = open("ratings.csv", "r")
    for item in file:
        x = item.split(',')
        userID = x[0]
        if userID not in data:
            data.append(userID)
    x = 0
    while x < len(data):
        data[x] = {}
        x = x + 1
    file.close()

#populate each dictionary based on their movies and ratings, index of list denotes userID
def getData():
    file = open("ratings.csv", "r")
    for item in file:
        x = item.split(',')
        userID = x[0]
        movieID = x[1]
        rating = x[2]
        if (userID == 'userId'):
            userID = 0
            movieID = 0
            rating = 0.0
        else:
            userID = int(userID)
            movieID = int(movieID)
            rating = float(rating)
        data[userID][movieID] = rating
    file.close()

#create a normal list for preparation of centered cosine reccomendation
def normalizeData():
    newlist = []
    newlist = data
    for items in newlist:
        total = 0
        for values in items:
            total += items[values]
        for values in items:
            avg = len(items)
            if (avg < 1):
                avg = 1
            items[values] = items[values] - (total/avg)
    return newlist

#get the centered cosine similarity between two users
def sim(item1, item2):
    numerator = 0
    denominator = 0
    d1 = 0
    d2 = 0
    for values in item1:
        if values in item2:
            numerator += (item1[values] * item2[values])
    for values in item1:
        d1 += (item1[values]) ** 2
    for values in item2:
        d2 += (item2[values]) ** 2
    denominator = ((d1**0.5) * (d2**0.5))
    if (denominator <= 0):
        denominator = 1
    return (numerator / denominator)

#compare one user's similiarity to all other users
def getsimlist(item):
    x = 0
    while x < len(normal):
        simlist.append(sim(normal[item], normal[x]))
        x += 1
    simlist[item] = 0

#Make a list of every user and their top 5 most similiar neighboring users
def matcher():
    list = []
    y = 0
    while y < 5:
        x = (simlist.index(max(simlist)))
        simlist[x] = 0
        list.append(x)
        y += 1
    matchlist.append(list)

#execute matcher and getsimlist, refresh simlist for every user
def makematch():
    x = 0
    while x < len(normal):
        getsimlist(x)
        matcher()
        del simlist[:]
        x += 1

#find and return the highest rated movie of item2 that is not in item1
def reccomend(item1, item2):
    inverse = [(value, key) for key, value in item2.items()]
    inverse.sort()
    inverse.reverse()
    x = 0
    while x < len(inverse):
        if (inverse[x][1]) in item1:
            x += 1
        else:
            return (inverse[x][1])
    return 0

#do reccomend() for the top5 highest matches for every user
def top5(index):
    mylist = []
    for items in matchlist[index]:
        mylist.append(reccomend(data[index], data[items]))
    reccomendlist.append(mylist)

#do top5() for every user, thus getting the top 5 movie reccomendations for every user, this accomplishes the goal of the project    
def reccomendall():
    x = 0
    while x < len(matchlist):
        top5(x)
        x += 1

#Display users and their top 5 reccomendations
def printrec():
    x = 1
    while x < len(reccomendlist):
        print("User-ID",x,': ', "Movie-ID",reccomendlist[x][0],', ',"Movie-ID",reccomendlist[x][1],', ',"Movie-ID",reccomendlist[x][2],', ',"Movie-ID",reccomendlist[x][3],', ',"Movie-ID",reccomendlist[x][4], sep = '')
        x += 1
    
    
    
            

               

setData()
getData()
normal = normalizeData()
makematch()
reccomendall()
printrec()
