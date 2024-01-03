### Compute a distance for trip List[Dict] ###

def simple_distance(r1, r2):
    if len(r2) > len(r1) :
        r3 = r2
        r2 = r1
        r1 = r3
    if len(r1) == len(r2):
        dist = 0
        for i in range(len(r1)):
            dist += step_distance(r1[i],r2[i])
        return dist
    else :
        if r1 != [] :
            return min(simple_distance(r1[1:],r2[1:])+step_distance(r1[0],r2[0]),20 + simple_distance(r1,r2[1:]))
        else :
            return 20*len(r2)

def step_distance(d1,d2):
    dist = 0
    if d1["from"] != d2["from"] :
        dist += 5
    if d1["to"] != d2["to"] :
        dist += 5
    dist += merch_distance(d1["merchandise"],d2["merchandise"])
    return dist

def merch_distance(m1,m2):
    tot = 0
    present_merch = []
    m1keys = m1.keys()
    m2keys = m2.keys()
    for merch in m1keys:
        if merch not in present_merch:
            present_merch.append(merch)
    for merch in m2keys:
        if merch not in present_merch:
            present_merch.append(merch)      
    for merch in present_merch : 
        if (merch not in m1keys) or (merch not in m2keys):
            tot +=2
        elif m1[merch] == m2[merch]:
            tot +=0
        elif (m1[merch] == 0) | (m2[merch] == 0):
            tot += 2
        else :
            tot += 1
    return 10 * (tot/(2*len(present_merch)))

""" a =[
            {
                "from": "Bologna",
                "to": "Genova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":18
                }
            },
            {
                "from": "Bologna",
                "to": "Genova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":18
                }
            }
        ]
b =[
            {
                "from": "Bologna",
                "to": "Genova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":18
                }
            },
            {
                "from": "Milano",
                "to": "Padova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":18
                }
            },
            {
                "from": "Bologna",
                "to": "Genova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":17
                }
            },
            {
                "from": "Milano",
                "to": "Padova",
                "merchandise": {
                    "puzzles": 16,
                    "vodka":17
                }
            }
        ] 
print(simple_distance(a,b))"""