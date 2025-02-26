import random


class RockPaperScissors:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.game_options = ['human-easy', 'human-medium', 'human-hard', 'human-very_hard']
        self.winning_op = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        self.comp_wins = 0
        self.human_wins = 0
        self.human_2_wins = 0
        self.user_choice = None
        self.l_user_choice = None
        self.comp_choice = None
        self.game_round_nf = True

    def win_finder_ai(self):
        """Checks winner for Human vs. AI mode."""
        if self.comp_wins == 5 or self.human_wins == 5:
            if self.comp_wins == 5:
                print('Computer wins!')
                self.game_round_nf = False
            else:
                print('You won!')
                self.game_round_nf = False
            self.comp_wins = 0
            self.human_wins = 0
            return  # Exit function when someone wins

        winning = self.winning_op
        com = self.comp_choice
        user = self.user_choice

        if winning[com] == user:
            self.comp_wins += 1
            print(f'{com} - Computer wins this round!')
        elif winning[user] == com:
            self.human_wins += 1
            print(f'{com} - You win this round!')
        else:
            print(f'Draw {com} - {user}')


    def easy(self):
        while self.game_round_nf:
            print(self.options)
            self.user_choice = input('What it your choice.\n')
            if self.user_choice in self.options:
                self.comp_choice = random.choice(self.options)
            else:
                print('Check spelings')
                continue
            self.win_finder_ai()

    def medium(self):
        while self.game_round_nf:
            print(self.options)
            self.user_choice = input('What it your choice.\n')
            if self.user_choice in self.options:
                if self.user_choice and random.random() < 0.5:
                    self.comp_choice = self.winning_op[self.l_user_choice]
                else:
                    self.comp_choice = random.choice(self.options)
            else:
                print('Check spelings')
                continue
            self.win_finder_ai()

    def hard(self):
        while self.game_round_nf:
            print(self.options)
            self.user_choice = input('What it your choice.\n')
            if self.user_choice in self.options:
                self.l_user_choice = self.user_choice
                if self.l_user_choice:
                    self.comp_choice = self.winning_op[self.l_user_choice]
                self.comp_choice = 'scissors'
            else:
                print('Check spelings')
                continue
            self.win_finder_ai()

    def very_hard(self):
        while self.game_round_nf:
            print(self.options)
            self.user_choice = input('What it your choice.\n')
            if self.user_choice in self.options:
                self.comp_choice = self.winning_op[self.user_choice]
                self.win_finder_ai()
            else:
                print('Check spelings')
                continue

    def play(self):
        print(' '.join(self.game_options))
        a = input('Which mode do you wan\'t to play in.(very_hard is imposible to win)\n').lower()
        self.game_round_nf = True
        if a in self.game_options:
            if a == 'human-easy':
                print('Playing in easy mode!')
                self.easy()
            elif a == 'human-medium':
                print('Playing in medium mode!')
                self.medium()
            elif a == 'human-hard':
                print('Plaing in hard mode!')
                self.hard()
            else:
                print('Plaing in very hard mode!')
                self.very_hard()
