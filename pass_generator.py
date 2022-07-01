import random

# total number of combinations possible is 5293955920339377119177015629247762262821197509765625
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*()_+"

all = lower + upper + numbers + special
passw = ""


def password(passw):
    for i in range(0, 5):
        passw += random.choice(all)
        
    return passw


def authquator(passw):
    for i in range(0, 16):
        passw += random.choice(all)
    

    return passw


# # for i in range(0, 8):
# #     index = random.randrange(0, len(all))
# #     passw += all[index]
# print(passw)
