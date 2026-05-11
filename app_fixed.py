import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

st.set_page_config(page_title="IPL Dashboard", page_icon="🏏", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    .stApp {
        background: linear-gradient(160deg, #060818 0%, #0a1628 40%, #0d2045 100%);
        font-family: 'Roboto', sans-serif;
    }
    .main-header {
        background: linear-gradient(90deg, #060818, #0a2a6e, #060818);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        border: 1px solid #00BFFF;
        margin-bottom: 25px;
        box-shadow: 0 0 30px rgba(0, 191, 255, 0.2);
    }
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(0,20,80,0.8), rgba(0,40,120,0.5));
        border: 1px solid rgba(0, 191, 255, 0.4);
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0, 191, 255, 0.1);
    }
    h1, h2, h3, p, label, .stMarkdown { color: white !important; }
    [data-testid="stMetricLabel"] { color: #00BFFF !important; font-size: 13px !important; }
    [data-testid="stMetricValue"] { color: white !important; font-size: 28px !important; font-weight: 700 !important; }
    hr { border-color: rgba(0, 191, 255, 0.3); }
    .stCheckbox label { color: white !important; }
    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #00BFFF !important;
        border-left: 4px solid #00BFFF;
        padding-left: 12px;
        margin: 20px 0 15px 0;
    }
    .trophy-card {
        border-radius: 12px;
        padding: 12px 8px;
        text-align: center;
        color: white;
        border: 1px solid rgba(0, 191, 255, 0.4);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div style="font-size:14px; color:#00BFFF; letter-spacing:4px; text-transform:uppercase; margin-bottom:8px;">TATA</div>
    <h1 style="color:white; font-size:2.8rem; margin:0; font-weight:700; letter-spacing:2px;">🏏 IPL Analytics Dashboard</h1>
    <p style="color:rgba(255,255,255,0.6); margin:8px 0 0 0; font-size:15px;">Indian Premier League | 2008 – 2025 | Complete Data Analysis</p>
</div>
""", unsafe_allow_html=True)

df = pd.read_csv("matches.csv")
df["season"] = df["season"].astype(str).str[:4]

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("🏟️ Total Matches", len(df))
col2.metric("📅 Seasons", df["season"].nunique())
col3.metric("👥 Teams", df["team1"].nunique())
col4.metric("🥇 Most Wins", df["winner"].value_counts().index[0])

st.divider()

# Season Champions
st.markdown('<div class="section-title">🏆 Season Wise Champions</div>', unsafe_allow_html=True)

real_winners = {
    "2008": ("Rajasthan Royals", "#EA1A85"),
    "2009": ("Deccan Chargers", "#FF6600"),
    "2010": ("Chennai Super Kings", "#F6A800"),
    "2011": ("Chennai Super Kings", "#F6A800"),
    "2012": ("Kolkata Knight Riders", "#3A225D"),
    "2013": ("Mumbai Indians", "#004BA0"),
    "2014": ("Kolkata Knight Riders", "#3A225D"),
    "2015": ("Mumbai Indians", "#004BA0"),
    "2016": ("Sunrisers Hyderabad", "#F7A721"),
    "2017": ("Mumbai Indians", "#004BA0"),
    "2018": ("Chennai Super Kings", "#F6A800"),
    "2019": ("Mumbai Indians", "#004BA0"),
    "2020": ("Mumbai Indians", "#004BA0"),
    "2021": ("Chennai Super Kings", "#F6A800"),
    "2022": ("Gujarat Titans", "#1C4B9B"),
    "2023": ("Chennai Super Kings", "#F6A800"),
    "2024": ("Kolkata Knight Riders", "#3A225D"),
    "2025": ("Royal Challengers Bengaluru", "#EC1C24"),
}

cols = st.columns(9)
for i, (season, (champion, color)) in enumerate(real_winners.items()):
    short_name = {
        "Rajasthan Royals": "RR", "Deccan Chargers": "DC",
        "Chennai Super Kings": "CSK", "Kolkata Knight Riders": "KKR",
        "Mumbai Indians": "MI", "Sunrisers Hyderabad": "SRH",
        "Gujarat Titans": "GT", "Royal Challengers Bengaluru": "RCB"
    }.get(champion, champion[:3].upper())
    with cols[i % 9]:
        st.markdown(f"""
        <div class="trophy-card" style="background: linear-gradient(135deg, {color}cc, {color}66);">
            <div style="font-size:20px;">🏆</div>
            <div style="font-size:13px; font-weight:700;">{season}</div>
            <div style="font-size:12px; color:rgba(255,255,255,0.9); font-weight:600;">{short_name}</div>
        </div>
        """, unsafe_allow_html=True)

if len(real_winners) > 9:
    cols2 = st.columns(9)
    items = list(real_winners.items())
    for i, (season, (champion, color)) in enumerate(items[9:]):
        short_name = {
            "Rajasthan Royals": "RR", "Deccan Chargers": "DC",
            "Chennai Super Kings": "CSK", "Kolkata Knight Riders": "KKR",
            "Mumbai Indians": "MI", "Sunrisers Hyderabad": "SRH",
            "Gujarat Titans": "GT", "Royal Challengers Bengaluru": "RCB"
        }.get(champion, champion[:3].upper())
        with cols2[i % 9]:
            st.markdown(f"""
            <div class="trophy-card" style="background: linear-gradient(135deg, {color}cc, {color}66);">
                <div style="font-size:20px;">🏆</div>
                <div style="font-size:13px; font-weight:700;">{season}</div>
                <div style="font-size:12px; color:rgba(255,255,255,0.9); font-weight:600;">{short_name}</div>
            </div>
            """, unsafe_allow_html=True)

st.divider()

plt.style.use('dark_background')
BG = '#0a1628'
ACCENT = '#00BFFF'

def style_ax(ax, fig):
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.tick_params(colors='white')
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color(ACCENT)
        ax.spines[spine].set_alpha(0.5)

# Graph 1 - Team wins
st.markdown('<div class="section-title">📊 Most Wins by Team</div>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(12, 4))
style_ax(ax, fig)
wins = df["winner"].value_counts().head(10)
bars = ax.bar(wins.index, wins.values, color=ACCENT, alpha=0.8, width=0.6)
for bar, val in zip(bars, wins.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(val),
            ha='center', va='bottom', color='white', fontsize=10, fontweight='bold')
ax.set_xlabel("Team", color='white', labelpad=10)
ax.set_ylabel("Wins", color='white')
ax.tick_params(axis='x', rotation=45, colors='white')
plt.tight_layout()
st.pyplot(fig)
plt.close()

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">🪙 Toss Decision</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    style_ax(ax, fig)
    toss = df["toss_decision"].value_counts()
    wedges, texts, autotexts = ax.pie(toss, labels=toss.index, autopct="%1.1f%%",
           colors=[ACCENT, "#1E90FF"], startangle=90,
           textprops={'color': 'white'}, wedgeprops={'edgecolor': BG, 'linewidth': 2})
    for at in autotexts:
        at.set_fontweight('bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown('<div class="section-title">📈 Matches Per Season</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    style_ax(ax, fig)
    season_matches = df.groupby("season").size()
    ax.plot(season_matches.index, season_matches.values, marker="o", color=ACCENT, linewidth=2.5, markersize=7)
    ax.fill_between(season_matches.index, season_matches.values, alpha=0.15, color=ACCENT)
    ax.tick_params(axis='x', rotation=45, colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.grid(True, alpha=0.1, color='white')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="section-title">🌟 Top Player of the Match</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    style_ax(ax, fig)
    mom = df["player_of_match"].value_counts().head(10)
    bars = ax.barh(mom.index, mom.values, color=ACCENT, alpha=0.8, height=0.6)
    ax.set_xlabel("Awards", color='white')
    ax.tick_params(colors='white')
    for bar, val in zip(bars, mom.values):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                str(val), va='center', color='white', fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col4:
    st.markdown('<div class="section-title">🏟️ Top Venues</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(7, 4))
    style_ax(ax, fig)
    venues = df["venue"].value_counts().head(8)
    short_venues = [v[:25] + "..." if len(v) > 25 else v for v in venues.index]
    bars = ax.barh(short_venues, venues.values, color="#1E90FF", alpha=0.8, height=0.6)
    ax.set_xlabel("Matches", color='white')
    ax.tick_params(colors='white')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.divider()

if st.checkbox("📋 Raw Data बघायची आहे?"):
    st.dataframe(df, use_container_width=True)

st.markdown("""
<div style="text-align:center; padding:20px; color:rgba(255,255,255,0.3); font-size:12px;">
    IPL Analytics Dashboard | Data Source: Kaggle | Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
