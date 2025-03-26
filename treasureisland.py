import traceback

class game_helpers:
    def __init__(self):
        self.exitcode = '$exit'
        self.expositions = [
            "You exit your ship and see a path that branches in two directions.",
            "\n\nYou wander down a path lined by dense jungle foliage. You approach a river.",
            '''You wait and a row boat randomly floats down the river and drifts ashore. 
            Oddly convient. 
            You row to the opposite shore.
            You exit the boat and follow a path barred by a wall. There are two doors.''',
            '''You are greeted with treasure on the other side of the door. So. Much. Treasure. \nLike, a lot. You're rich.
            You immediately pay for a crew to get you out of there. You retire. Again, so rich. Because of the treasture.
            \n\nCongratulations.'''
            ]
        
        self.scenarios = [
            "Do you go left or right? (Type 'left' or 'right').",
            "Do you swim or wait? (Type 'swim' or 'wait')",
            "Do you open the red or blue door? (Type 'red' or 'blue')"
            ]
        
        self.possible_decisions = [
            ['left', 'right'],
            ['swim', 'wait'],
            ['red', 'blue']
            ]
        
        self.wise_decisions = [
            'left',
            'wait',
            'blue'
            ]

        self.consequences = [
            "You fall down a hole. It's a deep hole. Really deep. Lethally deep. \nSo lethal, in fact, that you die.",
            "You are eaten alive by a particularly vicious trout. \nYou die from eateness.",
            "You enter and are immediately immolated. With fire. Fiery fire. \nYou die."
            ]

    def isUserBehaving(self, inputtocheck):
        is_user_behaving = True

        try:
            if inputtocheck == '$exit':
                print("\n\nThe ghost of Dredd Pirate McStabface stabs you (wait for it) in the face with a rusty cutlass. You deserved it.")
                is_user_behaving = False
            else:
                print(f"You chose {inputtocheck}")
        except:
            self.report_error("isUserBehaving")
        
        return is_user_behaving
    
    def getUserChoice(self, question, acceptableanswers):
        output = self.exitcode
        iterator = 1
        validResponse = False

        try:
            while not validResponse and iterator < 4:
                userinput = str.lower(input(f"{question} "))

                for answer in acceptableanswers:
                    if userinput == str.lower(answer):
                        validResponse = True
                        output = userinput
                
                if not validResponse and iterator < 3:
                    print("Sigh. You either mistyped something or you're stupid. Either way, try again.")
                
                iterator += 1

        except:
            print("An error occurred.")
        
        
        return output
    def survival(self, user_decision, wise_decision, consequence):
        user_still_alive = True
        
        try:
            if user_decision == wise_decision:
                print("You chose wisely.")
            else:
                print(consequence)
                user_still_alive = False
        except:
            self.report_error("survival")

        return user_still_alive
    
    def print_intro(self):
        print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

    def report_error(self, method):
        print(f"An error occurred in {method}.")


# ========== The game is afoot ==========   
helper = game_helpers()
survival = True

'''
1. Left or right, right == fall into hole. ded
2. Swim or wait, swim == attacked by trout, ded
3. Which door, red or blue. Red == burned by fire, ded.
'''
iterator = 0

try:
    for exposition in helper.expositions:
        if survival and iterator < 3:
            print(exposition)
            decision = helper.getUserChoice(helper.scenarios[iterator], helper.possible_decisions[iterator])

            survival = helper.isUserBehaving(decision)
            if survival:
                survival = helper.survival(decision, helper.wise_decisions[iterator], helper.consequences[iterator])
                if survival: iterator += 1
        elif iterator == 3:
            print(exposition)
        else:
            exit
except:
    helper.report_error("main")

input("\nThe end. Press any key to exit ...")