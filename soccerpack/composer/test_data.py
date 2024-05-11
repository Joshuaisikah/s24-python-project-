# Don't modify this file, it provides some fake data, so that the student in charge of analytics module can
# test the code even if the dictionaries in composer are not completed by the other team member.
# This also helps the student responsible for working on the composer module to understand what
# is the format of the expected output.

# This is a dictionary, where:
#   Key -> country
# Value -> nested dictionary, where:
#            Key -> name of the player
#          Value -> list with values for each player
fake_soccer_data = {
    'Argentina': {
        'Lionel Messi': ['FW', '35-177', 'Paris S-G', 1987, 7, 7, 690, 7.7, 7, 3, 3, 1, 0],
        'Ángel Di María': ['MF', '34-307', 'Juventus', 1988, 5, 4, 288, 3.2, 1, 1, 1, 0, 0]
    },
    'Australia': {
        'Craig Goodwin': ['MF', '31-002', 'Adelaide', 1991, 4, 3, 234, 2.6, 1, 1, 1, 0, 0],
        'Fran Karačić': ['DF', '26-220', 'Brescia', 1996, 2, 1, 93, 1, 0, 0, 0, 0, 0]
    },
    'Cameroon': {
        'Bryan Mbeumo': ['FW', '23-133', 'Brentford', 1999, 3, 3, 233, 2.6, 0, 0, 0, 0, 0],
        'Christian Bassogog': ['MF', '27-061', 'Shanghai Shen', 1995, 1, 0, 24, 0.3, 0, 0, 0, 1, 0]
    },
    'Costa Rica': {
        'Johan Venegas': ['FW', '34-021', 'Liga Deportiva Alajuelense', 1988, 1, 1, 73, 0.8, 0, 0, 0, 0, 0],
        'Juan Pablo Vargas': ['DF', '27-195', 'Millonarios', 1995, 1, 1, 90, 1, 1, 0, 1, 0, 0]
    },
    'France': {
        'Adrien Rabiot': ['MF', '27-259', 'Juventus', 1995, 6, 5, 483, 5.4, 1, 1, 1, 1, 0],
        'Antoine Griezmann': ['MF', '31-272', 'Atlético Madrid', 1991, 7, 6, 537, 6, 0, 3, 0, 1, 0]
    },
    'Belgium': {
        'Axel Witsel': ['MF', '33-340', 'Atlético Madrid', 1989, 3, 3, 270, 3, 0, 0, 0, 0, 0],
        'Yannick Carrasco': ['FW', '29-105', 'Atlético Madrid', 1993, 2, 2, 116, 1.3, 0, 0, 0, 1, 0]
    }
}

# This is a dictionary where
# Key -> position
# Value -> list all players in that position
fake_position_data = {
    'FW': ['Lionel Messi',
        'Bryan Mbeumo',
        'Johan Venegas',
        'Yannick Carrasco'],
    'MF': ['Ángel Di María',
        'Craig Goodwin',
        'Christian Bassogog',
        'Adrien Rabiot',
        'Antoine Griezmann',
        'Axel Witsel'],
    'DF': ['Fran Karačić', 'Juan Pablo Vargas']}


# This is a dictionary where
#   Key -> country
#   Value -> list of players that are from that country
fake_roster_data = {
    'Argentina': ['Lionel Messi', 'Ángel Di María'],
    'Australia': ['Craig Goodwin', 'Fran Karačić'],
    'Cameroon': ['Bryan Mbeumo', 'Christian Bassogog'],
    'Costa Rica': ['Johan Venegas', 'Juan Pablo Vargas'],
    'France': ['Adrien Rabiot', 'Antoine Griezmann'],
    'Belgium': ['Axel Witsel', 'Yannick Carrasco']
}

# This is a dictionary where
#   Key -> number of goals
# Value -> list all players who scored that number of goals

fake_goals_score_data = {
    7: ['Lionel Messi'],
    1: ['Ángel Di María', 'Craig Goodwin', 'Juan Pablo Vargas', 'Adrien Rabiot'],
    0: ['Fran Karačić', 'Bryan Mbeumo', 'Christian Bassogog', 'Johan Venegas', 'Antoine Griezmann', 'Axel Witsel', 'Yannick Carrasco']
}

# This is a dictionary where
#   Key -> country
# Value -> nested dictionary, where:
#       Key -> name of a club
#     Value -> list of players in that club for that country
fake_country_club_data = {
    'Argentina':
        {'Paris S-G': ['Lionel Messi'], 'Juventus': ['Ángel Di María']},
    'Australia':
        {'Adelaide': ['Craig Goodwin'], 'Brescia': ['Fran Karačić']},
    'Cameroon':
        {'Brentford': ['Bryan Mbeumo'], 'Shanghai Shen': ['Christian Bassogog']},
    'Costa Rica':
        {'Liga Deportiva Alajuelense': ['Johan Venegas'], 'Millonarios': ['Juan Pablo Vargas']},
    'France':
        {'Juventus': ['Adrien Rabiot'], 'Atlético Madrid': ['Antoine Griezmann']},
    'Belgium':
        {'Atlético Madrid': ['Axel Witsel', 'Yannick Carrasco']}
}

# This is a dictionary where
#   Key -> club name
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players in that country that play for that club

fake_club_country_data = {
    'Paris S-G':
        {'Argentina': ['Lionel Messi']},
    'Juventus':
        {'Argentina': ['Ángel Di María'], 'France': ['Adrien Rabiot']},
    'Adelaide':
        {'Australia': ['Craig Goodwin']},
    'Brescia':
        {'Australia': ['Fran Karačić']},
    'Brentford':
        {'Cameroon': ['Bryan Mbeumo']},
    'Shanghai Shen':
        {'Cameroon': ['Christian Bassogog']},
    'Liga Deportiva Alajuelense':
        {'Costa Rica': ['Johan Venegas']},
    'Millonarios':
        {'Costa Rica': ['Juan Pablo Vargas']},
    'Atlético Madrid':
        {'France': ['Antoine Griezmann'], 'Belgium': ['Axel Witsel', 'Yannick Carrasco']}
}

# This is a dictionary where
#   Key -> year
#   Value -> list of players that were born in that year
fake_year_player_data = {
    1987: ['Lionel Messi'],
    1988: ['Ángel Di María', 'Johan Venegas'],
    1991: ['Craig Goodwin', 'Antoine Griezmann'],
    1996: ['Fran Karačić'],
    1999: ['Bryan Mbeumo'],
    1995: ['Christian Bassogog', 'Juan Pablo Vargas', 'Adrien Rabiot'],
    1989: ['Axel Witsel'],
    1993: ['Yannick Carrasco']
}

# This is a dictionary where
#   Key -> starts
# Value -> nested dictionary, where:
#       Key -> country
#     Value -> list of players from that country that started that number of games
fake_start_player_data = {
    7: {
        'Argentina': ['Lionel Messi']
    },
    4: {
        'Argentina': ['Ángel Di María']
    },
    3: {
        'Australia': ['Craig Goodwin'],
        'Cameroon': ['Bryan Mbeumo'],
        'Belgium': ['Axel Witsel']
    },
    1: {
        'Australia': ['Fran Karačić'],
        'Costa Rica': ['Johan Venegas', 'Juan Pablo Vargas']
    },
    0: {
        'Cameroon': ['Christian Bassogog']
    },
    5: {
        'France': ['Adrien Rabiot']
    },
    6: {
        'France': ['Antoine Griezmann']
    },
    2: {
        'Belgium': ['Yannick Carrasco']
    }
}

# This dictionary is used to illustrate the use of the visualization module which
# is optional and not required as part of the project.
# This is a dictionary where
#   Key -> club
# Value -> nested dictionary, where:
#       Key -> player
#     Value -> number of goals scored
fake_top_scorers = {
    'Paris S-G': {
        'Kylian Mbappé': 8,
        'Lionel Messi': 7,
        'Neymar': 2,
        'Carlos Soler': 1
    },
    'Manchester United': {
        'Marcus Rashford': 3,
        'Bruno Fernandes': 2,
        'Casemiro': 1,
        'Cristiano Ronaldo': 1
    }
}