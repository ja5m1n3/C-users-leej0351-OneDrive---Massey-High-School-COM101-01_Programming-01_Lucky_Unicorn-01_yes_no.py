
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


print ("Program continues")
  