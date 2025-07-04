class Player:
    def __init__(self, username):
        self.__username = username
        self.__score = 0

    @property
    def username(self):
        return self.__username

    @property
    def score(self):
        return self.__score

    def increment_score(self):
        self.__score += 1
