#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from datetime import datetime
from datetime import timedelta
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# In[2]:


GRID_N_DAYS = 3500
BASE_DATE = datetime(2019,1,1)


# In[3]:


def populate(grid, start_date, end_date, labor_days):

    assert end_date > start_date, f'start date {start_date} is less than or equal to end date {end_date}'
    
    start_offset_days = (start_date - BASE_DATE).days
    end_offset_days = (end_date - BASE_DATE).days
    
    days_in_period = end_offset_days - start_offset_days
    
    assert labor_days <= days_in_period, (f'start date {start_date}, end date {end_date}:'
                                          f'the number of labor days {labor_days}'
                                          ' is greater than or equal to '
                                          f'the number of actual days in period {days_in_period}')
    
    avg_time_spent = labor_days/days_in_period
    
    grid[start_offset_days: end_offset_days] += avg_time_spent
    
    delta_grid = np.zeros(GRID_N_DAYS)
    delta_grid[start_offset_days: end_offset_days] += avg_time_spent
    
    if (grid[grid > 1]).size > 0:
        print(f'PROBLEM: adding date range {start_date} to {end_date} results in max daily work being exceeded')
        return (False, delta_grid)
    else:
        return (True, delta_grid)


# In[4]:


def check_member(df, team_member):
    print(f'Checking member {team_member}..')
    if df[team_member].isnull().values.any():
        print(f'Found a nan value for row {df[df[team_member].isnull()]}')
    grid = np.zeros(GRID_N_DAYS)
    all_ok = True
    delta_list = []
    for index, row in df.iterrows():
        start_date = datetime.strptime(row['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(row['Finish'], '%Y-%m-%d')
        labor_days = row[team_member]
        #print(f'Checking {start_date} to {end_date} and days {labor_days}')
        result, delta = populate(grid, start_date, end_date, labor_days)
        delta_list.append(delta)
        if not result:
            all_ok = False
    if all_ok:
        print(f'OK for member {team_member}')
    else:
        print(f'PROBLEMS found for member {team_member}')
    return grid, delta_list


# In[5]:


def plot_loading(grid, delta_list):
    date_list = [BASE_DATE + timedelta(days=i) for i in range(GRID_N_DAYS)]
    dates = matplotlib.dates.date2num(date_list)

    xrange = matplotlib.dates.date2num([datetime(2020,1,1), datetime(2022,1,1)])
    plt.figure(figsize=(20,10))
    for counter, delta in enumerate(delta_list):
        plt.plot_date(dates, delta.tolist(), label=df['Task'][counter])
    plt.plot_date(dates, grid.tolist(), label='Total')
    plt.legend(loc="upper left")
    plt.xlim(xrange[0], xrange[1])

    


# In[24]:


df = pd.read_csv('drp-plan.csv', skipinitialspace=True, quotechar='"' ).applymap(lambda x: x.strip() if type(x)==str else x)


# In[25]:


for member in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Mineo', 'Hamano', 'PU-2']:
    check_member(df, member)


# In[26]:


grid, delta_list = check_member(df, 'Price')


# In[27]:


plot_loading(grid, delta_list)


# In[28]:


grid[grid>1]


# In[29]:


grid, delta_list = check_member(df, 'Caplar')
plot_loading(grid, delta_list)


# In[ ]:




