from itertools import count
from math import fabs
from pickle import TRUE
from human import Human


class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [
            ["|", " ", "|", " ", "|", " ", "|"],
            ["-", "+", "-", "+", "-", "+", "-"],
            ["|", " ", "|", " ", "|", " ", "|"],
            ["-", "+", "-", "+", "-", "+", "-"],
            ["|", " ", "|", " ", "|", " ", "|"],
            ["-", "+", "-", "+", "-", "+", "-"], ]

    def welcome_message(self):
        print(f"Welcome to the Tic Tac Toe game!\n")

    def check_user_input(self, user_range):

        while True:
            user_input = input(
                f"How many human players in this game? (Enter from 0 to {user_range}):\n")
            try:
                user_input = int(user_input)
                if user_input in range(0, user_range+1):
                    print(f"{user_input} human player has selected.\n")
                    break
                else:
                    print("Check your selection, try again\n")
                    continue
            except ValueError:
                print("Invalid input, please enter a valid integer within the range\n")
                continue
        return user_input

    def determine_user_num_symbol(self):
        self.number_of_human_player = self.check_user_input(2)
        if self.number_of_human_player == 2:
            self.player1 = Human("Human Player 1")
            self.player2 = Human("Human Player 2")
        print(f"-----{self.player1.name} is choosing symbol-----")
        self.player1.choose_symbol()
        if self.player1.symbol == "X":
            self.player2.symbol = "O"
        else:
            self.player2.symbol = "X"
        print(f"{self.player1.name} chose {self.player1.symbol}")
        print(f"{self.player2.name} chose {self.player2.symbol}")

        # if self.number_of_human_player == 1:
        #     self.player1 = Human()
        #     self.player2 = Machine()
        # elif self.number_of_human_player == 2:
        #     self.player1 = Human()
        #     self.player2 = Human()

    def display_board(self, board):
        for i in board:
            print(" ".join(i))
        # print(" ".join(board))
        # print(self.board_row2)
        # print(self.board_row3)

    def update_board(self, position, symbol):
        if position == 1:
            self.board[4][1] = symbol
        elif position == 2:
            self.board[4][3] = symbol
        elif position == 3:
            self.board[4][5] = symbol
        elif position == 4:
            self.board[2][1] = symbol
        elif position == 5:
            self.board[2][3] = symbol
        elif position == 6:
            self.board[2][5] = symbol
        elif position == 7:
            self.board[0][1] = symbol
        elif position == 8:
            self.board[0][3] = symbol
        else:
            self.board[0][5] = symbol
        self.display_board(self.board)

    def machine_turn(self):
        pass

    def determine_winner(self, counter):
        self.game_on = True
        if counter == 9:
            print('tie, board full, no winner')
            self.game_on = False
        else:
            # player1 is the winner
            if self.board[0][1] == self.board[0][3] == self.board[0][5] == self.player1.symbol:
                # player1 top row wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[2][1] == self.board[2][3] == self.board[2][5] == self.player1.symbol:
                # player1 middle row wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[4][1] == self.board[4][3] == self.board[4][5] == self.player1.symbol:
                # player1 bottom row wins
                print(f"{self.player1.name} wins")
                self.game_on = False

            elif self.board[0][1] == self.board[2][1] == self.board[4][1] == self.player1.symbol:
                # player1 first column wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[0][3] == self.board[2][3] == self.board[4][3] == self.player1.symbol:
                # player1 second column wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[0][5] == self.board[2][3] == self.board[4][5] == self.player1.symbol:
                # player1 second column wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[0][1] == self.board[2][3] == self.board[4][5] == self.player1.symbol:
                # player1 diagonal wins
                print(f"{self.player1.name} wins")
                self.game_on = False
            elif self.board[0][5] == self.board[2][3] == self.board[4][1] == self.player1.symbol:
                # player1 diagonal wins
                print(f"{self.player1.name} wins")
                self.game_on = False

            # player2 is the winner
            elif self.board[0][1] == self.board[0][3] == self.board[0][5] == self.player2.symbol:
                # player2 top row wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[2][1] == self.board[2][3] == self.board[2][5] == self.player2.symbol:
                # player2 middle row wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[4][1] == self.board[4][3] == self.board[4][5] == self.player2.symbol:
                # player2 bottom row wins
                print(f"{self.player2.name} wins")
                self.game_on = False

            elif self.board[0][1] == self.board[2][1] == self.board[4][1] == self.player2.symbol:
                # player2 first column wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[0][3] == self.board[2][3] == self.board[4][3] == self.player2.symbol:
                # player2 second column wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[0][5] == self.board[2][3] == self.board[4][5] == self.player2.symbol:
                # player2 second column wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[0][1] == self.board[2][3] == self.board[4][5] == self.player2.symbol:
                # player2 diagonal wins
                print(f"{self.player2.name} wins")
                self.game_on = False
            elif self.board[0][5] == self.board[2][3] == self.board[4][1] == self.player2.symbol:
                # player2 diagonal wins
                print(f"{self.player2.name} wins")
                self.game_on = False
        return self.game_on

    def is_play_again(self):
        pass

    def end_game_message(self):
        pass

    def run_game(self):
        # algorithms to run the game
        print("game starts")
        self.display_board(self.board)
        self.determine_user_num_symbol()
        self.counter = 0
        while True:
            # player 1 move
            self.player1.make_move()
            print(f"\n")
            self.update_board(self.player1.position, self.player1.symbol)
            self.determine_winner(self.counter)
            if self.game_on == False:
                break
            else:
                self.counter += 1

            # player 2 move
            self.player2.make_move()
            print(f"\n")
            self.update_board(self.player2.position, self.player2.symbol)
            self.counter += 1
            self.determine_winner(self.counter)
            if self.game_on == False:
                break
            else:
                self.counter += 1


game_one = Game()
game_one.run_game()
