import math

def print_error(attempts, is_type_error, exception_msg):
    if is_type_error: 
        print(f"Inproper input: {exception_msg}")
        attempts -= 1
    else: print(f"{exception_msg}")

    return attempts

running = True
attempts = 10
while running and attempts > 0:
    try:
        height = int(input('What is your height in inches? '))
        weight = int(input('What is your weight in pounds? '))
        print(f"Your BMI is: {str(math.floor(height**2 / weight))}")

        input("\nDone. Press any key to exit ...")
        running = False
    except TypeError as t:
        attempts = print_error(attempts, True, str(t))
    except Exception as e:
        print_error(attempts, False, str(e))

    