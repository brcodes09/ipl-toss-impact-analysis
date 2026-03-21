import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df1 = pd.read_csv("de8ur8ru.csv")
df2 = pd.read_csv("IPL_2008-2024.csv")
df3 = pd.read_csv("team_performance_dataset_2008to2024.csv")
df4 = pd.read_csv("ipl_teams_2024_info.csv")
df5 = pd.read_csv("Players_Info_2024.csv")
#check winning probablity 
# 2. DATA CLEANING: Unify Team Names
team_renames = {
    'Delhi Daredevils': 'Delhi Capitals',
    'Kings XI Punjab': 'Punjab Kings',
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
    'Rising Pune Supergiants': 'Rising Pune Supergiant'
}
for col in ['team1', 'team2', 'toss_winner', 'winner']:
    df2[col] = df2[col].replace(team_renames)

# Drop matches with no result (abandoned)
df = df2.dropna(subset=['winner'])

# 3. CORE LOGIC: Does Toss Winner = Match Winner?
df['toss_match_winner'] = (df['toss_winner'] == df['winner'])

# 4. VISUALIZATION 1: Overall Percentage Chart (Pie Chart)
plt.figure(figsize=(8, 6))
toss_win_counts = df['toss_match_winner'].value_counts()
plt.pie(toss_win_counts, labels=['Toss Winner Lost', 'Toss Winner Won'], 
        autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('IPL Overall Toss-Match Win Probability (2008-2024)')
plt.savefig('toss_pie_chart.png')

# 5. VISUALIZATION 2: Batting vs Fielding (Bar Chart)
plt.figure(figsize=(8, 6))
sns.barplot(x='toss_decision', y='toss_match_winner', data=df, palette='viridis')
plt.axhline(0.5, color='red', linestyle='--', label='50% Neutral Line')
plt.title('Win %: Choosing to Bat vs Field')
plt.ylabel('Win Probability')
plt.savefig('decision_success.png')

# 6. VISUALIZATION 3: Venue Advantage (Heatmap)
# Selecting top 15 venues with most matches
top_venues = df['venue'].value_counts().nlargest(15).index
venue_df = df[df['venue'].isin(top_venues)]

venue_pivot = venue_df.pivot_table(index='venue', columns='toss_decision', 
                                   values='toss_match_winner', aggfunc='mean') * 100

plt.figure(figsize=(12, 8))
sns.heatmap(venue_pivot, annot=True, cmap='RdYlGn', fmt=".1f")
plt.title('Venue-wise Toss Advantage (%)')
plt.savefig('venue_heatmap.png')
plt.show()

#2.
