

# Funtions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input ("Have you played this game before? ").lower()
response = ""
while response.lower() != "xxx":
    # Ask the user if they have played before 
    response = input ("Have you played this game before? ") .lower()

    # If they day yes, output 'program continues' 
    if response == "yes" or response == "y":
        response = "yes"
        print ("program continues")

    elif response ==  "no" or response == "n":
        print ("display instructions")

    # If they say no, output 'display instructions'
    else :
        print ("Please answer yes / no")

    # print("Display instructions")
        
# Main rountine goes here...