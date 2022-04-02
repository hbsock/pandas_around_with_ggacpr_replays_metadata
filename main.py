import pandas as pd


if __name__ == "__main__":
    metadata = pd.read_csv("/home/hanbinsock/programman/ggacr_replays_metadata.csv")

    # Metadata updates were applied after a patch in November 2021, so replays before then don't have valid
    # data after the p2_rounds_won column
    # Can just filter by `problem_bitmask > 8` if only latest version metadata are desired as that should be the only bit mask used for valid metadata.
    # Reference: https://steamcommunity.com/app/348550/discussions/0/3203746177244378016/

    # metadata = metadata[metadata.problem_bitmask <= 8]


