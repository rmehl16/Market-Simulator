import math
import random
import numpy as np

"""
Contains industry name, growth factor
"""
class Industry:
    def __init__(self, industry_id, gf):
        self.id=industry_id
        self.gf=gf

"""
Overall growth factor
"""
class Stock:
    def __init__(self, stock_id, industry_id):
        self.sotck_id=stock_id
        self.industry_id=industry_id


"""
Maps stocks to price timeseries
"""
class MarketData:
    def __init__(self):
        self.timeseries_df=None
        self.day_ct=None
        self.industries=None
    
    def initialize(self, num_industries, industry_sizes=None):
        self.industries = []
        for i in range(num_industries):
            self.industries.append(Industry(i, random.uniform(1.0001, 1.0004)))


        if industry_sizes is None:
            industry_sizes=np.ones(num_industries) * 10
        
        

