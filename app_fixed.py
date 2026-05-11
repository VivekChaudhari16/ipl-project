import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

st.set_page_config(page_title="IPL Dashboard", page_icon="🏏", layout="wide")

# Blue Stadium Theme CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(160deg, #0a0a2e 0%, #0d1b4b 30%, #0a2a6e 60%, #0d1b4b 100%);
    }
    .main-header {
        background: linear-gradient(90deg, #0a0a2e, #1a3a8f, #0a0a2e);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #00BFFF;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(0, 191, 255, 0.3);
    }
    [data-testid="metric-container"] {
        background: rgba(0, 20, 80, 0.7);
        border: 1px solid #00BFFF;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 10px rgba(0, 191, 255, 0.2);
    }
    h1, h2, h3, p, label, .stMarkdown { color: white !important; }
    [data-testid="stMetricLabel"] { color: #00BFFF !important; }
    [data-testid="stMetricValue"] { color: white !important; }
    hr { border-color: #00BFFF; }
    .stCheckbox label { color: white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1 style="color:#00BFFF; font-size:2.5rem; margin:0;">🏏 IPL Data Analysis Dashboard</h1>
    <p style="color:white; margin:5px 0 0 0;">Real IPL Data | 2008 onwards | 1095 Matches</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("matches.csv")
df["season"] = df["season"].astype(str).str[:4]

# Metric cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Matches", len(df))
col2.metric("Seasons", df["season"].nunique())
col3.metric("Teams", df["team1"].nunique())
col4.metric("Top Team", df["winner"].value_counts().index[0])

st.divider()

# Season wise trophy
st.subheader("🏆 Season Wise Champions")

real_winners = {
    "2008": "Rajasthan Royals",
    "2009": "Deccan Chargers",
    "2010": "Chennai Super Kings",
    "2011": "Chennai Super Kings",
    "2012": "Kolkata Knight Riders",
    "2013": "Mumbai Indians",
    "2014": "Kolkata Knight Riders",
    "2015": "Mumbai Indians",
    "2016": "Sunrisers Hyderabad",
    "2017": "Mumbai Indians",
    "2018": "Chennai Super Kings",
    "2019": "Mumbai Indians",
    "2020": "Mumbai Indians",
    "2021": "Chennai Super Kings",
    "2022": "Gujarat Titans",
    "2023": "Chennai Super Kings"
}

team_colors = {
    "Mumbai Indians": "#004BA0",
    "Chennai Super Kings": "#F6A800",
    "Royal Challengers Bangalore": "#EC1C24",
    "Kolkata Knight Riders": "#3A225D",
    "Delhi Capitals": "#0078BC",
    "Rajasthan Royals": "#EA1A85",
    "Sunrisers Hyderabad": "#F7A721",
    "Punjab Kings": "#ED1B24",
    "Gujarat Titans": "#1C4B9B",
    "Deccan Chargers": "#FF6600",
}

available_seasons = sorted(df["season"].unique())
filtered_winners = {s: real_winners[s] for s in available_seasons if s in real_winners}

cols = st.columns(len(filtered_winners))
for i, (season, champion) in enumerate(filtered_winners.items()):
    color = team_colors.get(champion, "#333333")
    with cols[i]:
        st.markdown(f"""
        <div style="background-color:{color}; padding:10px; border-radius:10px; text-align:center; color:white; border: 1px solid #00BFFF; box-shadow: 0 0 8px rgba(0,191,255,0.3);">
            <div style="font-size:22px;">🏆</div>
            <div style="font-size:12px; font-weight:bold;">{season}</div>
            <div style="font-size:10px; margin-top:4px;">{champion}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

plt.style.use('dark_background')

# Graph 1 - Team wins
st.subheader("📊 Most Wins by Team")
fig, ax = plt.subplots(figsize=(12, 4))
fig.patch.set_facecolor('#0d1b4b')
ax.set_facecolor('#0d1b4b')
wins = df["winner"].value_counts().head(10)
wins.plot(kind="bar", ax=ax, color="#00BFFF")
ax.set_xlabel("Team", color='white')
ax.set_ylabel("Wins", color='white')
ax.tick_params(axis='x', rotation=45, colors='white')
ax.tick_params(axis='y', colors='white')
ax.spines['bottom'].set_color('#00BFFF')
ax.spines['left'].set_color('#00BFFF')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 2 - Toss decision
st.subheader("🪙 Toss Decision")
fig, ax = plt.subplots(figsize=(6, 4))
fig.patch.set_facecolor('#0d1b4b')
ax.set_facecolor('#0d1b4b')
toss = df["toss_decision"].value_counts()
ax.pie(toss, labels=toss.index, autopct="%1.1f%%",
       colors=["#00BFFF","#1E90FF"], startangle=90,
       textprops={'color': 'white'})
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 3 - Season matches
st.subheader("📈 Matches Per Season")
fig, ax = plt.subplots(figsize=(12, 3))
fig.patch.set_facecolor('#0d1b4b')
ax.set_facecolor('#0d1b4b')
season_matches = df.groupby("season").size()
ax.plot(season_matches.index, season_matches.values, marker="o", color="#00BFFF", linewidth=2, markersize=8)
ax.fill_between(season_matches.index, season_matches.values, alpha=0.2, color="#00BFFF")
ax.tick_params(colors='white', axis='x', rotation=45)
ax.tick_params(colors='white', axis='y')
ax.spines['bottom'].set_color('#00BFFF')
ax.spines['left'].set_color('#00BFFF')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, alpha=0.2, color='white')
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 4 - Top players
st.subheader("🌟 Top 10 Player of the Match")
fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor('#0d1b4b')
ax.set_facecolor('#0d1b4b')
mom = df["player_of_match"].value_counts().head(10)
ax.barh(mom.index, mom.values, color="#00BFFF")
ax.set_xlabel("Awards", color='white')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('#00BFFF')
ax.spines['left'].set_color('#00BFFF')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Graph 5 - Top venues
st.subheader("🏟️ Top 10 Venues")
fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor('#0d1b4b')
ax.set_facecolor('#0d1b4b')
venues = df["venue"].value_counts().head(10)
ax.barh(venues.index, venues.values, color="#1E90FF")
ax.set_xlabel("Matches", color='white')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('#00BFFF')
ax.spines['left'].set_color('#00BFFF')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
st.pyplot(fig)
plt.close()

if st.checkbox("Raw data "):
    st.dataframe(df)
