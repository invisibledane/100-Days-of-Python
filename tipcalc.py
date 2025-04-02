def invalid_attempt(error_msg, attempts):
    print(error_msg)
    attempts += 1

    return attempts

tip_dictionary = { 1:1.15, 2:1.2, 3: 1.25 }

checking = True
bill = 0
tip_percentage = 0
attempts = 1
total = 0

while checking and attempts < 6:
    try:
        bill = float(input('How much was the bill? '))
        tip_percentage = int(input("How much would you like to tip? 1 = 15%, 2 = 20%, 3 = 25% "))
        
        if tip_percentage in tip_dictionary:
            total = bill * tip_dictionary[tip_percentage]
            print(f"Your total after tip is: ${total}")
            checking = False
        else:
            attempts = invalid_attempt("That is not a valid tip selection", attempts)
    except ValueError as e:
        attempts = invalid_attempt("That is not a number", attempts)




input("\n Done. Press any key to continue ...")