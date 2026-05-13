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

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("🏟️ Total Matches", len(df))
col2.metric("📅 Seasons", df["season"].nunique())
col3.metric("👥 Teams", df["team1"].nunique())
col4.metric("🥇 Most Wins", df["winner"].value_counts().index[0])

st.divider()

# Tabs
tab1, tab2, tab3 = st.tabs(["🏆 Match Analysis", "🏏 Batsmen Stats", "🎯 Bowler Stats"])

# =====================
# TAB 1 - Match Analysis
# =====================
with tab1:
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

    short_names = {
        "Rajasthan Royals": "RR", "Deccan Chargers": "DC",
        "Chennai Super Kings": "CSK", "Kolkata Knight Riders": "KKR",
        "Mumbai Indians": "MI", "Sunrisers Hyderabad": "SRH",
        "Gujarat Titans": "GT", "Royal Challengers Bengaluru": "RCB"
    }

    items = list(real_winners.items())
    row1 = items[:9]
    row2 = items[9:]

    cols = st.columns(9)
    for i, (season, (champion, color)) in enumerate(row1):
        sn = short_names.get(champion, champion[:3].upper())
        with cols[i]:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,{color}cc,{color}66);padding:10px 6px;border-radius:10px;text-align:center;color:white;border:1px solid rgba(0,191,255,0.4);margin-bottom:5px;">
                <div style="font-size:18px;">🏆</div>
                <div style="font-size:12px;font-weight:700;">{season}</div>
                <div style="font-size:10px;opacity:0.9;">{sn}</div>
            </div>""", unsafe_allow_html=True)

    cols2 = st.columns(9)
    for i, (season, (champion, color)) in enumerate(row2):
        sn = short_names.get(champion, champion[:3].upper())
        with cols2[i]:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,{color}cc,{color}66);padding:10px 6px;border-radius:10px;text-align:center;color:white;border:1px solid rgba(0,191,255,0.4);margin-bottom:5px;">
                <div style="font-size:18px;">🏆</div>
                <div style="font-size:12px;font-weight:700;">{season}</div>
                <div style="font-size:10px;opacity:0.9;">{sn}</div>
            </div>""", unsafe_allow_html=True)

    st.divider()

    BG = '#0a1628'
    ACCENT = '#00BFFF'
    plt.style.use('dark_background')

    def style_ax(ax, fig):
        fig.patch.set_facecolor(BG)
        ax.set_facecolor(BG)
        ax.tick_params(colors='white')
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax.spines[spine].set_color(ACCENT)
            ax.spines[spine].set_alpha(0.5)

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
        ax.pie(toss, labels=toss.index, autopct="%1.1f%%",
               colors=[ACCENT, "#1E90FF"], startangle=90,
               textprops={'color': 'white'}, wedgeprops={'edgecolor': BG, 'linewidth': 2})
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
        for bar, val in zip(bars, mom.values):
            ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                    str(val), va='center', color='white', fontsize=9)
        ax.set_xlabel("Awards", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col4:
        st.markdown('<div class="section-title">🏟️ Top Venues</div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(7, 4))
        style_ax(ax, fig)
        venues = df["venue"].value_counts().head(8)
        short_venues = [v[:25] + "..." if len(v) > 25 else v for v in venues.index]
        ax.barh(short_venues, venues.values, color="#1E90FF", alpha=0.8, height=0.6)
        ax.set_xlabel("Matches", color='white')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

# =====================
# TAB 2 - Batsmen Stats
# =====================
with tab2:
    st.markdown('<div class="section-title">🏏 Top Batsmen Analysis</div>', unsafe_allow_html=True)

    # Top run scorers
    batsmen_runs = deliveries.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(15)

    st.markdown('<div class="section-title">📊 Top 15 Run Scorers (All Time)</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 5))
    BG = '#0a1628'
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    bars = ax.bar(batsmen_runs.index, batsmen_runs.values, color="#FFD700", alpha=0.85, width=0.6)
    for bar, val in zip(bars, batsmen_runs.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, str(val),
                ha='center', va='bottom', color='white', fontsize=8, fontweight='bold')
    ax.set_xlabel("Batsman", color='white', labelpad=10)
    ax.set_ylabel("Total Runs", color='white')
    ax.tick_params(axis='x', rotation=45, colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#FFD700')
        ax.spines[spine].set_alpha(0.5)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    col1, col2 = st.columns(2)

    with col1:
        # Most sixes
        st.markdown('<div class="section-title">💥 Most Sixes</div>', unsafe_allow_html=True)
        sixes = deliveries[deliveries["batsman_runs"] == 6].groupby("batter").size().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(7, 4))
        fig.patch.set_facecolor(BG)
        ax.set_facecolor(BG)
        ax.barh(sixes.index, sixes.values, color="#FF6B35", alpha=0.85, height=0.6)
        ax.set_xlabel("Sixes", color='white')
        ax.tick_params(colors='white')
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax.spines[spine].set_color('#FF6B35')
            ax.spines[spine].set_alpha(0.5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        # Most fours
        st.markdown('<div class="section-title">🔥 Most Fours</div>', unsafe_allow_html=True)
        fours = deliveries[deliveries["batsman_runs"] == 4].groupby("batter").size().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(7, 4))
        fig.patch.set_facecolor(BG)
        ax.set_facecolor(BG)
        ax.barh(fours.index, fours.values, color="#4CAF50", alpha=0.85, height=0.6)
        ax.set_xlabel("Fours", color='white')
        ax.tick_params(colors='white')
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax.spines[spine].set_color('#4CAF50')
            ax.spines[spine].set_alpha(0.5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    # Batsman search
    st.markdown('<div class="section-title">🔍 Player Stats Search</div>', unsafe_allow_html=True)
    all_batsmen = sorted(deliveries["batter"].unique())
    selected_batsman = st.selectbox("Batsman निवड", all_batsmen)
    if selected_batsman:
        p = deliveries[deliveries["batter"] == selected_batsman]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Runs", int(p["batsman_runs"].sum()))
        c2.metric("Sixes", int((p["batsman_runs"] == 6).sum()))
        c3.metric("Fours", int((p["batsman_runs"] == 4).sum()))
        c4.metric("Innings", int(p["match_id"].nunique()))

# =====================
# TAB 3 - Bowler Stats
# =====================
with tab3:
    st.markdown('<div class="section-title">🎯 Top Bowlers Analysis</div>', unsafe_allow_html=True)

    wickets = deliveries[deliveries["is_wicket"] == 1].groupby("bowler").size().sort_values(ascending=False).head(15)

    st.markdown('<div class="section-title">🎯 Top 15 Wicket Takers (All Time)</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 5))
    BG = '#0a1628'
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    bars = ax.bar(wickets.index, wickets.values, color="#9C27B0", alpha=0.85, width=0.6)
    for bar, val in zip(bars, wickets.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, str(val),
                ha='center', va='bottom', color='white', fontsize=9, fontweight='bold')
    ax.set_xlabel("Bowler", color='white', labelpad=10)
    ax.set_ylabel("Wickets", color='white')
    ax.tick_params(axis='x', rotation=45, colors='white')
    ax.tick_params(axis='y', colors='white')
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#9C27B0')
        ax.spines[spine].set_alpha(0.5)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    col1, col2 = st.columns(2)

    with col1:
        # Dismissal types
        st.markdown('<div class="section-title">📋 Dismissal Types</div>', unsafe_allow_html=True)
        dismissals = deliveries[deliveries["is_wicket"] == 1]["dismissal_kind"].value_counts()
        fig, ax = plt.subplots(figsize=(7, 4))
        fig.patch.set_facecolor(BG)
        ax.set_facecolor(BG)
        colors_list = ["#9C27B0", "#E91E63", "#FF5722", "#FF9800", "#FFC107", "#4CAF50", "#00BCD4"]
        ax.barh(dismissals.index, dismissals.values, color=colors_list[:len(dismissals)], alpha=0.85)
        ax.set_xlabel("Count", color='white')
        ax.tick_params(colors='white')
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['bottom', 'left']:
            ax.spines[spine].set_color('#9C27B0')
            ax.spines[spine].set_alpha(0.5)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

    with col2:
        # Bowler search
        st.markdown('<div class="section-title">🔍 Bowler Stats Search</div>', unsafe_allow_html=True)
        all_bowlers = sorted(deliveries["bowler"].unique())
        selected_bowler = st.selectbox("Bowler निवड", all_bowlers)
        if selected_bowler:
            b = deliveries[deliveries["bowler"] == selected_bowler]
            wickets_taken = int((b["is_wicket"] == 1).sum())
            runs_given = int(b["total_runs"].sum())
            matches = int(b["match_id"].nunique())
            economy = round(runs_given / (len(b) / 6), 2) if len(b) > 0 else 0
            c1, c2 = st.columns(2)
            c1.metric("Wickets", wickets_taken)
            c2.metric("Matches", matches)
            c3, c4 = st.columns(2)
            c3.metric("Runs Given", runs_given)
            c4.metric("Economy", economy)

st.divider()
if st.checkbox("📋 Raw Match Data"):
    st.dataframe(df, use_container_width=True)

st.markdown("""
<div style="text-align:center;padding:20px;color:rgba(255,255,255,0.3);font-size:12px;">
    IPL Analytics Dashboard | Data: Kaggle | Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
