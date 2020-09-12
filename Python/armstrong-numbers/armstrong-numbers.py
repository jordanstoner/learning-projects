# armstrong-numbers
# Jordan Stoner
# September 2020

# Prompt:
# Learn about armstrong numbers here.
# Define a function that allows the user to check whether a given number is armstrong number or not.
# Hint: To do this, first determine the number of digits of the given number. Call that n. 
# Then take every digit in the number and raise it to the nth power. 
# Add them, and if your answer is the original number then it is an Armstrong number.
# Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. 
# So 1634 is an Armstrong number.
# Tip: All single digit numbers are Armstrong numbers.

def main():
    user_number = input("Enter a number, and see if it is an Armstrong number!: ")

    if armstrong(user_number):
        print (f"{user_number} is an Armstrong number!")
    else:
        print (f"Sorry, {user_number} is not an Armstrong number...")


def armstrong(input_number):
    length = len(input_number)
    sum = 0

    for digit in range(length):
        number = int(input_number[digit])
        number **= length
        sum += number
    
    if sum == int(input_number):
        return True
    else:
        return False


if __name__ == "__main__":
    main()