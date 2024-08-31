import random 

user_wins = 0
bot_wins = 0
options = ['rock','paper','scissors']

while True:
    user = input('Choose Rock, Paper, Scissors or Q to quit. ').lower()
    if user == 'q':
        if user_wins > 0 or bot_wins > 0:
            if user_wins > bot_wins:
                print(f'Player wins {user_wins} to {bot_wins}!')
            elif user_wins == bot_wins:
                if user_wins == 1:
                    print(f'It\'s a draw with {bot_wins} point for everyone!')
                else:
                    print(f'It\'s a draw with {bot_wins} points for everyone!')
            else:
                print(f'Bot wins {bot_wins} to {user_wins}.')
        break
    
    if user not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    bot = options[random_number]

    if user == 'rock' and bot == 'scissors':
        print('You win! Bot chose scissors.\n')
        user_wins += 1
    elif user == 'paper' and bot == 'rock':
        print('You win! Bot chose rock.\n')
        user_wins += 1
    elif user == 'scissors' and bot == 'paper':
        print('You won! Bot chose paper.\n')
        user_wins += 1
    elif user == bot:
        print(f'Draw! Bot also chose {user}.\n')
    else:
        print(f'You lose! Bot chose {bot}\n')
        bot_wins += 1

print('Goodbye!')