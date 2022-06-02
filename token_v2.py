import random
tokens = ["unicorn", "horse", "zebra", "donkey"]

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,100):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        chosen = "horse / zebra"
        balance += 0.5

    print("Token: {}, Balance: ${}".format(chosen, balance))