#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
from datetime import datetime
from datetime import timedelta
import pandas as pd


# In[84]:


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
    
    delta_grid = np.zeros(3500)
    delta_grid[start_offset_days: end_offset_days] += avg_time_spent
    
    if (grid[grid > 1]).size > 0:
        print(f'PROBLEM: adding date range {start_date} to {end_date} results in max daily work being exceeded')
        return (False, delta_grid)
    else:
        return (True, delta_grid)


# In[85]:


def check_member(df, team_member):
    print(f'Checking member {team_member}..')
    if df[team_member].isnull().values.any():
        print(f'Found a nan value for row {df[df[team_member].isnull()]}')
    grid = np.zeros(3500)
    all_ok = True
    delta_list = []
    for index, row in df.iterrows():
        start_date = datetime.strptime(row['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(row['Finish'], '%Y-%m-%d')
        labor_days = row[team_member]
        print(f'Checking {start_date} to {end_date} and days {labor_days}')
        result, delta = populate(grid, start_date, end_date, labor_days)
        delta_list.append(delta)
        if not result:
            all_ok = False
    if all_ok:
        print(f'OK for member {team_member}')
    else:
        print(f'PROBLEMS found for member {team_member}')
    return grid, delta_list


# In[86]:


df = pd.read_csv('drp-plan.csv', skipinitialspace=True, quotechar='"' ).applymap(lambda x: x.strip() if type(x)==str else x)


# In[87]:


df


# In[88]:


for member in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Mineo', 'NAOJ-2']:
    check_member(df, member)


# In[91]:


grid, delta_list = check_member(df, 'Price')


# In[92]:


print(grid)


# In[90]:


print(type(grid))


# In[93]:


print(delta_list)


# In[46]:


grid.tolist()


# In[48]:


datetime(2019,1,1)+timedelta(days=1)


# In[67]:


dates = [datetime(2019,1,1)+timedelta(days=i) for i in range(3500)]


# In[68]:


dates


# In[69]:


import matplotlib


# In[72]:


date_list = dates


# In[73]:


dates = matplotlib.dates.date2num(date_list)


# In[74]:


dates


# In[75]:


matplotlib.pyplot.plot_date(dates, [i for i in range(3500)])


# In[76]:


import matplotlib.pyplot as plt


# In[79]:


plt.plot_date(dates, [i for i in range(3500)], label='a')
plt.plot_date(dates, [i-10 for i in range(3500)], label='b')
plt.plot_date(dates, [i/10 for i in range(3500)], label='c')
plt.legend(loc="upper left")


# In[78]:


len(grid.tolist())


# In[95]:


xrange = matplotlib.dates.date2num([datetime(2020,1,1), datetime(2021,1,1)])
for counter, delta in enumerate(delta_list):
    plt.plot_date(dates, delta.tolist(), label=counter)
    plt.legend(loc="upper left")
    plt.xlim(xrange[0], xrange[1])


# In[81]:





# In[ ]:




