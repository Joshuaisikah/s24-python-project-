from turtle import *
import soccerpack.composer as composer
import soccerpack.graphics as graphics
import pprint

# The student working on the composer (populating the dictionaries) should modify this
# script.

# change the value of this variable as you complete each function
# the values go from 2 to 7
working_on = 7

# change this value to True for displaying the graphics plots only if you decide
# to work on the bonus functions in the visualization module
display_plots = False

# which_dataset indicates which dataset to use
#   1 is for the fake_soccer_dataset.csv (6 countries, 12 players)
#   2 is for the soccer_small_dataset.csv (5 countries, 111 players)
#   3 is for the soccer_large_dataset.csv (32 countries, 160 players)
#   4 is for the soccer_complete_dataset.csv (32 countries, 680 players)
# To test your script with a different dataset change the value of this
# variable, by default use 1, which corresponds to fake_soccer_dataset.csv file
which_dataset = 1

datasets = {
    1: 'fake_soccer_dataset.csv',
    2: 'soccer_small_dataset.csv',
    3: 'soccer_large_dataset.csv',
    4: 'soccer_complete_dataset.csv'
}

if which_dataset < 1 or which_dataset > 4:
    print('----> use a value between 1 and 4 for which_dataset')
    exit()

# ************************************************
# Dictionary variables
# ************************************************


# These are the variables for storing or referencing the dictionaries
# that will be built when invoking the different functions below.
# Initially they are empty.

soccer_data = {}
position_data = {}
roster_data = {}
goals_score_data = {}
country_club_data = {}
club_country_data = {}
year_player_data = {}
start_player_data = {}

# ************************************************
# Invoking functions to build and populate the
# dictionaries.
# ************************************************

print('***************************************************')
print('building dictionaries')
print('***************************************************')

# builds a dictionary that has as key the country, and the value is a nested dictionary,
# where the key is the player's name and the value a list with all the data for that player
# the variable soccer_data will reference that dictionary

if working_on >= 1:
    name_of_input_file = datasets[which_dataset]
    print('******* Loading Original Soccer Data from file: ' +
          name_of_input_file + ' *******')
    soccer_data = composer.read_file(name_of_input_file)
    pprint.pprint(soccer_data, width=140, compact=False, sort_dicts=False)
    print('There are ', len(soccer_data), ' countries in the dataset!')

# Note: as you implement the other functions that populate the rest
# of the dictionaries, look at the output of the previously populated
# dictionaries to decide which is the best suited to be passed as
# argument to each function. In this example, soccer_data is used
# but it might be the case that a different dictionary has the data
# in a more suitable structure for you to access it.
# Also, you don't have to read again the data from the file. It has
# already been loaded and stored in the variable soccer_data

if working_on >= 2:
    print('******* Position Data *******')
    position_data = composer.build_position_data(soccer_data)
    pprint.pprint(position_data, width=50, compact=False, sort_dicts=False)

    print('******* Roster Data *******')
    roster_data = composer.build_roster_data(soccer_data)
    pprint.pprint(roster_data, width=150, compact=False, sort_dicts=False)

if working_on >= 3:
    print('******* Goals Score Data *******')
    goals_score_data = composer.build_goals_score_data(soccer_data)
    pprint.pprint(goals_score_data, width=150, compact=False, sort_dicts=False)

if working_on >= 4:
    print('******* Country Club Data *******')
    country_club_data = composer.build_country_club_data(soccer_data)
    pprint.pprint(country_club_data, width=150,
                  compact=False, sort_dicts=False)

if working_on >= 5:
    print('******* Club Country Data *******')
    club_country_data = composer.build_club_country_data(soccer_data)
    pprint.pprint(club_country_data, width=150,
                  compact=False, sort_dicts=False)

if working_on >= 6:
    print('******* Year Player Data *******')
    year_player_data = composer.build_year_player_data(soccer_data)
    pprint.pprint(year_player_data, width=150, compact=False, sort_dicts=False)

if working_on >= 7:
    print('******* Starts Player Data *******')
    start_player_data = composer.build_start_player_data(soccer_data)
    pprint.pprint(start_player_data, width=150,
                  compact=False, sort_dicts=False)


if display_plots == True:
    # Implementing the functions below is optional and a bonus for the project
    # they are not required
    print('***************************************************')
    print('******* Showing some plots *******')
    print('***************************************************')

    # Plots the top 3 scorers for team 'Paris S-G', uses fake data
    # just to illustrate how the graphics module works
    graphics.plot_top_k_fake_items_doc(
        composer.fake_top_scorers, 'Paris S-G', 4)

    # Plots the counts of goals scored by the top k players of a given club,
    # where k is a number between 1 and 5. For example if you pass 3,
    # the plot includes the top 3 scorers.
    # graphics.plot_top_k_scorer_club(soccer_data, 'Juventus', 3)

    # plots the counts of goals scored by the top k players of a given country,
    # where k is a number between 1 and 5. For example if you pass 3, the plot
    # includes the top 3 scorers.
    # graphics.plot_top_k_scorer_country(soccer_data, 'Argentina', 3)

    # Plots the total number of goals per country.
    # graphics.plot_goals_per_country(soccer_data)

    # Plots the total number of yellow cards per country
    # graphics.plot_yellow_cards_per_country(soccer_data)
    # graphics.plot_red_cards_per_country(soccer_data)

    # makes the plot function to stop, uncomment this line when working on your code
    # to test the functions in the graphics module
    graphics.render()
