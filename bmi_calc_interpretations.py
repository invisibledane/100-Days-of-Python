import math

def print_error(attempts, is_type_error, exception_msg):
    if is_type_error: 
        print(f"Inproper input: {exception_msg}")
        attempts -= 1
    else: print(f"{exception_msg}")

    return attempts

def interpret_bmi(bmi, interpretation):
    print(f"Your bmi is {str(bmi)}. You are {interpretation}")

bmi_interpretation = [ 'underweight',
                      'health weight',
                      'overweight',
                      'obese' ]

running = True
attempts = 10
input_invalid = True
while running and attempts > 0:
    try:
        while input_invalid:
            height = int(input('What is your height in inches? '))
            weight = int(input('What is your weight in pounds? '))
            if height > 0 and weight > 0: input_invalid = False
            else:
                if height < 0:
                    height = int(input("Invalid height. Please enter your height as a number greater than zero."))
                if weight < 0:
                    weight = int("Invalid weight. Please enter your weight as a number greater than zero.")
                
        bmi = float(math.floor(height**2 / weight))
        print(f"Your BMI is: {str(bmi)}")

        '''
    underweight: BMI less than 18.5

    Healthy weight: BMI between 18.5 and 24.9

    Overweight: BMI between 25 and 29.9

    Obesity: BMI of 30 or higher.
    '''
        if bmi < 18.5:
            interpret_bmi(bmi, bmi_interpretation[0])
        elif bmi > 18.4 and bmi < 25:
            interpret_bmi(bmi, bmi_interpretation[1])
        elif bmi > 24.9 and bmi < 30:
            interpret_bmi(bmi, bmi_interpretation[2])
        else:
            interpret_bmi(bmi, bmi_interpretation[3])

        input("\nDone. Press any key to exit ...")
        running = False
    except TypeError as t:
        attempts = print_error(attempts, True, str(t))
    except Exception as e:
        print_error(attempts, False, str(e))

    
