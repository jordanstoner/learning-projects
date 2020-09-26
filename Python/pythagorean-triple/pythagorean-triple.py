# pythagorean-triple
# Jordan Stoner
# September 2020

# Prompt:
# Pythagorean Triples Checker
# If you do not know how basic right triangles work, or what a Pythagorean Triple is read these articles on Wikipedia¹ ².
# Allows the user to input the sides of any triangle in any order.
# Return whether the triangle is a Pythagorean Triple or not.
# Loop the program so the user can use it more than once without having to restart the program.

def main():
    print('Please enter the side lengths'
    ' (e.g. 3, 4, 5):')
    sides = list(map(int, input(">").split(',')))
    
    if is_triple(sides):
        print(f"{sides} is a pythagorean triple")
    else:
        print(f"{sides} is NOT a pythagorean triple")
    main()

def is_triple(sides):
    sides.sort()
    a, b, c = sides
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
