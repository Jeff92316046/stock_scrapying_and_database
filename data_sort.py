import scrapying

data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
def sort_data():
    i = 0
    for P in scrapying.people:
        i += 1
        data[i%15].append(P)