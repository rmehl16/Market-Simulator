import math
import sys
import random
import numpy as np
from numpy.core import numeric
from numpy.core.arrayprint import _get_format_function
import matplotlib.pyplot as plt

"""
Contains industry name, growth factor type
"""
class Industry:
    def __init__(self, industry_id, gf_type, n):
        self.id=industry_id
        self.gf_type=gf_type
        #self.gf_series=self.__generate_gf_series(n)

    """
    Create global variables for these
    """
    def __generate_gf_series(self, n):
        if self.gf_type == 'RANDOM':
            return 
        
        elif self.gf_type == 'UNIFORM':
            return random.uniform(0.9999, 1.0001)

        elif self.gf_type == 'CYCLICAL':
            return


"""
Overall growth factor
"""
class Stock:
    def __init__(self, stock_id, industry_id):
        self.stock_id=stock_id
        self.industry_id=industry_id


"""
Maps stocks to price timeseries
"""
class MarketData:
    def __init__(self):
        self.timeseries_map=None
        self.day_ct=None
        self.industries=None
    
    def print_timeseries(self, max_output=sys.maxsize):
        num_recs = 0
        for stock in self.timeseries_map:
            if num_recs >= max_output:
                return
            print("{}:".format(stock.stock_id), self.timeseries_map[stock])
            num_recs += 1

    def plot_timeseries(self, max_output=sys.maxsize):
        num_lines=0
        for stock in self.timeseries_map:
            if num_lines >= max_output:
                break
            y = self.timeseries_map[stock]
            x = np.arange(y.size)
            plt.plot(x,y)
            num_lines += 1
        plt.show()
    

    """
    Initializes stocks, industries, and None object for timeseries
    """
    def initialize(self, num_days=250, num_industries=25, industry_sizes=None, industry_gfs=None):
        if (industry_sizes is None) or (len(industry_sizes) < 25):
            industry_sizes=np.ones(num_industries) * 20
            
        self.industries = []
        self.timeseries_map = {}
        stock_id = 0
        for i in range(num_industries):
            self.industries.append(Industry(i, 'UNIFORM', num_days)) # Change from hard code to optional parameter

            for j in range(int(industry_sizes[i])):
                self.timeseries_map[Stock(stock_id, i)] = None
                stock_id += 1

        
        # m x 1 array of open prices
        #open_prices = np.random.randint(5, high=500, size=num_days)

        for stock in self.timeseries_map:

            # n x 1 array of percentage gains/losses
            factors = np.random.normal(loc=1.0001, scale=0.005, size=(num_days))

            # n x 1 matrix of industry gfs
            #industry_factors = stock.industry_id
            
        # final factors is element wise multiplication of random factors and industry factors


            # final multiplication will be written manually since each entry depends on previous number
            ts = np.zeros(num_days)
            ts[0] = np.random.randint(25, high=100)
            for i in range(1, num_days):
                #print(ts[i-1] * factors[i])
                ts[i] = ts[i-1] * factors[i]

            self.timeseries_map[stock] = ts



# Start of execution
if __name__ == "__main__":
    print('Starting main')

    data = MarketData()

    data.initialize()

    #data.print_timeseries(20)

    data.plot_timeseries(25)
        
        

