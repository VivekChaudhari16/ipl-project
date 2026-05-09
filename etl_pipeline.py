import pandas as pd
import os

# ============================================
# ETL PIPELINE - IPL Data
# ============================================

# ----------------------------
# STEP 1: EXTRACT
# ----------------------------
def extract():
    print("EXTRACT: Loading raw data...")
    df = pd.read_csv("ipl_matches.csv")
    print(f"Extracted {len(df)} rows, {len(df.columns)} columns")
    return df

# ----------------------------
# STEP 2: TRANSFORM
# ----------------------------
def transform(df):
    print("\nTRANSFORM: Cleaning and processing data...")

    # 1. Remove duplicates
    df = df.drop_duplicates()
    print(f"After removing duplicates: {len(df)} rows")

    # 2. Add win_margin column
    df["win_margin"] = df.apply(
        lambda x: f"{x['win_by_runs']} runs" if x["win_by_runs"] > 0
        else f"{x['win_by_wickets']} wickets", axis=1
    )

    # 3. Add toss_won_match column (did toss winner win the match?)
    df["toss_won_match"] = df["toss_winner"] == df["winner"]

    # 4. Add match_type column (close match or one-sided?)
    df["match_type"] = df["win_by_runs"].apply(
        lambda x: "Close" if 0 < x <= 20 else ("One-sided" if x > 20 else "Chase")
    )

    # 5. Season winner (team with most wins per season)
    season_winners = df.groupby("season")["winner"].agg(
        lambda x: x.value_counts().index[0]
    ).reset_index()
    season_winners.columns = ["season", "season_champion"]
    df = df.merge(season_winners, on="season", how="left")

    print("Added new columns: win_margin, toss_won_match, match_type, season_champion")
    print(f"Final shape: {df.shape}")
    return df

# ----------------------------
# STEP 3: LOAD
# ----------------------------
def load(df):
    print("\nLOAD: Saving processed data...")
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/ipl_processed.csv", index=False)
    print("Saved to data/ipl_processed.csv")

    # Save summary stats
    summary = {
        "total_matches": len(df),
        "total_seasons": df["season"].nunique(),
        "total_teams": df["team1"].nunique(),
        "toss_win_rate": f"{df['toss_won_match'].mean()*100:.1f}%",
        "most_wins": df["winner"].value_counts().index[0]
    }
    print("\nSummary Stats:")
    for k, v in summary.items():
        print(f"  {k}: {v}")

# ----------------------------
# RUN PIPELINE
# ----------------------------
if __name__ == "__main__":
    print("=" * 40)
    print("IPL ETL PIPELINE STARTED")
    print("=" * 40)
    
    raw_data = extract()
    processed_data = transform(raw_data)
    load(processed_data)
    
    print("\nETL PIPELINE COMPLETED!")
    print("=" * 40)
