from requests import request
import pandas as pd
import json


class MlbStatsClient():
    def __init__(self):
        """
        This function initiates the mlb stats api client with the various endpoints

        Parameters:
        -----------
        None

        Returns:
        -----------
        None 
        """
        self.base_url =  "https://statsapi.mlb.com"
        self.games_endpoint = "/api/v1/schedule?sportId=1&date="
        self.boxscore_endpoint = "/api/v1/game/{gamePk}/boxscore"
        self.playbyplay_endpoint = "/api/v1/game/{gamePk}/playByPlay"

    def get_games_df(self, date:str):
        """
        This function returns a dataframe with data from the schedule api for the given data

        Parameters:
        -----------
        date: str
            a date in the format yyyy-mm-dd

        Returns:
        -----------
        games_df: DataFrame
            a pandas dataframe with information from the games played on the given date.
        """
        response = request(url = self.base_url+self.games_endpoint+date, method='get').json()
        try:
            games = response["dates"][0]["games"]
            
            columns_to_drop = ["link", "recordSource", "ifNecessary", "ifNecessaryDescription", "resumedFrom", "resumedFromDate",
                            "gameGuid", "gameDate", "reverseHomeAwayStatus", "inningBreakLength", "rescheduledFrom",
                            "rescheduledFromDate", "description", "publicFacing", "isTie", "content", "status", "teams", "venue",
                            "doubleHeader", "tiebreaker", "gamedayType", "calendarEventID", "scheduledInnings"]

            teams_columns_to_drop = ["away.team.link", "home.team.link", "away.leagueRecord.pct",
                                    "home.leagueRecord.pct", "away.seriesNumber", "home.seriesNumber",
                                    "away.splitSquad", "home.splitSquad", "away.isWinner"]
            
            df = pd.DataFrame.from_dict(games)

            status_df = pd.json_normalize(df["status"])["statusCode"]
            teams_df = pd.json_normalize(df["teams"]).drop(columns=teams_columns_to_drop)
            venue_df = pd.json_normalize(df["venue"]).drop(columns=["link"]).rename(columns={"id":"venueId", "name":"venueName"})

            columns_to_drop = set(columns_to_drop).intersection(set(df.columns))

            games_df = df.join(status_df).join(teams_df).join(venue_df).drop(columns=columns_to_drop)

            return games_df
        except:
            return "Something Went Wrong!"
    
    def get_game_boxscore(self, game_pk:str):
        """
        This function is used to retrieve boxscore data for the given game

        Parameters:
        -----------
        game_pk: str
            the game identifier in string format

        Returns:
        -----------
        final_df: DataFrame
            a pandas dataframe containing boxscore information for the given game. 
        """
        endpoint = self.boxscore_endpoint.replace("{gamePk}", game_pk)
        response = request(url=self.base_url+endpoint, method='get').json()

        away_json = response["teams"]["away"]
        home_json = response["teams"]["home"]


        away_df = pd.DataFrame.from_dict([away_json["team"]])[["id", "name"]].rename(columns={"id":"teamId", "name":"teamName"})
        home_df = pd.DataFrame.from_dict([home_json["team"]])[["id", "name"]].rename(columns={"id":"teamId", "name":"teamName"})

        away_batting_df = pd.DataFrame.from_dict([away_json["teamStats"]["batting"]])
        away_pitching_df = pd.DataFrame.from_dict([away_json["teamStats"]["pitching"]])
        away_fielding_df = pd.DataFrame.from_dict([away_json["teamStats"]["fielding"]])

        columns_to_drop_batting = ["doubles", "triples", "baseOnBalls", "intentionalWalks", "hitByPitch",
                        "caughtStealing", "stolenBasePercentage", "groundIntoDoublePlay",
                        "groundIntoTriplePlay", "plateAppearances", "leftOnBase", "sacBunts",
                        "sacFlies", "catchersInterference", "pickoffs", "atBatsPerHomeRun", "popOuts", "lineOuts"]
        columns_to_drop_pitching = set(away_batting_df)\
                .intersection(away_pitching_df)\
                .union(["inningsPitched", "saveOpportunities", "completeGames", "shutouts",
                    "strikePercentage", "hitBatsmen", "groundOutsToAirouts", "pitchesPerInning",
                    "runsScoredPer9", "homeRunsPer9", "inheritedRunners", "inheritedRunnersScored",
                    "passedBall", "balks"])
        columns_to_drop_fielding = set(away_batting_df).intersection(away_fielding_df)
            

        away_batting_df.drop(columns=columns_to_drop_batting, inplace=True)
        away_pitching_df.drop(columns=columns_to_drop_pitching, inplace=True)
        away_fielding_df = away_fielding_df["errors"]

        away_df = away_df.join(away_batting_df).join(away_pitching_df).join(away_fielding_df)
        away_df.index = [game_pk]

        home_batting_df = pd.DataFrame.from_dict([home_json["teamStats"]["batting"]])
        home_pitching_df = pd.DataFrame.from_dict([home_json["teamStats"]["pitching"]])
        home_fielding_df = pd.DataFrame.from_dict([home_json["teamStats"]["fielding"]])

        home_batting_df.drop(columns=columns_to_drop_batting, inplace=True)
        home_pitching_df.drop(columns=columns_to_drop_pitching, inplace=True)
        home_fielding_df = home_fielding_df["errors"]

        home_df = home_df.join(home_batting_df).join(home_pitching_df).join(home_fielding_df)
        home_df.index = [game_pk]

        final_df = pd.concat([home_df, away_df])

        return (final_df)
    

    def get_pitching_data(self, game_pk:str):
        """
        This function generates a dataframe with pitching data for the given game

        Parameters:
        -----------
        game_pk: str
            the identifier for the given game in string format

        Returns:
        -----------
        pitches_df: DataFrame
            a pandas dataframe containing data for each pitch thrown in the game. 
        """
 
        endpoint = self.playbyplay_endpoint.replace("{gamePk}", game_pk)
        response = request(url=self.base_url+endpoint, method='get').json()

        plays = response["allPlays"]

        pitches = []

        for play in plays:
            events = play["playEvents"]
            inning = play["about"]["inning"]
            half_inning = play["about"]["halfInning"]
            pitcher_id = play["matchup"]["pitcher"]["id"]
            pitch_hand = play["matchup"]["pitchHand"]["description"]
            batter_id = play["matchup"]["batter"]["id"]
            bat_side = play["matchup"]["batSide"]["description"]
            at_bat_result = play["result"]["event"]
            i = 0
            for event in events:
                if event["isPitch"]:
                    try:

                        pitch_result = event["details"]["description"]
                        zone = event["pitchData"]["zone"]
                        start_speed = event["pitchData"]["startSpeed"]
                        pitch_number = event["pitchNumber"]

                        event_json = {
                            "inning":inning,
                            "halfInning":half_inning,
                            "pitcherId":pitcher_id,
                            "pitchHand":pitch_hand,
                            "batterId":batter_id,
                            "batSide":bat_side,
                            "atBatResult":at_bat_result,
                            "pitchResult":pitch_result,
                            #"zone":zone,
                            "startSpeed":start_speed,
                            "pitchNumber":pitch_number
                        }

                        pitches.append(event_json)
                        i+=1
                    except Exception as e:
                        pass
        pitches_df = pd.DataFrame.from_dict(pitches)
        return pitches_df
    

if __name__ == "__main__":
    client = MlbStatsClient()

