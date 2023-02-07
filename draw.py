import matplotlib.pyplot as plt
from matplotlib import ticker
import copy


class drawer :
    def __init__(self) :
        self.data1 = [] #people
        self.data2 = [] #share

    def set_up_down(self,down,up,stock):
        temp_data = self.data1[0]
        
        for i in self.data1:
            k = 0 
            for j in i: 
                temp_data[k] += j
                k += 1
        self.data1.clear()
        self.data1 = copy.deepcopy(temp_data)

        temp_data_2 = self.data2[int(down)-1]
        
        for i in range(int(down),int(up)):
            k = 0 
            for j in self.data2[i]: 
                temp_data_2[k] += j
                k += 1
       
        self.data2.clear()
        self.data2 = copy.deepcopy(temp_data_2)
        self.draw_pic(stock)
        
                
    def draw_pic(self,stock):
        """
        line_a, = plt.plot(range(0,len(self.data)), self.data, '-o', label='A')
        plt.title(stock, fontsize=16)
        plt.xlabel('week', fontsize=16)
        if self.flag == 0:
            plt.ylabel('share', fontsize=16)
        elif self.flag == 1:
            plt.ylabel('people', fontsize=16)
        plt.show()
        self.data.clear()
        """
        fig, ax1 = plt.subplots()
        plt.title(stock, fontsize=16)
        plt.xlabel('week', fontsize=16)
        ax2 = ax1.twinx()
        ax1.set_ylabel('people', color='tab:blue')
        ax1.plot(range(len(self.data1)), self.data1, color='tab:blue', alpha=0.75)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x),',')))
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        ax2.set_ylabel('share', color='black')
        
        ax2.plot(range(len(self.data2)), self.data2 , color='black', alpha=1)
        ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=1))
        ax2.set_ylim(0.9*min(self.data2),1.1*max(self.data2))
        ax2.tick_params(axis='y', labelcolor='black')
        fig.tight_layout()
        plt.show()


