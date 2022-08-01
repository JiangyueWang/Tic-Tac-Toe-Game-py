class Human():

    def __init__(self, name):
        self.name = name
        self.symbol = ""
        self.position = 0

    def choose_symbol(self):
        while True:
            self.user_input = input("Do you want to be 'X' or 'O'?\n")
            if self.user_input == 'X' or self.user_input == "x":
                self.symbol = 'X'
                break
            elif self.user_input == 'O' or self.user_input == 'o':
                self.symbol = 'O'
                break
            else:
                print("Check your entry, select again")

    def make_move(self):
        while True:
            self.position = input(
                f"{self.name} please enter 1 to 9 to represent the postion you want to place your symbol:\n")
            try:
                self.position = int(self.position)
                if self.position not in range(0, 10):
                    print(f"Check your input, try again\n")
                    continue
                else:
                    break
            except ValueError:
                print(f"Must be a valid integer, try again\n")
                continue


# human_one = Human("Human 1")
# human_one.choose_symbol()
# human_one.make_move()
