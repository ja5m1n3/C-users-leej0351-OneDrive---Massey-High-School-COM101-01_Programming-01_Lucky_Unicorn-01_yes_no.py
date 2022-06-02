
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

# Main rountine goes here...
show_instructions = yes_no("Would you like to see the instructions ")

if show_instructions == "yes":
   instructions()


how_much = num_check("How much would you like to play with? ", 0, 10 )
print ("You will be spending ${}".format(how_much))
  