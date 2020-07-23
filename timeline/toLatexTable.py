#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Load in CSV
# Last row is usually plotted first, so reverse that.
df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x).iloc[::-1]

df_report0 = df[['Task', 'Start', 'Finish', 'Category', 'Description', 'Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita']].copy()

# Remove Project and Hardware tasks

hp_indices = df[(df['Category']=='Hardware') | (df['Category']=='Project')].index
df_report = df.drop(hp_indices)

with open("doc/table.tex", "w") as text_file:
    text_file.write(df_report.to_latex(index=False, longtable=True, column_format='llllp{2cm}llllll'))


