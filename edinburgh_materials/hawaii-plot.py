# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:03:36 2019

@author: ahall
"""

import pandas as pd
from matplotlib import pyplot as plt
import datetime


names=['year',
       'month',
       'decimal date',
       'average',
       'interpolated',
       'trend',
       'num days']

df = pd.read_csv('co2_mm_mlo.txt', 
                 comment='#', 
                 sep="\s+", 
                 header=None, 
                 index_col=1, 
                 names=names, 
                 na_values=[-99.99, -1], 
                 parse_dates={'date':[0, 1]}
                 )

fig=plt.figure()
plt.plot(df['date'],df['average'],color='r')
plt.plot(df['date'],df['trend'],color='k')

plt.xlabel('YEAR')
plt.ylabel('PARTS PER MILLION')
plt.grid(b=True, which='major', axis='both')
plt.text(datetime.date(1958,1,1), 400, 'Scripps Institution of Oceanography\nNOAA Earth System Research Laboratory')

fig.suptitle(r'Atmospheric $CO_2$ at Mauna Loa Observatory')


fig.savefig('hawaii_plot.png')