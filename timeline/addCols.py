#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Load in CSV
# Last row is usually plotted first, so reverse that.
df = pd.read_csv('drp-plan.csv').applymap(lambda x: x.strip() if type(x)==str else x)

df['Description'] = ""
df['Resources'] = ""

with open("drp-plan-exp.csv", "w") as text_file:
    text_file.write(df.to_csv(index=False))

