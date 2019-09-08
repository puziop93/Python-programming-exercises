'''
8) Rock Paper Scissors
Question
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
Solution
'''
import random
while True:
    user = input("What do you choose - rock, paper or scissors? ")
    randa = random.randint(0,2)
    if randa == 0:
        randa = "rock"
    elif randa == 1:
        randa = "scissors"
    elif randa == 2:
        randa = "paper"
    print('Your opponent chose the',randa)
    if (user == randa):
        print("It's a draw, You chose the same!")
    elif(user=='rock' and randa=='scissors') or (user =='scissors' and randa =='paper') or (user =="paper" and randa =="rock"):
        print('Congratulation! Your %s beats %s !' %(user, randa))
    else:
        print('You lose')
    user = input('do you want to play again? Y/N ')
    if user.lower() =='y': pass
    else:
        break
