#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from datetime import datetime
import pandas as pd


# In[2]:


def populate(grid, start_date, end_date, labor_days):

    assert end_date > start_date, f'start date {start_date} is less than or equal to end date {end_date}'
    
    start_offset_days = (start_date - datetime(2019,1,1)).days
    end_offset_days = (end_date - datetime(2019,1,1)).days
    
    days_in_period = end_offset_days - start_offset_days
    
    assert labor_days <= days_in_period, (f'start date {start_date}, end date {end_date}:'
                                          f'the number of labor days {labor_days}'
                                          ' is greater than or equal to '
                                          f'the number of actual days in period {days_in_period}')
    
    avg_time_spent = labor_days/days_in_period
    
    grid[start_offset_days: end_offset_days] += avg_time_spent
    
    if (grid[grid > 1]).size > 0:
        raise OverflowError(f'Problem: adding date range {start_date} to {end_date} results in max daily work being exceeded')


# In[3]:


def check_member(df, team_member):
    print(f'Checking member {team_member}..')
    if df[team_member].isnull().values.any():
        print(f'Found a nan value for row {df[df[team_member].isnull()]}')
    grid = np.zeros(3500)
    for index, row in df.iterrows():
        start_date = datetime.strptime(row['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(row['Finish'], '%Y-%m-%d')
        labor_days = row[team_member]
        print(f'Checking {start_date} to {end_date}')
        populate(grid, start_date, end_date, labor_days)
    print('OK')


# In[7]:


df = pd.read_csv('drp-plan.csv', skipinitialspace=True, quotechar='"' ).applymap(lambda x: x.strip() if type(x)==str else x)


# In[8]:


df


# In[9]:


for member in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Mineo']:
    check_member(df, member)


# In[ ]:





# In[ ]:




