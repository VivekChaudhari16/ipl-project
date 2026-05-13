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
        padding: 30px; border-radius: 16px; text-align: center;
        border: 1px solid #00BFFF; margin-bottom: 25px;
        box-shadow: 0 0 30px rgba(0, 191, 255, 0.2);
    }
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(0,20,80,0.8), rgba(0,40,120,0.5));
        border: 1px solid rgba(0, 191, 255, 0.4);
        border-radius: 12px; padding: 15px;
        box-shadow: 0 4px 15px rgba(0, 191, 255, 0.1);
    }
    h1, h2, h3, p, label, .stMarkdown { color: white !important; }
    [data-testid="stMetricLabel"] { color: #00BFFF !important; font-size: 13px !important; }
    [data-testid="stMetricValue"] { color: white !important; font-size: 28px !important; font-weight: 700 !important; }
    hr { border-color: rgba(0, 191, 255, 0.3); }
    .stCheckbox label { color: white !important; }
    .section-title {
        font-size: 18px; font-weight: 700; color: #00BFFF !important;
        border-left: 4px solid #00BFFF; padding-left: 12px; margin: 20px 0 15px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <div style="font-size:14px; color:#00BFFF; letter-spacing:4px; text-transform:uppercase; margin-bottom:8px;">TATA</div>
    <h1 style="color:white; font-size:2.8rem; margin:0; font-weight:700; letter-spacing:2px;">🏏 IPL Analytics Dashboard</h1>
    <p style="color:rgba(255,255,255,0.6); margin:8px 0 0 0; font-size:15px;">Indian Premier League | 2008 - 2023 | Complete Data Analysis</p>
</div>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("matches.csv")
df["season"] = df["season"].astype(str).str[:4]
deliveries = pd.read_csv("deliveries.csv")

# Overall Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("🏟️ Total Matches", len(df))
col2.metric("📅 Seasons", df["season"].nunique())
col3.metric("👥 Teams", df["team1"].nunique())
col4.metric("🥇 Most Wins", df["winner"].value_counts().index[0])

st.divider()

# Season Champions
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

short_names = {
    "Rajasthan Royals": "RR", "Deccan Chargers": "DC",
    "Chennai Super Kings": "CSK", "Kolkata Knight Riders": "KKR",
    "Mumbai Indians": "MI", "Sunrisers Hyderabad": "SRH",
    "Gujarat Titans": "GT", "Royal Challengers Bengaluru": "RCB"
}

st.markdown('<div class="section-title">🏆 Season Wise Champions — Season निवडा</div>', unsafe_allow_html=True)
st.markdown("<p style='color:rgba(255,255,255,0.5); font-size:12px;'>खालील dropdown मधून season select करा</p>", unsafe_allow_html=True)

# Season selector
all_seasons = sorted(df["season"].unique())
selected_season = st.selectbox("Season निवड", ["All Seasons"] + list(all_seasons), label_visibility="collapsed")

# Trophy cards row 1
items = list(real_winners.items())
cols = st.columns(9)
for i, (season, (champion, color)) in enumerate(items[:9]):
    sn = short_names.get(champion, champion[:3].upper())
    is_selected = selected_season == season
    border = "3px solid white" if is_selected else "1px solid rgba(0,191,255,0.4)"
    opacity = "1" if is_selected or selected_season == "All Seasons" else "0.4"
    with cols[i]:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{color}cc,{color}66);padding:10px 6px;border-radius:10px;text-align:center;color:white;border:{border};margin-bottom:5px;opacity:{opacity};">
            <div style="font-size:18px;">🏆</div>
            <div style="font-size:12px;font-weight:700;">{season}</div>
            <div style="font-size:10px;opacity:0.9;">{sn}</div>
        </div>""", unsafe_allow_html=True)

# Trophy cards row 2
cols2 = st.columns(9)
for i, (season, (champion, color)) in enumerate(items[9:]):
    sn = short_names.get(champion, champion[:3].upper())
    is_selected = selected_season == season
    border = "3px solid white" if is_selected else "1px solid rgba(0,191,255,0.4)"
    opacity = "1" if is_selected or selected_season == "All Seasons" else "0.4"
    with cols2[i]:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{color}cc,{color}66);padding:10px 6px;border-radius:10px;text-align:center;color:white;border:{border};margin-bottom:5px;opacity:{opacity};">
            <div style="font-size:18px;">🏆</div>
            <div style="font-size:12px;font-weight:700;">{season}</div>
            <div style="font-size:10px;opacity:0.9;">{sn}</div>
        </div>""", unsafe_allow_html=True)

# Filter data based on season
if selected_season != "All Seasons":
    filtered_df = df[df["season"] == selected_season]
    season_label = f"Season {selected_season}"
    # Show season champion info
    if selected_season in real_winners:
        champ, color = real_winners[selected_season]
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{color}44,{color}22);padding:15px;border-radius:12px;text-align:center;border:1px solid {color};margin:10px 0;">
            <span style="font-size:24px;">🏆</span>
            <span style="color:white;font-size:16px;font-weight:700;margin-left:10px;">{selected_season} Champion: {champ}</span>
        </div>""", unsafe_allow_html=True)
else:
    filtered_df = df
    season_label = "All Seasons"

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Match Analysis", "🏏 Batsmen Stats", "🎯 Bowler Stats"])

BG = '#0a1628'
ACCENT = '#00BFFF'
plt.style.use('dark_background')

def style_ax(ax, fig, color=None):
    c = color or ACCENT
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.tick_params(colors='white')
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color(c)
        ax.spines[spine].set_alpha(0.5)

# TAB 1
with tab1:
    st.markdown(f'<div class="section-title">📊 Match Analysis — {season_label}</div>', unsafe_allow_html=True)

    # Filtered metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Matches", len(filtered_df))
    c2.metric("Teams", filtered_df["team1"].nunique())
    winner_counts = filtered_df["winner"].value_counts()
    c3.metric("Top Team", winner_counts.index[0] if len(winner_counts) > 0 else "-")
    c4.metric("Top Team Wins", winner_counts.iloc[0] if len(winner_counts) > 0 else 0)

    # Graph 1 - Team wins
    st.markdown('<div class="section-title">📊 Most Wins by Team</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 4))
    style_ax(ax, fig)
    wins = filtered_df["winner"].value_counts().head(10)
    bars = ax.bar(wins.index, wins.values, color=ACCENT, alpha=0.8, width=0.6)
    for bar, val in zip(bars, wins.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val),
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
        toss = filtered_df["toss_decision"].value_counts()
        ax.pie(toss, labels=toss.index, autopct="%1.1f%%",
               colors=[ACCENT, "#1E90FF"], startangle=90,
               textprops={'color': 'white'}, wedgeprops={'edgecolor': BG, 'linewidth': 2})
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="section-title">🌟 Top Player of the Match</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig)
        mom = filtered_df["player_of_match"].value_counts().head(10)
        bars = ax.barh(mom.index, mom.values, color=ACCENT, alpha=0.8, height=0.6)
        for bar, val in zip(bars, mom.values):
            ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                    str(val), va='center', color='white', fontsize=9)
        ax.set_xlabel("Awards", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    if selected_season == "All Seasons":
        st.markdown('<div class="section-title">📈 Matches Per Season</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 3))
        style_ax(ax, fig)
        season_matches = df.groupby("season").size()
        ax.plot(season_matches.index, season_matches.values, marker="o", color=ACCENT, linewidth=2.5, markersize=7)
        ax.fill_between(season_matches.index, season_matches.values, alpha=0.15, color=ACCENT)
        ax.tick_params(axis='x', rotation=45, colors='white')
        ax.grid(True, alpha=0.1, color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    col3, col4 = st.columns(2)
    with col3:
        st.markdown('<div class="section-title">🏟️ Top Venues</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig, "#1E90FF")
        venues = filtered_df["venue"].value_counts().head(8)
        short_venues = [v[:25] + "..." if len(v) > 25 else v for v in venues.index]
        ax.barh(short_venues, venues.values, color="#1E90FF", alpha=0.8, height=0.6)
        ax.set_xlabel("Matches", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col4:
        if selected_season == "All Seasons":
            st.markdown('<div class="section-title">🎖️ Most Titles</div>', unsafe_allow_html=True)
            title_counts = {}
            for s, (champ, _) in real_winners.items():
                title_counts[champ] = title_counts.get(champ, 0) + 1
            title_df = pd.Series(title_counts).sort_values(ascending=False).head(8)
            fig, ax = plt.subplots(figsize=(7, 4))
            style_ax(ax, fig, "#FFD700")
            bars = ax.barh(title_df.index, title_df.values, color="#FFD700", alpha=0.85, height=0.6)
            for bar, val in zip(bars, title_df.values):
                ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                        str(val), va='center', color='white', fontsize=10, fontweight='bold')
            ax.set_xlabel("Titles", color='white')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()

# TAB 2
with tab2:
    # Filter deliveries by season
    if selected_season != "All Seasons":
        season_match_ids = filtered_df["id"].tolist()
        filtered_del = deliveries[deliveries["match_id"].isin(season_match_ids)]
    else:
        filtered_del = deliveries

    st.markdown(f'<div class="section-title">🏏 Batsmen Stats — {season_label}</div>', unsafe_allow_html=True)

    batsmen_runs = filtered_del.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(15)

    fig, ax = plt.subplots(figsize=(12, 5))
    style_ax(ax, fig, "#FFD700")
    bars = ax.bar(batsmen_runs.index, batsmen_runs.values, color="#FFD700", alpha=0.85, width=0.6)
    for bar, val in zip(bars, batsmen_runs.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10, str(val),
                ha='center', va='bottom', color='white', fontsize=8, fontweight='bold')
    ax.set_xlabel("Batsman", color='white')
    ax.set_ylabel("Total Runs", color='white')
    ax.tick_params(axis='x', rotation=45, colors='white')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">💥 Most Sixes</div>', unsafe_allow_html=True)
        sixes = filtered_del[filtered_del["batsman_runs"] == 6].groupby("batter").size().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig, "#FF6B35")
        ax.barh(sixes.index, sixes.values, color="#FF6B35", alpha=0.85, height=0.6)
        ax.set_xlabel("Sixes", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="section-title">🔥 Most Fours</div>', unsafe_allow_html=True)
        fours = filtered_del[filtered_del["batsman_runs"] == 4].groupby("batter").size().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig, "#4CAF50")
        ax.barh(fours.index, fours.values, color="#4CAF50", alpha=0.85, height=0.6)
        ax.set_xlabel("Fours", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    st.markdown('<div class="section-title">🔍 Player Stats Search</div>', unsafe_allow_html=True)
    all_batsmen = sorted(filtered_del["batter"].unique())
    selected_batsman = st.selectbox("Batsman निवड", all_batsmen)
    if selected_batsman:
        p = filtered_del[filtered_del["batter"] == selected_batsman]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Runs", int(p["batsman_runs"].sum()))
        c2.metric("Sixes", int((p["batsman_runs"] == 6).sum()))
        c3.metric("Fours", int((p["batsman_runs"] == 4).sum()))
        c4.metric("Innings", int(p["match_id"].nunique()))

# TAB 3
with tab3:
    if selected_season != "All Seasons":
        season_match_ids = filtered_df["id"].tolist()
        filtered_del2 = deliveries[deliveries["match_id"].isin(season_match_ids)]
    else:
        filtered_del2 = deliveries

    st.markdown(f'<div class="section-title">🎯 Bowler Stats — {season_label}</div>', unsafe_allow_html=True)

    wickets = filtered_del2[filtered_del2["is_wicket"] == 1].groupby("bowler").size().sort_values(ascending=False).head(15)

    fig, ax = plt.subplots(figsize=(12, 5))
    style_ax(ax, fig, "#9C27B0")
    bars = ax.bar(wickets.index, wickets.values, color="#9C27B0", alpha=0.85, width=0.6)
    for bar, val in zip(bars, wickets.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(val),
                ha='center', va='bottom', color='white', fontsize=9, fontweight='bold')
    ax.set_xlabel("Bowler", color='white')
    ax.set_ylabel("Wickets", color='white')
    ax.tick_params(axis='x', rotation=45, colors='white')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">📋 Dismissal Types</div>', unsafe_allow_html=True)
        dismissals = filtered_del2[filtered_del2["is_wicket"] == 1]["dismissal_kind"].value_counts()
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig, "#9C27B0")
        colors_list = ["#9C27B0","#E91E63","#FF5722","#FF9800","#FFC107","#4CAF50","#00BCD4"]
        ax.barh(dismissals.index, dismissals.values, color=colors_list[:len(dismissals)], alpha=0.85)
        ax.set_xlabel("Count", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        st.markdown('<div class="section-title">🔍 Bowler Stats Search</div>', unsafe_allow_html=True)
        all_bowlers = sorted(filtered_del2["bowler"].unique())
        selected_bowler = st.selectbox("Bowler निवड", all_bowlers)
        if selected_bowler:
            b = filtered_del2[filtered_del2["bowler"] == selected_bowler]
            c1, c2 = st.columns(2)
            c1.metric("Wickets", int((b["is_wicket"] == 1).sum()))
            c2.metric("Matches", int(b["match_id"].nunique()))
            c3, c4 = st.columns(2)
            c3.metric("Runs Given", int(b["total_runs"].sum()))
            economy = round(int(b["total_runs"].sum()) / (len(b) / 6), 2) if len(b) > 0 else 0
            c4.metric("Economy", economy)

st.divider()
if st.checkbox("📋 Raw Match Data"):
    st.dataframe(filtered_df, use_container_width=True)

st.markdown("""
<div style="text-align:center;padding:20px;color:rgba(255,255,255,0.3);font-size:12px;">
    IPL Analytics Dashboard | Data: Kaggle | Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
