import pandas as pd

df2 = pd.read_csv('IPL_2008-2024.csv')
print('rows', len(df2))
print('cols', df2.columns.tolist())
print(df2[['toss_winner','toss_decision','winner','win_by_runs','win_by_wickets']].head())
