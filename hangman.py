import random

mistakes = [ '  O',
            '''  O
-''',
'''  O
--''',
'''  O
--|''',
'''  O
--|-''',
'''  O
--|--''',
'''  O
--|--
 /''',
'''  O
--|--
 / \\''']

word_list = [ 'angle',  'bread', 'corn', 'dare', 'earth', 'food', 'great', 
             'height', 'igloo', 'just', 'keep', 'loft', 'main', 'need', 'orbit','pride',
             'road', 'stove', 'trust', 'under', 'very', 'water', 'xerox', 'yonder', 'zebra' ]

running = True
mistakes = 0
test_runs = 10
while running:
    goal_word = word_list[random.randint(0, len(word_list)- 1)]
    print(goal_word)

    spaces = len(goal_word)
    print(goal_word)
    goal_word_spaces = ''
    while spaces > 0:
        goal_word_spaces += '-'
        spaces -= 1
    print(goal_word_spaces)
    running = False

input('\nPress any key to close.')