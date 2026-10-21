
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "PNRao_HR_Analytics_Recruitment_Funnel.csv"
)


def main():
    df = pd.read_csv(DATA_FILE)

    df["ApplicationDate"] = pd.to_datetime(
        df["ApplicationDate"], errors="coerce"
    )
    df["DateatStage"] = pd.to_datetime(
        df["DateatStage"], errors="coerce"
    )

    reference_date = pd.Timestamp("2026-10-21")

    print("RECRUITMENT FUNNEL VALIDATION")
    print("=" * 45)

    print(f"Total records: {len(df):,}")
    print(f"Unique candidates: {df['CandidateID'].nunique():,}")
    print(f"Unique positions: {df['PositionID'].nunique():,}")

    print(
        "Invalid application dates:",
        df["ApplicationDate"].isna().sum()
    )
    print(
        "Invalid stage dates:",
        df["DateatStage"].isna().sum()
    )

    print(
        "Stage date before application date:",
        (
            df["DateatStage"].notna()
            & df["ApplicationDate"].notna()
            & (df["DateatStage"] < df["ApplicationDate"])
        ).sum()
    )
        
    future_stages = df[df["DateatStage"] > reference_date]

    print("\nFuture stage dates by stage:")
    print(
        future_stages["Stage"]
        .value_counts()
        .to_string()
    )

    print("\nFuture stage dates by candidate source:")
    print(
        future_stages["Source"]
        .value_counts()
        .to_string()
    )

    print("\nEarliest and latest stage dates:")
    print("Earliest:", df["DateatStage"].min())
    print("Latest:", df["DateatStage"].max())

    print(
        "Application dates after reference date:",
        (df["ApplicationDate"] > reference_date).sum()
    )
    print(
        "Stage dates after reference date:",
        (df["DateatStage"] > reference_date).sum()
    )

    print("\nRecruitment stages:")
    print(df["Stage"].value_counts(dropna=False).to_string())

    print("\nCandidate sources:")
    print(df["Source"].value_counts(dropna=False).to_string())

    
    print("\nCandidates with multiple distinct stages:")
    stages_per_candidate = df.groupby("CandidateID")["Stage"].nunique()
    print((stages_per_candidate > 1).sum())

    print("\nNumber of distinct stages per candidate:")
    print(stages_per_candidate.value_counts().sort_index().to_string())

    print("\nCandidates appearing more than once:")
    candidate_counts = df["CandidateID"].value_counts()
    print((candidate_counts > 1).sum())

if __name__ == "__main__":
    main()
