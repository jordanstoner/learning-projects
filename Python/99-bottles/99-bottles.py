# 99-bottles
# Jordan Stoner
# September 2020

# Program prints the lyrics to the classic song while iterating through a range.

def bottles():
    for bottle_count in range(99, 0, -1):

        new_bottle_count = bottle_count - 1

        if bottle_count > 1 or bottle_count == 0:
            bottle_noun = 'bottles'
        else:
            bottle_noun = 'bottle'

        if new_bottle_count > 1 or new_bottle_count == 0:
            new_bottle_noun = 'bottles'
        else:
            new_bottle_noun = 'bottle'

        print(f"{bottle_count} {bottle_noun} of beer on the wall..."
              f"{bottle_count} {bottle_noun} of beer..."
              f"You take one down..."
              f"Pass it around..."
              f"{new_bottle_count} {new_bottle_noun} of beer on the wall!")


if __name__ == '__main__':
    bottles()
