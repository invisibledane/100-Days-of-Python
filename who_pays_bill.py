import random

people = ['Bill', 'Jim', 'Jane', 'Christina', 'Riley']

# Choose, at random, someone to pay the bill
random_selection = random.randint(0, len(people) - 1)

print(people[random_selection])

input('Done, I think. Press any key to close.')