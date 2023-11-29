class GameScorer:
    def __init__(self, name_team_1=None, name_team_2=None, score_team_1=None, score_team_2=None):
        # Assumes that either all or none of the arguments are None
        self.name_team_1 = name_team_1
        self.name_team_2 = name_team_2
        self.score_team_1 = score_team_1
        self.score_team_2 = score_team_2
        self.points_team_1, self.points_team_2 = None, None
        # If both names of the teams are None, ask for them
        if None in (self.name_team_1, self.name_team_2):
            self.input_names_scores()

    # Method to ask for names and scores of teams
    def input_names_scores(self):
        self.name_team_1 = input("Enter name of team 1: ")
        self.name_team_2 = input("Enter name of team 2: ")
        self.score_team_1 = int(input(f"Enter score of {self.name_team_1}: "))
        self.score_team_2 = int(input(f"Enter score of {self.name_team_2}: "))

    def __str__(self):
        return (f"Team {self.name_team_1}: Score: {self.score_team_1}, Points: {self.points_team_1}\n"
                f"Team {self.name_team_2}: Score: {self.score_team_2}, Points: {self.points_team_2}")


# Class FootballScorer inherits from GameScorer
class FootballScorer(GameScorer):
    def __init__(self, week_game, name_team_1=None, name_team_2=None, score_team_1=None, score_team_2=None):
        # Note the relation to parent class using super()
        super().__init__(name_team_1, name_team_2, score_team_1, score_team_2)
        self.week_game = week_game

    def calculate_points(self):
        if self.score_team_1 > self.score_team_2:
            self.points_team_1, self.points_team_2 = 3, 0
        elif self.score_team_1 < self.score_team_2:
            self.points_team_1, self.points_team_2 = 0, 3
        else:
            self.points_team_1, self.points_team_2 = 1, 1

    def __str__(self):
        # Note the relation to parent class using super()
        return (f"\nGame of week: {self.week_game}\n" +
                super().__str__())


class TeamFootballSeason:
    def __init__(self, n_games, name_team_1, names_team_2, scores_team_1, scores_team_2):
        self.n_games = n_games
        names_team_1 = [name_team_1] * n_games
        # The games are composed of FootballScorer objects
        self.games = [FootballScorer(game, names_team_1[n], names_team_2[n], scores_team_1[n], scores_team_2[n]) for
                      n, game in enumerate(range(n_games))]

    def add_game(self, name_team_2, score_team_1, score_team_2):
        self.n_games += 1
        self.games.append(FootballScorer(self.n_games, self.games[0].name_team_1, name_team_2, score_team_1, score_team_2))

    def add_football_scorer(self, fs):
        self.n_games += 1
        self.games.append(fs)

    def __str__(self):
        return '\n'.join([str(game) for game in self.games])


if __name__ == '__main__':
    gs = GameScorer()
    print(gs)

    fs2 = FootballScorer(4, 't1', 't2', 0, 3)
    fs2.calculate_points()
    print(fs2)  # Note the difference to the parent class

    fst = TeamFootballSeason(3, 't1', ['t2', 't3', 't4'], [1, 2, 3], [0, 1, 2])
    print(fst)

    fst.add_game('t5', 1, 1)
    print(fst)