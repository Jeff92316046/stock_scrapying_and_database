import scrapying

def sort_data(pre_data):
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    i = 0
    for P in pre_data:
        i += 1
        data[i%15].append(P)
    return data