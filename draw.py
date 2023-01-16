import matplotlib.pyplot as plt
import data_sort 
import copy

data = []
def set_up_down(down,up):
    for i in range(0,51):
        data.append(data_sort.data[int(down)-1][i])

    for i in range(int(down),int(up)):
        for j in range(0,51):
            data[j] += data_sort.data[i][j]
        
def draw_pic():
    line_a, = plt.plot(range(0,51), data, '-o', label='A')
    plt.title('Stock', fontsize=16)
    plt.xlabel('week', fontsize=16)
    plt.ylabel('people', fontsize=16)
    plt.show()

def clean_data():
    data.clear()