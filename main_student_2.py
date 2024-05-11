from turtle import *
import soccerpack.analytics as analytics
import soccerpack.composer as composer
import soccerpack.graphics as graphics
import pprint

# The student working on the analytics (computing statistics) should modify this
# script.

# change this value to 1 for displaying the graphics plots
display_plots = 0

# The student working on the stats (computing statistics) should modify this
# script. The stats module will use the fake data defined in dictionaries in the
# script parser.data_example.py
# Once I grade, I will be using the data generated by your teammate.

# change the value of this variable as you complete each function so you
# can test them! the values go from 2 to 7
working_on = 7

print('***************************************************')
print('computing analytics')
print('***************************************************')


# You have to implement the functions in analytics, you have to decide
# which dictionary to pass as argument to these functions.
# Presently these functions are returning empty results because
# the dictionaries are empty except analytics.most_common_country()
# which I provide as example.

if working_on >= 1:
    pprint.pprint('Computing some analytics and printing the results')
    result = analytics.most_common_country(composer.fake_soccer_data)
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 2:
    result = analytics.get_top_scorer(composer.fake_soccer_data, 'Argentina')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 3:
    result = analytics.avg_goals_scored(composer.fake_soccer_data, 'Juventus')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 4:
    result = analytics.get_players_club_begin(composer.fake_soccer_data, 'A')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 4:
    result = analytics.get_players_name_begin(composer.fake_soccer_data, 'C')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 5:
    result = analytics.get_players_minutes_played(
        composer.fake_soccer_data, 325)
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 6:
    result = analytics.compute_avg_goals_countries(composer.fake_soccer_data)
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 7:
    result = analytics.compute_cards_per_country(
        composer.fake_soccer_data, color='y')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)

if working_on >= 7:
    result = analytics.compute_cards_per_country(
        composer.fake_soccer_data, color='r')
    pprint.pprint(result, width=150, compact=False, sort_dicts=False)
