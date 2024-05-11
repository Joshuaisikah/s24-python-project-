# *************************************************
# Functions
# *************************************************
# build_position_data: builds the position_data dictionary by using as input values
# passed as argument on the parameter data, when the function is invoked
# This function returns a dictionary where:
# Key -> position
#   Value -> list all players in that position

# Don't modify the function build_position_data, it has already been implemented
# so you have an idea on what is the process to follow for the other functions.

def build_position_data(data):

    temp_data = {}

    # iterates over all countries
    for country, player in data.items():

        # for each country, iterates over all players
        for player_name, player_data in player.items():
            # the first entry in player_data is the position the
            # player plays
            player_position = player_data[0]

            # if the position is not in the temp dictionary, creates the entry
            # with that position as key and assigns as value the player name
            if player_position not in temp_data:
                temp_data[player_position] = [player_name]

            # if the position is already in the temp dictionary, references that entry
            # and appends as value the player name
            else:
                temp_data[player_position].append(player_name)

    return temp_data
def build_roster_data(data):
    temp_data = {}
    for country, players in data.items():
        temp_data[country] = list(players.keys())
    return temp_data

def build_goals_score_data(data):
    temp_data = {}
    for players in data.values():
        for player, stats in players.items():
            goals = int(stats[10])
            temp_data.setdefault(goals, []).append(player)
    return temp_data

def build_country_club_data(data):
    temp_data = {}
    for country, players in data.items():
        for player, stats in players.items():
            club = stats[2]
            temp_data.setdefault(country, {}).setdefault(club, []).append(player)
    return temp_data

def build_club_country_data(data):
    temp_data = {}
    for country, players in data.items():
        for player, stats in players.items():
            club = stats[2]
            temp_data.setdefault(club, {}).setdefault(country, []).append(player)
    return temp_data

def build_year_player_data(data):
    temp_data = {}
    for players in data.values():
        for player, stats in players.items():
            try:
                year_born = int(stats[3])
                temp_data.setdefault(year_born, []).append(player)
            except (ValueError, IndexError):
                print(f"Error processing data for player {player}. Please check the data structure.")
    return temp_data
def build_start_player_data(data):
    temp_data = {}
    for country, players in data.items():
        for player, stats in players.items():
            games_started = int(float(stats[7]))
            temp_data.setdefault(games_started, {}).setdefault(country, []).append(player)
    return temp_data
