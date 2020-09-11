import random

def dice_roll(number_of_dice:int, sides:int, modifier:int) -> int:
    """This function calculates dice rolls and gives the result

    Args:
        sides (int): number of sides in a die
        number_of_dice (int): how many dice will be rolled
        modifier (int): a modifier added to the dice roll

    Returns:
        int: final result of dice rolls and added modifier
    """
    print(f"You are rolling {number_of_dice}d{sides} dice with modifier {modifier}.")
    
    result = 0

    for x in range(number_of_dice):
        roll = random.randint(1,sides)
        print(f"Your {x+1}. roll: {roll}")
        result += roll

    print(f"Added modifier: {modifier}")

    return result + modifier

def print_welcome():
    """This method prints a welcome screen.
    """
    print("|----------------------------------|")
    print("|                                  |")
    print("|    Welcome to the Dice Roller!   |")
    print("|                                  |")
    print("|----------------------------------|\n")

def user_input():
    """This function asks the user for inputs:
    1. input: how many dice.
    2. input: what type of die (i.e. how many sides in the die).
    3. input: modifier added to the total result.

    Returns:
        int, int, int: as above
    """
    number_of_dice = int(input("Please enter the number of dice you want to roll: "))
    type_of_dice = int(input("Please enter the type of die you want to roll: "))
    modifier = int(input("Please enter a modifier to be added to your dice roll: "))
    return number_of_dice, type_of_dice, modifier

print_welcome()

dice_parameters = user_input()
print(dice_parameters)
roll_result = dice_roll(dice_parameters[0], dice_parameters[1], dice_parameters[2])

print(f"Your total dice roll result: {roll_result}")
