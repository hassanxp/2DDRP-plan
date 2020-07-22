#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Load in CSV
# Last row is usually plotted first, so reverse that.
df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x).iloc[::-1]

df_report = df[['Task', 'Start', 'Finish', 'Category']].copy()

with open("doc/table.tex", "w") as text_file:
    text_file.write(df.to_latex(index=False))


