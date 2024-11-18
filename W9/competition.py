
class Event:
    """Represent an event in the competition."""

    def __init__(self, name, points):
        """Construct a new event.
        :param name: the name of the event
        :param points: the number of points awarded to the winner"""
        self.name = name
        self.points = points

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

def get_events():
    """Create the list of events in the competition
    :return: a list of competition events"""
    return [
        Event("5k Run", 10),
        Event("Long Jump", 5),
        Event("Chess Game", 7),
        Event("Rubik's Cube", 3),
        Event("Victoria Sponge Baking", 10)
    ]

def get_scores(events, num_players):
    """Prompt the user for the winner of each event
    :param events: the list of competition events
    :param num_players: the number of players in the competition
    :return: an list giving the score of each player 0..numPlayers - 1"""
    total_scores = [0] * num_players

    for i in range(5):
        winner = get_winner(events[i], num_players)
        total_scores[winner] += events[i].get_points()

    return total_scores

def get_winner(event, num_players):
    """Prompt the user for the winner of the given event
    :param event: the event in question
    :param num_players: the number of players in the competition"""
    print("Which player won the", event.get_name())
    while True:
        winner = int(input(
            "Enter player number between 0 and " +
            str(num_players - 1) +
            ": "
        ))
        if winner >= 0 and winner < num_players:
            return winner


def print_scores(scores):
    """Print the results of the competition to the screen
    :param scores: a list of scores, one entry for each player"""
    for i in range(len(scores)):
        print("Player", i, "scored", scores[i])

events = get_events()
scores = get_scores(events, 2)
print_scores(scores)
