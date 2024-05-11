
from soccerpack.analytics.stats import most_common_country, get_top_scorer, avg_goals_scored, get_players_club_begin, get_players_name_begin, get_players_minutes_played, compute_avg_goals_countries, compute_cards_per_country
from soccerpack.analytics.stats import most_common_country, get_top_scorer, avg_goals_scored, get_players_club_begin, get_players_name_begin, get_players_minutes_played, compute_avg_goals_countries, compute_cards_per_country
import turtle

def plot_top_k_fake_items_doc(data, title, k):
    # Assuming data is a dictionary where the keys are labels and the values are heights
    labels = list(data.keys())[:k]
    heights = list(data.values())[:k]

    # Create a new turtle screen and set its background color
    wn = turtle.Screen()
    wn.bgcolor("white")

    # Create a new turtle object
    t = turtle.Turtle()
    t.color("black")
    t.shape("turtle")

    # Draw the bars
    for i in range(len(labels)):
        t.penup()
        t.goto(i * 25, 0)
        t.pendown()
        t.begin_fill()
        t.left(90)
        t.forward(heights[i])
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(heights[i])
        t.left(90)
        t.end_fill()

    # Hide the turtle and close the window when clicked
    t.hideturtle()
    turtle.done()

# ... rest of your functions ...
def plot_top_k_scorer_club(soccer_data, club, k):
    print('plot_top_k_scorer_club: ')
    players = get_players_club_begin(soccer_data, club)
    players.sort(key=lambda x: x[1], reverse=True)
    plot_top_k_fake_items_doc(dict(players[:k]), club, k)

# ... rest of your functions ...
def plot_top_k_scorer_club(soccer_data, club, k):
    print('plot_top_k_scorer_club: ')
    players = get_players_club_begin(soccer_data, club)
    players.sort(key=lambda x: x[1], reverse=True)
    plot_top_k_fake_items_doc(dict(players[:k]), club, k)

def plot_top_k_scorer_country(soccer_data, country, k):
    print('plot_top_k_scorer_country: ')
    players = get_players_name_begin(soccer_data, country)
    players.sort(key=lambda x: x[1], reverse=True)
    plot_top_k_fake_items_doc(dict(players[:k]), country, k)

def plot_goals_per_country(soccer_data):
    print('plot_goals_per_country: ')
    goals = compute_avg_goals_countries(soccer_data)
    plot_top_k_fake_items_doc(dict(goals), "Goals per Country", len(goals))

def plot_yellow_cards_per_country(soccer_data):
    print('plot_yellow_cards_per_country: ')
    yellow_cards = compute_cards_per_country(soccer_data, 'y')
    plot_top_k_fake_items_doc(dict(yellow_cards), "Yellow Cards per Country", len(yellow_cards))

def plot_red_cards_per_country(soccer_data):
    print('plot_red_cards_per_country: ')
    red_cards = compute_cards_per_country(soccer_data, 'r')
def plot_top_k_scorer_club(soccer_data, club, k):
    print('plot_top_k_scorer_club: ')
    players = []
    for country in soccer_data.values():
        for player, stats in country.items():
            if stats[4] == club:
                players.append((player, int(stats[10])))
    players.sort(key=lambda x: x[1], reverse=True)
    plot_top_k_fake_items_doc(dict(players[:k]), club, k)

def plot_top_k_scorer_country(soccer_data, country, k):
    print('plot_top_k_scorer_country: ')
    players = [(player, int(stats[10])) for player, stats in soccer_data[country].items()]
    players.sort(key=lambda x: x[1], reverse=True)
    plot_top_k_fake_items_doc(dict(players[:k]), country, k)

def plot_goals_per_country(soccer_data):
    print('plot_goals_per_country: ')
    goals = [(country, sum(int(player[10]) for player in players.values())) for country, players in soccer_data.items()]
    plot_top_k_fake_items_doc(dict(goals), "Goals per Country", len(goals))

def plot_yellow_cards_per_country(soccer_data):
    print('plot_yellow_cards_per_country: ')
    yellow_cards = [(country, sum(int(player[13]) for player in players.values())) for country, players in soccer_data.items()]
    plot_top_k_fake_items_doc(dict(yellow_cards), "Yellow Cards per Country", len(yellow_cards))

def plot_red_cards_per_country(soccer_data):
    print('plot_red_cards_per_country: ')
    red_cards = [(country, sum(int(player[14]) for player in players.values())) for country, players in soccer_data.items()]
    plot_top_k_fake_items_doc(dict(red_cards), "Red Cards per Country", len(red_cards))

    import matplotlib.pyplot as plt

    def plot_top_k_fake_items_doc(data, title, k):
        # Assuming data is a dictionary where the keys are labels and the values are heights
        labels = list(data.keys())
        heights = list(data.values())

        plt.bar(labels, heights)
        plt.title(title)
        plt.show()