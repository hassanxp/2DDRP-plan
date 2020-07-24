#!/usr/bin/env python
# coding: utf-8

# In[121]:


import numpy as np
from datetime import datetime
import pandas as pd


# In[155]:


def populate(grid, start_date, end_date, labor_days):
    
    start_offset_days = (start_date - datetime(2019,1,1)).days
    end_offset_days = (end_date - datetime(2019,1,1)).days
    
    days_in_period = end_offset_days - start_offset_days
    
    assert end_date > start_date
    assert labor_days <= days_in_period
    
    avg_time_spent = labor_days/days_in_period
    
    grid[start_offset_days: end_offset_days] += avg_time_spent
    
    if (grid[grid > 1]).size > 0:
        raise OverflowError(f'Problem: adding date range {start_date} to {end_date} results in max daily work being exceeded')


# In[156]:


grid = np.zeros(2000)


# In[157]:


populate(grid, datetime(2020,1,4), datetime(2020,1,5), 1)


# In[158]:


populate(grid, datetime(2020,1,4), datetime(2020,1,5), 1)


# In[171]:


df = pd.read_csv('drp-plan.csv', skipinitialspace=True, quotechar='"' ).applymap(lambda x: x.strip() if type(x)==str else x)


# In[172]:


df


# In[173]:


grid_price = np.zeros(2000)


# In[174]:


def check_member(df, team_member):
    print(f'Checking member {team_member}..')
    grid = np.zeros(3500)
    for index, row in df.iterrows():
        start_date = datetime.strptime(row['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(row['Finish'], '%Y-%m-%d')
        labor_days = row[team_member]
        print(f'Checking {start_date} to {end_date}')
        populate(grid, start_date, end_date, labor_days)
    print('OK')


# In[175]:


check_member(df, 'Price')


# In[176]:


for member in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Mineo']:
    check_member(df, member)


# In[177]:


check_member(df, 'Caplar')


# In[178]:


df[df['Caplar'] > 0]


# In[ ]:




