#!/usr/bin/env python
# coding: utf-8

import pandas as pd

def process_resources(row):
    resources = ""
    for name in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Hamano', 'PU-2']:
        if row[name] > 0:
            resources += f'{name}:{row[name]}, '
    return resources[:-2]


# Load in CSV
# Last row is usually plotted first, so reverse that.
df0 = pd.read_csv('drp-plan.csv', skipinitialspace=True,  quotechar='"').applymap(lambda x: x.strip() if type(x)==str else x)

df1 = df0[['Task', 'Start', 'Finish', 'Category', 'Description', 'Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita', 'Hamano', 'PU-2']].copy()

# Remove Project and Hardware tasks

hp_indices = df1[(df1['Category']=='Hardware') | (df1['Category']=='Project')].index
df2 = df1.drop(hp_indices)

for index, row in df2.iterrows():
    df2.at[index, 'Resource'] = process_resources(row)

df3 = df2[['Task', 'Start', 'Finish', 'Description', 'Resource']].copy()

with open("doc/table.tex", "w") as text_file:
    text_file.write(df3.to_latex(index=False, longtable=True, column_format='p{2cm}llp{2cm}l'))


