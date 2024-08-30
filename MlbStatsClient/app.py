from mlb_api_client import MlbStatsClient
import pandas as pd
import matplotlib.pyplot as plt

# initiate client
client = MlbStatsClient()

# get games data for 2024-06-18
games_df_06_18_24 = client.get_games_df("2024-06-18")
game_pk_list_06_18_24 = games_df_06_18_24["gamePk"]

# Get boxscore data for each game and generate single dataframe
boxscore_df_06_18_24 = pd.DataFrame()
for pk in game_pk_list_06_18_24:
    df = client.get_game_boxscore(game_pk=str(pk))
    boxscore_df_06_18_24 = pd.concat([boxscore_df_06_18_24, df])

print(boxscore_df_06_18_24)

# get pitching data for game id 746049
pitching_data_746049 = client.get_pitching_data(game_pk="746049")

print(pitching_data_746049)

# filter for swinging strikes and generate bar graph for left and right side at bats
strikes_746049 = pitching_data_746049[pitching_data_746049["pitchResult"] == "Swinging Strike"]

strike_count_by_pitch_hand = strikes_746049[["pitchHand", "pitchResult"]].groupby("pitchHand").count().rename(columns={"pitchResult":"SwingingStrikes"})

strike_count_by_pitch_hand.plot.bar(y="SwingingStrikes").plot()

plt.show()