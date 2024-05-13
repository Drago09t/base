import pandas as pd

import matplotlib.pyplot as plt

 


df = pd.read_csv('football.csv')

 


plt.figure(figsize=(12, 8))

plt.plot(df['Player Name'], df['Yellow cards'], marker='o', color='orange', linestyle='-', linewidth=2)

plt.title('yellow card by players')

plt.xlabel('players')

plt.ylabel('Yellow Cards')

plt.xticks(rotation=35, ha='right')

plt.grid(True)

plt.tight_layout()

plt.show()


plt.figure(figsize=(12, 8))

plt.scatter(df['Player Name'], df['Assists'], color='green', marker='o')

plt.title('Assists by Players')

plt.xlabel('Players')

plt.ylabel('Assists')

plt.xticks(rotation=35, ha='right')

plt.grid(True)

plt.tight_layout()

plt.show()


plt.figure(figsize=(12, 8))

df_country_goals = df.groupby('Country')['Goals'].sum().reset_index()

plt.bar(df_country_goals['Country'], df_country_goals['Goals'], color='blue')

plt.title('Total Goals by Country')

plt.xlabel('Country')

plt.ylabel('Total Goals')

plt.xticks(rotation=35, ha='right')

plt.grid(axis='y')

plt.tight_layout()

plt.show()