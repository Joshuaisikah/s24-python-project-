


# Finds the country with the largest number of total minutes played
# by their players and returns a tuple, with the name of the country
# and the total number of minutes played by the players of that country.

# Don't modify the function most_common_country, it has already been implemented
# so you have an idea on what is the process to follow for the other functions.
def most_common_country(data):
    print('Analytics module computing -> most_common_country: ', end='')

    largest_minutes_played = 0
    total_minutes_played = 0
    max_country_name = ''

    # iterates over countries and player data for that country
    for country, players in data.items():

        total_minutes_played = 0
        # iterates over players of a country
        for player, player_data in players.items():
            # references minutes played for each player
            total_minutes_played += int(player_data[7])

        # if the total minutes played for this country's players
        # is greater than the previous greater value, replace it
        # reference also the name of that country
        if total_minutes_played > largest_minutes_played:
            largest_minutes_played = total_minutes_played
            max_country_name = country

    return (max_country_name, largest_minutes_played)


# Finds the top scorer for a given country, returns a tuple with the name
# of the player and the number of goals scorer. If there are more than
# one player with the same number of goals, returns the one at the top alphabetically.
def get_top_scorer(data, country):
    top_scorer = ''
    max_goals = 0
    for player, stats in data[country].items():
        goals = int(stats[10])
        if goals > max_goals or (goals == max_goals and player < top_scorer):
            top_scorer = player
            max_goals = goals
    return (top_scorer, max_goals)

#fix
def avg_goals_scored(data, club):
    total_goals = 0
    count = 0
    for country in data.values():
        for player, stats in country.items():
            if stats[2] == club and int(stats[10]) > 0:
                total_goals += int(stats[10])
                count += 1
    return (club, total_goals / count if count else 0)

def get_players_club_begin(data, letter):
    players = []
    for country in data.values():
        for player, stats in country.items():
            if stats[2].startswith(letter):
                players.append((player, int(stats[6])))
    return players

def get_players_name_begin(data, letter):
    players = []
    for country in data.values():
        for player, stats in country.items():
            if player.startswith(letter):
                players.append((player, int(stats[6])))
    return players
def get_players_minutes_played(data, limit):
    players = []
    for country in data.values():
        for player, stats in country.items():
            if int(stats[6]) < limit:
                players.append((player, int(stats[6])))
    return players

def compute_avg_goals_countries(data):
    countries_avg_goals = []
    for country, players in data.items():
        total_goals = 0
        player_count = 0
        for player, stats in players.items():
            total_goals += int(stats[10])
            player_count += 1
        average_goals = total_goals / player_count if player_count != 0 else 0
        countries_avg_goals.append((country, average_goals))
    return countries_avg_goals

def compute_cards_per_country(data, color='y'):
    countries_total_cards = []
    index = 11 if color == 'y' else 12
    for country, players in data.items():
        total_cards = 0
        for player_data in players.values():
            if len(player_data) > index:
                total_cards += int(player_data[index])
        countries_total_cards.append((country, total_cards))
    return countries_total_cards