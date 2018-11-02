# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:28:21 2018

@author: bretl
"""

#use +stat_smooth (method=lm) for trendline
#Question 1: data on daphnia length vs weight
import pandas as pd
import numpy as np
from plotnine import *
daphnialw=pd.read_csv("hypoxia-10815-wpreexposure - Sheet1.csv",header=1,sep=',')
#Just length vs width
e=ggplot(daphnialw, aes(x='length',y='weight'))+theme_classic()+xlab('length')+ylab('weight')
e+geom_point()+stat_smooth(method="lm")
#same plot but grouped by clone type
d=ggplot(daphnialw, aes(x='length',y='weight', color='clone'))+theme_classic()+xlab('length')+ylab('weight')
d+geom_point()+stat_smooth(method="lm")


#question 2
import pandas as pd
import numpy as np
from plotnine import *
data=pd.read_csv('data.txt', sep=',', header=0)
a=ggplot(data, aes(x='factor(region)', y='observations' ))+theme_classic()+xlab('region')+ylab('observations')
a+geom_bar(stat='summary', fun_y=np.mean)

b=ggplot(data, aes(x='region', y='observations'))+theme_classic()+xlab('region')+ylab('observations')
b+geom_point()+geom_jitter()

##question 2 discussion
#the bar plot and scatterplot tell different stories. Just looking at the barplot would imply there are no differences in the regions
#while there aren't differences in the means of the regions, the scatterplot shows there are differences in the distributions within the regions
