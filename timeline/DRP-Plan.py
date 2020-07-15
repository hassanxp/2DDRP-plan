#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.figure_factory as ff
import pandas as pd
import random
import plotly.graph_objects as go


# In[2]:


catColors = dict(Project='rgb(255, 51, 0)', 
                 Hardware='rgb(230, 230, 0)', 
                 Sky='rgb(51, 153, 255)', 
                 PSF='rgb(102, 0, 255)', 
                 WavelengthCalibration='rgb(153, 102, 255)', 
                 Calibration='rgb(204, 51, 255)',
                 Infra='rgb(153, 0, 153)')


# In[6]:


df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x)

for cat in set(df['Category']):
    if cat not in catColors:
        print(f'category {cat} is not in color mapping') 

arms_full = df[df['Task'] == 'SM3(B+R+N)@LAM']['Start'].values[0]
commissioning_start = df[df['Task'] == 'Commissioning']['Start'].values[0]
commissioning_end = df[df['Task'] == 'Commissioning']['Finish'].values[0]
ssp_end = df[df['Task'] == 'Call for SSP']['Start'].values[0]

#print(f'{arms_full} {commissioning_start} {commissioning_end} {ssp_end}')

fig = ff.create_gantt(df, colors=catColors, index_col='Category',
                      show_colorbar=False, 
                      bar_width=0.1, 
                      showgrid_x=True, 
                      showgrid_y=False, 
                      title="DRP Plan")
fig.update_layout(plot_bgcolor='rgba(0,0,0, 0.1)')

for mls_yr, mls_text in {arms_full: 'R+B+N', 
                 commissioning_start: 'Comm Start', 
                 commissioning_end : 'Comm End', 
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


# In[ ]:





# In[ ]:




