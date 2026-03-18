# ipl-toss-impact-analysis
IPL Toss Impact Analysis is a data analysis project that studies how winning the toss affects match results in the Indian Premier League. Using Python, Pandas, Matplotlib, and Seaborn, the project analyzes win probability, batting vs chasing success, and venue advantages through visualizations like heatmaps and percentage charts.

thechnology used : 
Python: The core programming language.

Pandas: For data manipulation and "cleaning" the datasheet.

Matplotlib & Seaborn: For generating those heatmaps and percentage charts.

NumPy: For handling logical conditions and numerical arrays.

 | Function | Syntax | Use Case (1 Line) |
|---|---|---|---|
| Loading | `pd.read_csv('file.csv')` | Loads your IPL datasheet into a workable DataFrame. | |
| Inspection | `df.info()` | Checks for missing values and data types of columns. | |
| Cleaning | `df.dropna(subset=['winner'])` | Removes matches that ended in 'No Result' or had missing winners. | |
| Standardizing | `df.replace({'Old Name': 'New Name'})` | Merges renamed teams (e.g., Delhi Daredevils to Delhi Capitals). | |
| Manipulation | `df['toss_win_match_win'] = (df['toss_winner'] == df['winner'])` | Creates a column to see if the toss winner also won the match. | |
| Grouping | `df.groupby('venue')['toss_win_match_win'].mean()` | Calculates the win percentage for toss winners at each stadium. | |
| Counting | `df['toss_decision'].value_counts()` | Counts how many times teams chose to 'bat' vs 'field' first. | |
| Analysis | `pd.crosstab(df['venue'], df['toss_decision'])` | Creates a frequency table of decisions per venue for the heatmap. | |
| Heatmap | `sns.heatmap(data, annot=True)` | Visualizes the toss advantage across different venues. | |
| Pie Chart | `plt.pie(data, labels=labels, autopct='%1.1f%%')` | Shows the overall percentage of "Toss Win = Match Win". | |
