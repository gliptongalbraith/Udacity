import random

move = ["rock", "paper", "scissors"]  # Defines moves


class Player:

    """
    Creates a Player class
    Takes argument self and returns rock
    Learn definition isn't used
    """

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer:

    """
    Creates a Random Player class
    Takes argument self and returns random string from list move
    Learn definition isn't used
    """

    def move(self):
        return random.choice(move)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer:

    """
    Creates a Human Player class
    Takes argument self and requests user input for move
    Requests input so long as move1 is not in list move
    Learn definition isn't used
    """

    def move(self):
        move1 = input(("Would you like to play rock, paper or scissors?:")
                      .lower())
        while move1 not in move:
            move1 = input("Would you like to play rock, paper or scissors?:")

        return move1

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer:

    """
    Creates a Reflect Player class
    Takes arguments self, my_move, and their_move
    Returns random string from list move if their_move undefined
    Otherwise returns their_move
    Learn function assigns their_move to self variable
    """

    their_move = "None"

    def move(self):
        if self.their_move == "None":
            self.their_move = random.choice(move)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer:

    """
    Creates a Cycle Player class
    Takes argument self
    Returns random string from list move if their_move undefined
    Otherwise cycles through variable options in order
    Learn function assigns my_move to self variable
    """

    my_move = "None"

    def move(self):
        while self.my_move == "None":
            self.my_move = random.choice(move)
        else:
            if self.my_move == "rock":
                self.my_move = "paper"
            elif self.my_move == "paper":
                self.my_move = "scissors"
            else:
                self.my_move = "rock"

        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):

    """
    Defines rules of the game
    Rock beats scissors, scissors beat paper, paper beats rock
    """

    return (
        (one == "rock" and two == "scissors") or
        (one == "scissors" and two == "paper") or
        (one == "paper" and two == "rock")
    )


class Game:

    """
    Defines structure of the game
    Each player moves, each move is printed, the learn function is called
    The score is then registered
    """

    def __init__(self, p1, p2):  # Sets initial variable of game
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            global P1_score
            print("Player 1 wins")
            self.p1.score = 1
            print(f"The score is {self.p1.score} to {self.p2.score}.")
        elif beats(move2, move1) is True:
            global P2_score
            print("Player 2 wins")
            self.p2.score = 1
            print(f"The score is {self.p1.score} to {self.p2.score}.")
        else:
            print("The round was a tie")
            print(f"The score is {self.p1.score} to {self.p2.score}.")

    def play_game(self):
        """
        Defines intro for game
        Prints start message, sets number of rounds
        Prints current round number, runs round,
        Prints game over once conditions met for ending game
        """
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print(f"The final score is {self.p1.score} to {self.p2.score}.")
        print("Game over!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
