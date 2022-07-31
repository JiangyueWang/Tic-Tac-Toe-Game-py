class Human():

    def __init__(self, name):
        self.name = name
        self.symbol = ""
        self.position = 0

    def choose_symbol(self):
        while True:
            self.user_input = input("Do you want to be 'X' or 'O'?").upper()
            if self.user_input == 'X':
                self.symbol = 'X'
                break
            elif self.user_input == 'O':
                self.symbol = 'X'
                break
            else:
                print("Check your entry, select again")

    def make_move(self):
        pass
