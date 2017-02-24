#write a Flame program!
#take in two names to 'predict' romantic compatability

from prompt import user_prompt
from prompt import match_prompt

def get_name(prompt):
    """
    Prompts user for valid name as a string
    returns the string after checking it is valid
    """
    while True:
        name = raw_input(prompt)
        name = name.lower().strip(' ').replace(" ", "")
        print name
        if not name.isalpha():
            print "Invalid name, please try again."
        else:
            return name
    return name

def get_list(str):
   """
   converts a string to a list
   """
   some_list = list(str)
   return some_list

def get_non_duplicate_list(player_list, match_list):
    non_duplicates = []
    for chr in player_list:
        if not chr in match_list:
            non_duplicates.append(chr)
    for chr in match_list:
        if not chr in player_list:
            non_duplicates.append(chr)
    return non_duplicates

def total_remaining_chr(non_duplicates):
    """
    returns len of a list
    """
    total_chr = len(non_duplicates)
    #print total_chr
    return total_chr

def get_compatability(total_chr):
    """
    returns list element via index
    """
    flame = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies'] * 5
    compatability = flame[total_chr -1]
    #print compatability
    return compatability

def print_results(compatability):
    """
    concatanates a promt and a result str
    """
    print "You both are most compatible as " + compatability

def play_the_game(user_name, match_name):
    player_list = get_list(user_name)
    match_list = get_list(match_name)
    print_results(get_compatability(total_remaining_chr(get_non_duplicate_list(player_list, match_list))))

def play_game(input=False):
    if input:
        play_the_game(get_name(user_prompt), get_name(match_prompt))
    else:
        # play the game some other way like on the web
        pass


def main():
    play_the_game(get_name(user_prompt), get_name(match_prompt))
main()

