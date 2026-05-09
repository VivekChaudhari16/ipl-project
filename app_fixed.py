import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

st.set_page_config(page_title="IPL Dashboard", page_icon="🏏", layout="wide")

st.title("🏏 IPL Data Analysis Dashboard")
st.write("2015-2022 seasons | 8 teams | 224 matches")

df = pd.read_csv("ipl_matches.csv")

# Metric cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Matches", len(df))
col2.metric("Seasons", df["season"].nunique())
col3.metric("Teams", df["team1"].nunique())
col4.metric("Top Team", df["winner"].value_counts().index[0])

st.divider()

# ============================================
# SEASON WISE WINNER TROPHY
# ============================================
st.subheader("🏆 Season Wise Champions")

season_winners = df.groupby("season")["winner"].agg(
    lambda x: x.value_counts().index[0]
).reset_index()
season_winners.columns = ["season", "champion"]

team_colors = {
    "Mumbai Indians": "#004BA0",
    "Chennai Super Kings": "#FFFF00",
    "Royal Challengers Bangalore": "#EC1C24",
    "Kolkata Knight Riders": "#3A225D",
    "Delhi Capitals": "#0078BC",
    "Rajasthan Royals": "#EA1A85",
    "Sunrisers Hyderabad": "#F7A721",
    "Punjab Kings": "#ED1B24"
}

cols = st.columns(len(season_winners))
for i, row in season_winners.iterrows():
    color = team_colors.get(row["champion"], "#333333")
    with cols[i]:
        st.markdown(f"""
        <div style="background-color:{color}; padding:12px; border-radius:10px; text-align:center; color:white;">
            <div style="font-size:28px;">🏆</div>
            <div style="font-size:13px; font-weight:bold;">{row['season']}</div>
            <div style="font-size:11px; margin-top:4px;">{row['champion']}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Graph 1 - Team wins
st.subheader("Most Wins by Team")
fig, ax = plt.subplots(figsize=(10, 4))
wins = df["winner"].value_counts()
wins.plot(kind="bar", ax=ax, color=["#2196F3","#FF9800","#E91E63","#4CAF50","#9C27B0","#00BCD4","#FF5722","#8BC34A"])
ax.set_xlabel("Team")
ax.set_ylabel("Wins")
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 2 - Toss decision
st.subheader("Toss Decision")
fig, ax = plt.subplots(figsize=(6, 4))
toss = df["toss_decision"].value_counts()
ax.pie(toss, labels=["Field First","Bat First"], autopct="%1.1f%%",
       colors=["#2196F3","#FF9800"], startangle=90)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 3 - Season matches
st.subheader("Matches Per Season")
fig, ax = plt.subplots(figsize=(10, 3))
season_matches = df.groupby("season").size()
ax.plot(season_matches.index, season_matches.values, marker="o", color="#4CAF50", linewidth=2, markersize=8)
ax.fill_between(season_matches.index, season_matches.values, alpha=0.2, color="#4CAF50")
ax.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 4 - Top players
st.subheader("Top 10 Player of the Match")
fig, ax = plt.subplots(figsize=(10, 4))
mom = df["player_of_match"].value_counts().head(10)
ax.barh(mom.index, mom.values, color="#9C27B0")
ax.set_xlabel("Awards")
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Raw data
if st.checkbox("Raw data बघायची आहे?"):
    st.dataframe(df)
