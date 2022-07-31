from human import Human


class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board_new = [
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
        self.check_user_input(2)
        self.number_of_human_player = self.check_user_input(2)
        if self.number_of_human_player == 2:
            self.player1 = Human("Human Player 1")
            self.player2 = Human("Human Player 2")
        print(f"-----{self.player1.name} is choosing symbol-----")
        self.player1.choose_symbol()
        if self.player1.symbol == "X":
            self.player2.symbol == "O"
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

    def human_turn(self):
        pass

    def machine_turn(self):
        pass

    def dispay_updated_board(self):
        pass

    def determine_winner(self):
        pass

    def is_play_again(self):
        pass

    def end_game_message(self):
        pass

    def run_game(self):
        # algorithms to run the game
        print("game starts")
        self.display_board(self.board_new)
        self.determine_user_num_symbol()


game_one = Game()
game_one.run_game()
