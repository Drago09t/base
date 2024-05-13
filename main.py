

df = pd.read_csv('C:\Users\Students\Documents\ai_lab.csv')

 



mean_Goals = df['Goals'].mean()

mean_Assists = df['Assists'].mean()

mean_yellow_cards = df['Yellow cards'].mean()

 

print("mean Goals:", mean_Goals)

print("mean Assists:", mean_Assists)

print("mean Yellow cards:", mean_yellow_cards)

 


df['Goals'].fillna(mean_Goals, inplace=True)

df['Assists'].fillna(mean_Assists, inplace=True)

df['Yellow cards'].fillna(mean_yellow_cards, inplace=True)

 


new_mean_Goals = df['Goals'].mean()

new_mean_assists = df['Assists'].mean()

new_mean_yellow_cards = df['Yellow cards'].mean()

 

result = new_mean_Goals - (new_mean_assists + new_mean_yellow_cards)

print("Result:", result)

 


df.to_csv('final.csv', index=False)