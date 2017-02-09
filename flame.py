#write a Flame program!
#take in two names to 'predict' romantic compatability

def get_player_name():
    """
    Prompts user for valid username as a string
    returns the string after checking it is valid
    """
    while True:
        player_name = raw_input("Your name please? :")
        player_name = player_name.lower().strip(' ')
        if not player_name.isalpha():
            print "Invalid name, please try again."
        else:
            return player_name

def get_match_name():
    """
    promts user for valid username as a string
    returns the string after checking it is valid
    """
    while True:
        match_name = raw_input(
            "Your crush's name? :"
        )
        match_name = match_name.lower().strip(' ')
        if not match_name.isalpha():
            print "Invalid name, please try again."
        else:
            return match_name

def get_player_list(name):
   """
   converts player_name to a list
   """
   player_list = list(name)
   return player_list

def get_match_list(match_name):
    """
    convert match_name to list
    """
    match_list = list(match_name)
    return match_list

def get_non_duplicate_list(player_list, match_list):
    """
    removes common chr between two list
    concatanatest them and returns a list of non duplicate chr
    """
    match_listcp = match_list[:]
    for chr in player_list:
        if chr in match_list:
            match_list.remove(chr)
            print match_list
    for chr in match_listcp:
        if chr in player_list:
            player_list.remove(chr)
            print player_list
    non_duplicates = player_list + match_list
    print non_duplicates
    return non_duplicates

def total_remaining_chr(non_duplicates):
    """
    returns len of a list
    """
    total_chr = len(non_duplicates)
    print total_chr
    return total_chr

def get_compatability(total_chr):
    """
    returns list elementi of a list
    """
    flame = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies'] * 5
    compatability = flame[total_chr -1]
    print compatability
    return compatability

def print_results(compatability):
    """
    concatanates a promt and a result str
    """
    print "You both are most compatible as " + compatability

def main():
    name = get_player_name()
    match_name = get_match_name()
    player_list = get_player_list(name)
    match_list = get_match_list(match_name)
    no_duplicates = get_non_duplicate_list(player_list, match_list)
    total_chr = total_remaining_chr(no_duplicates)
    compatability = get_compatability(total_chr)
    print_results(compatability)

main()

