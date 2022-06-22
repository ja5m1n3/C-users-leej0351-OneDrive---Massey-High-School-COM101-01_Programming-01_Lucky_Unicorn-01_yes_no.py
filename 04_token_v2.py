import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print ("*** Round #{} ***".format(rounds_played))
    print(rounds_played)
    balance -= 1
    print ("Balance: ", balance)
    print ()

    play_again = input(" Press Enter to play again " "or 'xxx' to quit")
tokens = ["unicorn", "horse", "zebra", "donkey"]

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,10):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add 4$ to balance)
    if 1 <= chosen_num <= 5: 
        chosen = "unicorn"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        # if the number is even, set the chosen
        # item to a horse
        chosen = "horse / zebra"
        balance -= 0.5
        # otherwise set it to a zebra
    print("You got a  {}. Your balance is "
          "${:.2f}".format(chosen, balance))

print()


print("Final Balance :${:.2f}".format(balance))