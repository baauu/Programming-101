########################################################################
##
## CS 101 Lab
## Program # 5
## Name: Jessi Bautista Espino
## Email: jbr75@umsystem.edu
##
## PROBLEM : Randomize some slots and then fide if there is a match
##
## ALGORITHM : 
##      Provided below 
## 
## ERROR HANDLING:
##      None found. 
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        user_input = input('Do you want to play again? ==> ')
        if user_input == 'Y' or user_input == 'YES':
            return True
        elif user_input == 'N' or user_input == 'NO':
            return False
        else: 
            print('You must enter Y/YES/N/NO to continue. Please try again. ')


def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    while True: 
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager < 0: 
            print('The wager amount must be greater than 0. Please enter again.')
            continue
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.')
            print(bank)
            continue
        elif 0 < wager <= bank: 
            return wager


def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''

    first_slot = random.randint(1,10)
    second_slot = random.randint(1,10)
    third_slot = random.randint(1,10) 

    return first_slot, second_slot, third_slot

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    if reela == reelb and reela == reelc:
        return 3
    elif reela == reelb or reelb == reelc or reela == reelc:
        return 2
    else:
        return 0


def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    while True: 
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank <0:
            print('Too low a value, you can only choose 1 - 100 chips')
        elif bank > 100: 
            print('Too high a value, you can only choose 1 - 100 chips')
        else: 
            return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 0:
        return wager * -1
    if matches == 2: 
        return (wager * 3) - wager 
    if matches == 3: 
        return (wager * 10) - wager


if __name__ == "__main__":

    playing = True
    while playing == True:

        bank = get_bank()
        starting_chips = bank
        chips_max = bank
        rounds = 0 

        while bank > 0:   # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

            chips_max = max(bank, chips_max)
            rounds += 1  
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()