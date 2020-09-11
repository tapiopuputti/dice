import random

def dice_roll(sides:int, number_of_dice:int, modifier:int) -> int:
    """This function calculates dice rolls and gives the result

    Args:
        sides (int): number of sides in a die
        number_of_dice (int): how many dice will be rolled
        modifier (int): a modifier added to the dice roll

    Returns:
        int: final result of dice rolls and added modifier
    """
    print(f"You are rolling {number_of_dice}d{sides} dice with modifier {modifier}.")
    result = 1
    return result

def print_welcome():
    print("|----------------------------------|")
    print("|                                  |")
    print("|    Welcome to the Dice Roller!   |")
    print("|                                  |")
    print("|----------------------------------|\n")
    

print_welcome()
dice_roll(6, 2, -1)
#print(dice_roll.__doc__)