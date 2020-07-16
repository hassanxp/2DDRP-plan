#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.figure_factory as ff
import pandas as pd
import random
import plotly.graph_objects as go


# In[8]:


catColors = dict(Project='rgb(255, 51, 0)', 
                 Hardware='rgb(230, 230, 0)', 
                 Sky='rgb(51, 153, 255)', 
                 PSF='rgb(102, 0, 255)', 
                 WavelengthCalibration='rgb(153, 102, 255)', 
                 Calibration='rgb(204, 51, 255)',
                 Infra='rgb(153, 0, 153)')


# In[35]:


# Load in CSV
# Last row is usually plotted first, so reverse that.
df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x).iloc[::-1]

for cat in set(df['Category']):
    if cat not in catColors:
        print(f'category {cat} is not in color mapping') 

arms_full = df[df['Task'] == 'SM3(B+R+N)@LAM']['Start'].values[0]
engobs_start = df[df['Task'] == 'Start of engineering observations']['Start'].values[0]
science_ops = df[df['Task'] ==  'Science Operations']['Start'].values[0]
ssp_end = df[df['Task'] == 'Call for SSP']['Start'].values[0]

fig = ff.create_gantt(df, colors=catColors, index_col='Category',
                      show_colorbar=False, 
                      bar_width=0.1, 
                      showgrid_x=True, 
                      showgrid_y=False, 
                      title="DRP Plan",
                      height=1000)
fig.update_layout(plot_bgcolor='rgba(0,0,0, 0.1)')

for mls_yr, mls_text in {arms_full: 'R+B+N', 
                 engobs_start: 'Eng Obs Start', 
                 engobs_end : 'Eng Obs End', 
                 ssp_end : 'Call for SSP'}.items():
    fig.add_trace(
        go.Scatter(
            x = [mls_yr, mls_yr],
            y = [-1, len(df.index) + 1],
#            mode = "lines",
            mode = "lines+text",
            name = mls_text,
            textposition = "bottom center",
            line = go.scatter.Line(color = "gray", width = 1),
            showlegend = False
        )
    )

fig.show()


# In[31]:


df


# In[ ]:




