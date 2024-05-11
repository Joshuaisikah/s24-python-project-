# Do not modify this script!!!!!!
import os
# this list has the metadata for the dataset, that is the names of the columns
metadata = ['position', 'age', 'club', 'birth_year', 'games', 'games_starts', 'minutes', 'minutes_90s', 'goals',
            'assists', 'goals_pens', 'cards_yellow', 'cards_red']


# reads from a text file and returns a dictionary where the key is the country
# and the value is another dictionary where the key is the player name and the
# value a list with all data for that player
def read_file(file):
    complete_data = {}

    print('input file is: ' + file)

    with open('datasets/' + file, encoding='utf-8') as file_handler:
        count = 0
        for line in file_handler:
            # skips the first line from the file because it has only the column names (metadata)
            if count > 0:
                # use comma to break down the line into columns and returns a list
                line = line.replace('\n', '').split(',')

                # extracts data from the line based on the index of each column
                player_name = line[0]
                country_name = line[2]
                original_player_data = [line[1]] + line[3:]
                player_data = []
                for value in original_player_data :

                    # tries to convert a string to integer
                    try:
                        player_data.append(int(value))

                    # if it fails try to convert a string to a float
                    except ValueError:
                        try:
                            player_data.append(float(value))

                        # if it fails it treats the value as a string
                        except ValueError:
                            player_data.append(value)

                # if the country_name is new, add it to the dictionary
                if country_name not in complete_data:
                    complete_data[country_name] = {player_name: player_data}

                # if the country_name already exists in the dictionary, adds the
                # new entry to the existing dictionary entries
                else:
                    complete_data[country_name][player_name] = player_data
            count += 1

    # returns the dictionary to the caller
    return complete_data
