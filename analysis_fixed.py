import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import os

os.makedirs("graphs", exist_ok=True)

df = pd.read_csv("ipl_matches.csv")

# Graph 1 - Team wins bar chart
fig, ax = plt.subplots(figsize=(12, 5))
wins = df["winner"].value_counts()
wins.plot(kind="bar", ax=ax, color=["#2196F3","#FF9800","#E91E63","#4CAF50","#9C27B0","#00BCD4","#FF5722","#8BC34A"])
ax.set_title("Most Wins by Team (2015-2022)", fontsize=14, fontweight="bold")
ax.set_xlabel("Team")
ax.set_ylabel("Total Wins")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig("graphs/team_wins.png", dpi=150)
plt.close()

# Graph 2 - Toss decision pie chart
fig, ax = plt.subplots(figsize=(7, 5))
toss = df["toss_decision"].value_counts()
ax.pie(toss, labels=["Field First", "Bat First"], autopct="%1.1f%%",
       colors=["#2196F3", "#FF9800"], startangle=90)
ax.set_title("Toss Decision: Bat vs Field", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("graphs/toss_decision.png", dpi=150)
plt.close()

# Graph 3 - Season wise matches
fig, ax = plt.subplots(figsize=(10, 5))
season_matches = df.groupby("season").size()
ax.plot(season_matches.index, season_matches.values, marker="o", color="#4CAF50", linewidth=2, markersize=8)
ax.fill_between(season_matches.index, season_matches.values, alpha=0.2, color="#4CAF50")
ax.set_title("Matches Per Season", fontsize=14, fontweight="bold")
ax.set_xlabel("Season")
ax.set_ylabel("Number of Matches")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("graphs/season_matches.png", dpi=150)
plt.close()

# Graph 4 - Top Player of Match winners
fig, ax = plt.subplots(figsize=(10, 5))
mom = df["player_of_match"].value_counts().head(10)
ax.barh(mom.index, mom.values, color="#9C27B0")
ax.set_title("Top 10 Player of the Match Winners", fontsize=14, fontweight="bold")
ax.set_xlabel("Awards")
plt.tight_layout()
plt.savefig("graphs/top_players.png", dpi=150)
plt.close()

print("All 4 graphs saved!")
