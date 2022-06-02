
# Funtions go here...
def yes_no(question):
    valid = False
    while not valid:   

        response = input (question) .lower()     

        # If they day yes, output 'program continues' 
        if response == "yes" or response == "y":
            return "yes"

        elif response ==  "no" or response == "n":
            return "no"

        # If they say no, output 'display instructions'
        else :
            print ("Please answer yes / no")

        
# Main rountine goes here...
show_instructions = yes_no("Have you played this game before ")
like_CS = yes_no("Do you like CS? ")
print("You said ", like_CS)
