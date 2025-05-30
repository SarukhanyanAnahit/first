user1_att = 5
user2_att = 5
used_numbers = []

def is_valid_number(number):
    return number.isdigit() and len(number) == 3

while user1_att > 0 and user2_att > 0:
    user1 = input("user1: ")
    if not is_valid_number(user1) or user1 in used_numbers:
        print("wrong input for user1 or number already used")
        user1_att -= 1
        continue
    used_numbers.append(user1)

    user2 = input("user2: ")
    if not is_valid_number(user2) or user2 in used_numbers:
        print("wrong input for user2.")
        user2_att -= 1
        continue

    if user1[-1] != '0' and user2[0] != user1[-1]:
        print(f"user2 must enter a number starting with {user1[-1]}")
        user2_att -= 1
        continue
    used_numbers.append(user2)

print("game over.")