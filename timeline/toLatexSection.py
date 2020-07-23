import pandas as pd

def process_resources(row):
    resources = ""
    for name in ['Price', 'Caplar', 'Belland', 'Yasuda', 'Yabe', 'Yamashita']:
        if row[name] > 0:
            resources += f'{name} : {row[name]}, '
    return resources[:-2]


# Load in CSV
df0 = pd.read_csv('drp-plan.csv', skipinitialspace=True, quotechar='"' ).applymap(lambda x: x.strip() if type(x)==str else x)

# Remove Project and Hardware tasks

hp_indices = df0[(df0['Category']=='Hardware') | (df0['Category']=='Project')].index
df = df0.drop(hp_indices)

with open("doc/tasks.tex", "w") as tf:

    tf.write('\section{Tasks}')

    for index, row in df.iterrows():
        tf.write(f'\subsection{{{row["Task"]}}}\n\n')
        tf.write(f'{row["Description"]}\n\n')
        tf.write(f'Period: {row["Start"]} - {row["Finish"]}\n\n')
        tf.write(f'Resources: {process_resources(row)}\n\n')


