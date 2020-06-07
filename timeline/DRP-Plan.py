#!/usr/bin/env python
# coding: utf-8

# In[23]:


import plotly.figure_factory as ff
import pandas as pd
import random
import plotly.graph_objects as go


# In[24]:


catColors = dict(Project='rgb(255, 51, 0)', 
                 Hardware='rgb(230, 230, 0)', 
                 Sky='rgb(51, 153, 255)', 
                 PSF='rgb(102, 0, 255)', 
                 WavelengthCalibration='rgb(153, 102, 255)', 
                 Calibration='rgb(204, 51, 255)')


# In[88]:


df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x)


# In[89]:


for cat in set(df['Category']):
    if cat not in catColors:
        print(f'category {cat} is not in color mapping') 


# In[90]:


arms_full = df[df['Task'] == 'SM3(B+R+N)@LAM']['Start'].values[0]
commissioning_start = df[df['Task'] == 'Commissioning']['Start'].values[0]
commissioning_end = df[df['Task'] == 'Commissioning']['Finish'].values[0]


# In[91]:


fig = ff.create_gantt(df, colors=catColors, index_col='Category',
                      show_colorbar=True, bar_width=0.05, showgrid_x=True, showgrid_y=False, title="DRP Plan")
fig.update_layout(plot_bgcolor='rgba(0,0,0, 0.02)')

for yr in [arms_full, commissioning_start, commissioning_end]:
    fig.add_trace(
        go.Scatter(
            x = [yr, yr],
            y = [-1, len(df.index) + 1],
            mode = "lines",
            line = go.scatter.Line(color = "gray", width = 1),
            showlegend = False
        )
    )

fig.show()


# In[ ]:




