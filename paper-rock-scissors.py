import random

class game_helpers:
    def __init__(self):
        self.error_code = "^error"
        self.rock_paper_scissor_dict = { 0:"rock", 
                                        1:"paper", 
                                        2:"scissor" }
        self.rock_paper_scissors_acceptable = [
            'rock', 
            'paper', 
            'scissor', 
            'r', 
            'p', 
            's' ]
        
        self.loss_criteria = {
            'paper':'scissor',
            'rock':'paper',
            'scissor':'rock',
            'p':'scissor',
            'r':'paper',
            's':'rock'
        }

    def get_user_input(self, prompt_text, acceptable_answers):

        getting_input = True
        attempts = 1
        user_input = self.error_code

        try:
            while getting_input and attempts < 4:
                user_input = str.lower(input(prompt_text))

                if user_input in acceptable_answers:
                    print(f"You chose '{user_input}'")
                    getting_input = False
                else:
                    print("That's not what I asked for. Try again.")
                    attempts += 1
        except:
            self.print_error("get_user_input", "error")
        
        return user_input

    def print_error(self, method_name, error):
        print(f"An error occured in {method_name}. \nError: {error}")
    
    def is_user_behaving(self, user_input):
        is_user_behaving = False

        if user_input == self.error_code:
            print("I guess you don't want to play. Bye.")
        else:
            is_user_behaving = True

        return is_user_behaving
    
    def determine_winner(self, user_selection, sys_selection):

        winner = 'player'
        outcome_statement = f"I chose {sys_selection}"

        if self.loss_criteria[user_selection] == sys_selection:
            print(f"You won! {outcome_statement}")
        elif self.loss_criteria[sys_selection] == user_selection:
            print(f"You lost! I chose {outcome_statement}")
        else:
            print(f"It was a draw! {outcome_statement}")

        

def main():
    helper = game_helpers()

    playing = True

    while playing:
        print("Let's play some rock paper scissors!")

        rockpaperscissorsprompt = "Enter rock or r, paper or p, scissors or s "

        user_choice = helper.get_user_input(rockpaperscissorsprompt, helper.rock_paper_scissors_acceptable)

        if not helper.is_user_behaving(user_choice):
            playing = False
        else: 
            system_selection = helper.rock_paper_scissor_dict[random.randint(0, 1)]
            helper.determine_winner(user_choice, system_selection)
            playing = False


main()          

input("Press any key to exit ...")