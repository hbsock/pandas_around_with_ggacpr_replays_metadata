import pandas as pd
import matplotlib.pyplot as plt


def get_count_of_characters(df):
    char_count_df = df.loc[:, ["p1_character", "p2_character"] ].apply(pd.value_counts)
    return char_count_df["p1_character"] + char_count_df["p2_character"]

def get_count_of_characters_for_specific_steam_id(df, steam_id):

    def get_character_of_steam_id(x):
        if x["p1_steam_id"] == steam_id:
            return x["p1_character"]
        elif x["p2_steam_id"] == steam_id:
            return x["p2_character"]

    result_df = df.query( "p1_steam_id == @steam_id or p2_steam_id == @steam_id" )\
        .apply( get_character_of_steam_id, axis=1 )

    return pd.value_counts(result_df)

if __name__ == "__main__":
    metadata_df = pd.read_csv("/home/hanbinsock/programman/ggacr_replays_metadata.csv")

    # Metadata updates were applied after a patch in November 2021, so replays before then don't have valid
    # data after the p2_rounds_won column
    # Can just filter by `problem_bitmask > 8` if only latest version metadata are desired as that should be the only bit mask used for valid metadata.
    # Reference: https://steamcommunity.com/app/348550/discussions/0/3203746177244378016/

    #char_count_df = get_count_of_characters( metadata_df )
    #plt.show( char_count_df.plot.bar() )

    char_count_of_nibnab_df = get_count_of_characters_for_specific_steam_id(metadata_df, 76561198011058687)
    plt.show( char_count_of_nibnab_df.plot.bar() )
