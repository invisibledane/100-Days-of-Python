import random
import string
import math

class password_helper():
    def __init__(self):
        self.try_again_msg = "That is not a number, please try again."
        self.invalid_stop_msg = "That is not a valid response. Exiting."
        self.acceptable_yesno_entry_prompt = "Enter: 'yes', 'no', 'y' or 'n'"
        self.valid_yesno_selection = { 'yes':True, 'y':True,'no':False,'n':False }
        self.desired_character_prompts = ["Would you like to include letters? ",
                  "Would you like to include numbers?",
                  "would you like to include special characters?" ]
        self.password_character_types = { "letters":False, "numbers":False, "characters":False }
        self.long_character_type = 'none'
        self.desired_password_length = 0

    def get_desired_pass_length(self):
        password_length = -1
        attempts = 5
        checking = True

        while checking and attempts > 0:
            try:
                password_length = int(input('How long would you like your password? (Enter a number greater than 9.) '))
                if password_length > 9: checking = False
                else: 
                    print('Password length must be at least 10 characters.')
            except TypeError as e:
                self.invalid_response_prompt(attempts)
            except:
                print("An error occurred.")
            
            attempts -= 1
            
        return password_length

    def get_desired_char_types(self):
        try:
            self.password_character_types['letters'] = self.characters_to_include(self.desired_character_prompts[0])
            if self.password_character_types['letters'] == False: self.password_character_types.pop('letters')

            self.password_character_types['numbers'] = self.characters_to_include(self.desired_character_prompts[1])
            if self.password_character_types['numbers'] == False: self.password_character_types.pop('numbers')

            self.password_character_types['characters'] = self.characters_to_include(self.desired_character_prompts[2] )
            if self.password_character_types['characters'] == False: self.password_character_types.pop('characters')
        except Exception as e:
            print(f"an error occurred: {str(e.__traceback__)}")

    def generate_random_letter(self):
        random_ltr = random.choice(string.ascii_letters)

        return random_ltr

    def generate_random_number(self):
        random_num = random.randint(0, 9)
        return random_num
    
    def generate_random_letters(self, num_of_ltrs):
        ltr_list = []

        while num_of_ltrs > 0:
            ltr_list.append(self.generate_random_letter())
            num_of_ltrs -= 1

        return ltr_list
    
    def generate_random_numbers(self, num_of_nums):
        num_list = []

        while num_of_nums > 0:
            num_list.append(self.generate_random_number())
            num_of_nums -= 1

        return num_list
    
    def generate_random_character(self):
        random_char = random.choice(string.punctuation)

        return random_char
    
    def generate_random_characters(self, num_of_chars):
        char_list = []

        while num_of_chars > 0:
            char_list.append(self.generate_random_character())
            num_of_chars -= 1
        
        return char_list
    
    def characters_to_include(self, prompt):
        include_character = False
        checking = True
        attempts = 5
        
        while checking and attempts > 0:
            try:
                user_selection = str.lower(input(f"{prompt} {self.acceptable_yesno_entry_prompt} "))
                if user_selection in self.valid_yesno_selection:
                    include_character = self.valid_yesno_selection[user_selection]
                    checking = False
                else:
                    attempts -= 1
                    if attempts > 0:
                        print("Invalid selection. Please try again.")
                    else:
                        print("Invalid selection, exiting")
            except ValueError as e:
                attempts -= 1
                self.invalid_response_prompt(attempts)
                    
        
        return include_character

    def generate_password_characters(self):
        generated_password_characters = []

        self.long_char_type = random.choice(list(self.password_character_types.keys()))
        
        number_of_characters_to_generate = math.floor(self.desired_password_length / len(self.password_character_types))
        long_chars_to_generate = number_of_characters_to_generate + (self.desired_password_length % len(self.password_character_types))

        for value in self.password_character_types:
                match value:
                    case 'letters':
                        if value == self.long_char_type:
                            generated_password_characters += self.generate_random_letters(long_chars_to_generate)
                        else: 
                            generated_password_characters += self.generate_random_letters(number_of_characters_to_generate)
                    case 'numbers': 
                        if value == self.long_char_type:
                            generated_password_characters += self.generate_random_numbers(long_chars_to_generate)
                        else: 
                            generated_password_characters += self.generate_random_numbers(number_of_characters_to_generate)
                    case 'characters':
                        if value == self.long_char_type:
                            generated_password_characters += self.generate_random_characters(long_chars_to_generate)
                        else: 
                            generated_password_characters += self.generate_random_characters(number_of_characters_to_generate)
        
        return generated_password_characters
    
    def generate_randomized_password(self, generated_password_chars_list):
        shuffled_list = random.sample(generated_password_chars_list, len(generated_password_chars_list))
        randomized_password = self.convert_passlist_to_string(shuffled_list)

        return randomized_password

    def invalid_response_prompt(self, attempts):
        if attempts > 0:
            print(self.try_again_msg)
        else:
            print(self.invalid_stop_msg)
    
    def convert_passlist_to_string(self, password_char_list):
        password_str = ''
        for character in password_char_list:
            password_str = f"{password_str}{character}"

        return password_str
    
    def get_yesno_answer(self, prompt):
        response = False
        attempts = 5
        running = True

        while running and attempts > 0:
            user_input = input(f"{prompt} {self.acceptable_yesno_entry_prompt} ")
            if user_input in self.valid_yesno_selection:
                response = self.valid_yesno_selection[user_input]
                running = False
            else: 
                self.invalid_response_prompt(attempts)
                atempts -= 1
        
        return response

print('''
 ad8888888888ba
dP'         `"8b,
8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
8  8   8              """        """      ""    8b
8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  `"""'       ,d8""
Yb,         ,ad8"
 "Y8888888888P"
      
=================================================
=================================================
====                                         ====
==== Welcome to the Noskl password generator ====
====                                         ====
=================================================
=================================================
''')

running = True
attempts = 10
while running and attempts > 0:
    helper = password_helper()

    try:
        helper.desired_password_length = helper.get_desired_pass_length()
        helper.get_desired_char_types()
        generated_password_chars = helper.generate_password_characters()

        '''
        prompt = ["Would you like to include letters? ",
                  "Would you like to include numbers?",
                  "would you like to include special characters?" ]
        
        password_character_types['letters'] = helper.characters_to_include(helper.desired_character_prompts[0])
        if password_character_types['letters'] == False: password_character_types.pop('letters')

        password_character_types['numbers'] = helper.characters_to_include(helper.desired_character_prompts[1])
        if password_character_types['numbers'] == False: password_character_types.pop('numbers')

        password_character_types['characters'] = helper.characters_to_include(helper.desired_character_prompts[2] )
        if password_character_types['characters'] == False: password_character_types.pop('characters')

        helper.long_char_type = random.choice(list(password_character_types.keys()))
        generated_password = []
        number_of_characters_to_generate = math.floor(desired_pass_length / len(password_character_types))
        character_countdown = 0
        
 
        for value in password_character_types:
            if value == long_char_type:
                character_countdown = number_of_characters_to_generate + (desired_pass_length % len(password_character_types))
                match value:
                    case 'letters':
                        generated_password += helper.generate_random_letters(character_countdown)
                    case 'numbers': 
                        generated_password += helper.generate_random_numbers(character_countdown)
                    case 'characters':
                        generated_password += helper.generate_random_characters(character_countdown)
            else:
                match value:
                    case 'letters':
                        generated_password += helper.generate_random_letters(number_of_characters_to_generate)
                    case 'numbers': 
                        generated_password += helper.generate_random_numbers(number_of_characters_to_generate)
                    case 'characters':
                        generated_password += helper.generate_random_characters(number_of_characters_to_generate)
        '''
        pass_string = helper.generate_randomized_password(random.sample(generated_password_chars, len(generated_password_chars)))
        print(f"Your password is: {pass_string}")
       
        running = helper.get_yesno_answer("Finished. Would you like to create another password?")
        if running:
            helper = None
            attempts = 10
    except ValueError as e:
        print("That was not a letter or word.")
    except Exception as e:
        print(e)

input("Done. Press any key to continue ...")