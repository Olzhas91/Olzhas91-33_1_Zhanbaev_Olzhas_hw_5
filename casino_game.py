import random
import configparser
from decouple import config

class CasinoGame:
    def __init__(self):
        self.slots = list(range(1, 31))
        self.money = self.get_initial_money()
        self.bet = 0

    def get_initial_money(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        return int(config['DEFAULT']['MY_MONEY'])

    def play(self):
        while True:
            self.print_money()
            self.get_bet()
            self.spin_slots()
            self.check_win()
            if not self.play_again():
                break
        self.print_result()

    def print_money(self):
        print(f'Your current money: ${self.money}')

    def get_bet(self):
        while True:
            try:
                self.bet = int(input('Place your bet: $'))
                if self.bet <= 0 or self.bet > self.money:
                    raise ValueError
                break
            except ValueError:
                print('Invalid bet. Please enter a valid amount.')

    def spin_slots(self):
        self.winning_slot = random.choice(self.slots)

    def check_win(self):
        if self.winning_slot == self.bet:
            self.money += self.bet * 2
            print('Congratulations! You won!')
        else:
            self.money -= self.bet
            print('Sorry, you lost.')

    def play_again(self):
        while True:
            choice = input('Do you want to play again? (y/n): ')
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                return False
            else:
                print('Invalid choice. Please enter "y" or "n".')

    def print_result(self):
        print(f'Game over. Your final money: ${self.money}')
        if self.money > 0:
            print("You're a winner!")
        else:
            print('You lost all your money. Better luck next time!')

game = CasinoGame()
game.play()