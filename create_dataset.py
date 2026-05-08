import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

teams = [
    "Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore",
    "Kolkata Knight Riders", "Delhi Capitals", "Rajasthan Royals",
    "Sunrisers Hyderabad", "Punjab Kings"
]

venues = [
    "Wankhede Stadium", "M.A. Chidambaram Stadium", "Eden Gardens",
    "Arun Jaitley Stadium", "Sawai Mansingh Stadium", "Rajiv Gandhi Stadium"
]

players = {
    "Mumbai Indians": ["Rohit Sharma", "Suryakumar Yadav", "Jasprit Bumrah", "Hardik Pandya", "Kieron Pollard"],
    "Chennai Super Kings": ["MS Dhoni", "Ruturaj Gaikwad", "Ravindra Jadeja", "Deepak Chahar", "Faf du Plessis"],
    "Royal Challengers Bangalore": ["Virat Kohli", "Glenn Maxwell", "Mohammed Siraj", "Dinesh Karthik", "Harshal Patel"],
    "Kolkata Knight Riders": ["Shreyas Iyer", "Andre Russell", "Sunil Narine", "Pat Cummins", "Venkatesh Iyer"],
    "Delhi Capitals": ["Rishabh Pant", "David Warner", "Axar Patel", "Anrich Nortje", "Prithvi Shaw"],
    "Rajasthan Royals": ["Sanju Samson", "Jos Buttler", "Yuzvendra Chahal", "Trent Boult", "Shimron Hetmyer"],
    "Sunrisers Hyderabad": ["Kane Williamson", "Rashid Khan", "Bhuvneshwar Kumar", "Nicholas Pooran", "Washington Sundar"],
    "Punjab Kings": ["Shikhar Dhawan", "Liam Livingstone", "Kagiso Rabada", "Mayank Agarwal", "Arshdeep Singh"]
}

matches = []
match_id = 1

for season in range(2015, 2023):
    team_list = teams.copy()
    for i in range(len(team_list)):
        for j in range(i+1, len(team_list)):
            team1 = team_list[i]
            team2 = team_list[j]
            
            toss_winner = random.choice([team1, team2])
            toss_decision = random.choice(["bat", "field"])
            
            if toss_decision == "bat":
                batting_first = toss_winner
                batting_second = team2 if toss_winner == team1 else team1
            else:
                batting_second = toss_winner
                batting_first = team2 if toss_winner == team1 else team1
            
            score1 = random.randint(130, 220)
            score2 = random.randint(120, 215)
            
            if score1 > score2:
                winner = batting_first
                win_by_runs = score1 - score2
                win_by_wickets = 0
            else:
                winner = batting_second
                win_by_runs = 0
                win_by_wickets = random.randint(1, 9)
            
            mom = random.choice(players[winner])
            venue = random.choice(venues)
            
            matches.append({
                "match_id": match_id,
                "season": season,
                "team1": team1,
                "team2": team2,
                "venue": venue,
                "toss_winner": toss_winner,
                "toss_decision": toss_decision,
                "winner": winner,
                "win_by_runs": win_by_runs,
                "win_by_wickets": win_by_wickets,
                "player_of_match": mom
            })
            match_id += 1

df = pd.DataFrame(matches)
df.to_csv("ipl_matches.csv", index=False)
print(f"Dataset ready! Total matches: {len(df)}")
print(df.head())
print(f"\nSeasons: {df['season'].unique()}")
print(f"Teams: {df['team1'].nunique()}")
