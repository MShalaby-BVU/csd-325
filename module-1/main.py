"""
Michael Shalaby
9/11/2025
Assignment 1.3

This code displays the "bottle of beer" song, with the number of bottles being a user input.
"""

def bottle_word(bottle_count):
    return "bottle" if bottle_count == 1 else "bottles"
def beer(initial_count):
    for i in range(initial_count, 0, -1):
        print(f"{i} {bottle_word(i)} of beer on the wall, {i} {bottle_word(i)} of beer.")
        print(f"Take one down, pass it around, {i - 1} {bottle_word(i-1)} of beer on the wall.")
    print("Time to buy more beer.")
def main():
    try:
        while True:
            beer(int(input("\nHow many bottles of beer are on the wall?\n")))
    except ValueError:
        print("Please enter a valid number.")
        main()

if __name__ == "__main__":
    main()
