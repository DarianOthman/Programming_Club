class FootballScorer:
    def __init__(self, name_team_1=None, name_team_2=None, score_team_1=None, score_team_2=None):
        self.name_team_1 = name_team_1
        self.name_team_2 = name_team_2
        self.score_team_1 = score_team_1
        self.score_team_2 = score_team_2
        self.points_team_1, self.points_team_2 = None, None
        if None in (self.name_team_1, self.name_team_2):
            self.input_names_scores()

    def input_names_scores(self):
        self.name_team_1 = input("Enter name of team 1: ")
        self.name_team_2 = input("Enter name of team 2: ")
        self.score_team_1 = int(input(f"Enter score of {self.name_team_1}: "))
        self.score_team_2 = int(input(f"Enter score of {self.name_team_2}: "))

    # Method to calculate points based on scores
    def calculate_points(self):
        if self.score_team_1 > self.score_team_2:
            self.points_team_1, self.points_team_2 = 3, 0
        elif self.score_team_1 < self.score_team_2:
            self.points_team_1, self.points_team_2 = 0, 3
        else:
            self.points_team_1, self.points_team_2 = 1, 1

    def __str__(self):
        return (f"Team 1: Score: {self.score_team_1}, Points: {self.points_team_1}\n"
                f"Team 2: Score: {self.score_team_2}, Points: {self.points_team_2}")


if __name__ == '__main__':
    # This will call the function input_names_scores() in the object initialization
    fs = FootballScorer()
    # and then calculate_points()
    fs.calculate_points()
    # and then print using the reserved method __str__()
    print(fs)

    # This will directly input the names and scores in the object initialization
    fs2 = FootballScorer('t1', 't2', 1, 2)
    fs2.calculate_points()
    print(fs2)
