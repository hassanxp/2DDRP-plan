#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.figure_factory as ff
import pandas as pd
import random


# In[2]:


random.seed(123)


# In[12]:


catColors = dict(Sky='rgb(220, 0, 0)', Project='rgb(220, 0, 0)', 
                 Hardware='rgb(220, 0, 0)', Calibration='rgb(220, 0, 0)', 
                 PsfModelling='rgb(220, 0, 0)', WavelengthCalibration='rgb(220, 0, 0)')
catColors


# In[11]:


df = pd.read_csv('drp-plan.csv')
numUniqueCategories = len(df.Category.unique())
catColors = ["#%06x" % random.randint(0, 0xFFFFFF) for i in range(numUniqueCategories)] 

fig = ff.create_gantt(df, colors=catColors, index_col='Category',
                      show_colorbar=True, bar_width=0.05, showgrid_x=True, showgrid_y=False, title="DRP Plan")
fig.update_layout(plot_bgcolor='rgba(0,0,0, 0.02)')
fig.show()


# In[ ]:




