import Game


if __name__ == "__main__":
    print("Welcome to Rock Paper scissors game")
    game = Game.RockPaperScissors()

    while True:
        game.play()
        a = input('Do you wan\'t to play again?\n').lower()
        if a == 'yes':
            continue
        else:
            print('Bye, hope to see you later!')
            break
