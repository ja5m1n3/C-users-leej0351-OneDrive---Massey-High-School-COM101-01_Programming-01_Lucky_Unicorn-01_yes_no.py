import random


# Funtions go here...
def yes_no(question):
    valid = False
    while not valid:   

        response = input (question).lower()     

        # If they day yes, output 'program continues' 
        if response == "yes" or response == "y":
            return "yes"

        elif response ==  "no" or response == "n":
            return "no"

        # If they say no, output 'display instructions'
        else :
            print ("Please answer yes / no")


def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:

                return response
            # output an error
            else:
                print(error)

        except ValueError:
            print(error) 

def instructions():
    print("""

**** Instructions ******

Pay $1 per round.  Winnings as follows...
- Unicoron: $5
- Horse: $0.50
- Zebra: $0.50
- Donkey: $0.00

Can you beat the bank?


    """)


def statement_generator(statement, decoration):

    sides = "*" * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main rountine goes here...
show_instructions = yes_no("Would you like to see the instructions ")

if show_instructions == "yes":
   instructions()


how_much = num_check("How much would you like to play with? ", 0, 10 )
print ("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    print()
    # Print round number
    print ("*** Round #{} ***".format(rounds_played))


    # decide on winnings!
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add 4$ to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "@"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1
    else:
        # if the number is even, set the chosen
        # item to a horse
        chosen = "horse / zebra"
        decoration = "+"
        balance -= 0.5
        # otherwise set it to a zebra
    feedback = "You got a  {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(feedback, decoration)


    if balance <1:
        play_again = "xxx"
        statement_generator("Sorry you have run out of money", "!")

    else:
        play_again = input("Press Enter to play again " "or 'xxx' to quit")
