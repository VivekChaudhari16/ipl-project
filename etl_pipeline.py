import pandas as pd
import os

# ============================================
# ETL PIPELINE - Real IPL Data
# ============================================

# ----------------------------
# STEP 1: EXTRACT
# ----------------------------
def extract():
    print("EXTRACT: Loading raw data...")
    df = pd.read_csv("matches.csv")
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

    # 2. Fix season column
    df["season"] = df["season"].astype(str).str[:4]

    # 3. Add toss_won_match column
    df["toss_won_match"] = df["toss_winner"] == df["winner"]

    # 4. Add match_type_result column
    df["match_result_type"] = df.apply(
        lambda x: f"Won by {int(x['result_margin'])} runs" 
        if x["result"] == "runs" 
        else f"Won by {int(x['result_margin'])} wickets" 
        if x["result"] == "wickets" 
        else "Tie/No Result", axis=1
    )

    # 5. Season winner
    season_winners = df.groupby("season")["winner"].agg(
        lambda x: x.value_counts().index[0]
    ).reset_index()
    season_winners.columns = ["season", "season_champion"]
    df = df.merge(season_winners, on="season", how="left")

    print("Added: toss_won_match, match_result_type, season_champion")
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
