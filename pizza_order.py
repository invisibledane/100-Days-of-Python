class pizza_helper():
    def __init__(self):
        self.pizza_size_prices = { "small":15, "medium":20, "large":25 }
        self.pizza_size_index = {'s':"small", 'small':"small", 
                                 'm':"medium", 'medium':"medium", 
                                 'l':"large", 'large':"large" }
        self.pepperoni_prices = { "small":2, "medium":3, "large":3 }
        self.yes_no_valid_response = ['yes', 'y', 'no', 'n' ]
        self.extra_cheese = 1
        self.pizza_price = 0

    def order_pizza_size(self):
        try:
            pizza_size = self.pizza_size_index[self.get_user_input("Which size would you like? s/small, m/medium, l/large?", 
                                             "Please choose an appropriate size.", self.pizza_size_index, 5)]
        except Exception as e:
            print(str(e))

        return pizza_size
    
    def order_pepperoni(self):
        add_pepp = self.get_yesno_answer_as_truefalse("Would you like pepperoni?", 5)
        
        return add_pepp
    
    def order_extra_cheese(self):
        add_extra_cheese = self.get_yesno_answer_as_truefalse("Would you like extra cheese?", 5)

        return add_extra_cheese

    def notify_invalid_selection(self, prompt, attempts):
        print(f"Invalid selection, {prompt}")
        attempts -= 1

        return attempts

    def get_user_input(self, prompt, invalid_entry_prompt, acceptable_input, total_attempts):

        running = True
        try: 
            while running and total_attempts > 0:
                user_input = str.lower(input(f"{prompt} "))

                if user_input not in acceptable_input:
                    total_attempts = self.notify_invalid_selection(invalid_entry_prompt, total_attempts)
                else: running = False
        except Exception as e:
            print(str(e))

        return user_input
    
    def get_yesno_answer_as_truefalse(self, prompt, attempts):
        try:
            extra_cheese = False

            running = True
            while running and attempts > 0:
                response = str.lower(input(f"{prompt} Enter yes/y, no/n. "))

                if response in self.yes_no_valid_response:
                    if response == 'yes' or response == 'y':
                        extra_cheese = True
                    running = False
                else:
                    attempts = self.notify_invalid_selection("Invalid response", attempts)

                return extra_cheese

        except Exception as e:
            print(str(e))

    def give_final_cost(self):
        print(f"You order will be ${self.pizza_price}")

    def order_pizza(self):
        pizza_size = self.order_pizza_size()
        self.pizza_price += self.pizza_size_prices[pizza_size]
        if self.order_pepperoni(): 
            self.pizza_price += self.pepperoni_prices[pizza_size]
        if self.order_extra_cheese(): self.pizza_price += 1
        self.give_final_cost()

# Run script
running = True
while running:
    helper = pizza_helper()
    helper.order_pizza()

    if helper.get_yesno_answer_as_truefalse("Run again?", 1):
        helper = None
    else:
        running = False
        input("Done. Press any key to close.")
    
        