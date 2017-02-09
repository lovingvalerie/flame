#write a Flame program!
#take in two names to 'predict' romantic compatability

def get_name(promt):
    """
    Prompts user for valid username as a string
    returns the string after checking it is valid
    """
    while True:
        name = promt
        name = name.lower().strip(' ')
        if not name.isalpha():
            print "Invalid name, please try again."
        else:
            return name

def get_list(str):
   """
   converts a string to a list
   """
   some_list = list(str)
   return some_list

def get_non_duplicate_list(player_list, match_list):
    """
    removes common chr between two list
    conccantonates them and returns a list of non duplicate chr
    """
    match_listcp = match_list[:]
    for chr in player_list:
        if chr in match_list:
            match_list.remove(chr)
            #print match_list
    for chr in match_listcp:
        if chr in player_list:
            player_list.remove(chr)
            #print player_list
    non_duplicates = player_list + match_list
    #print non_duplicates
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

def main():
    user_promt = raw_input("Your name please? :")
    match_promt = raw_input("Your crush's name? :")
    name = get_name(user_promt)
    match_name = get_name(match_promt)
    player_list = get_list(name)
    match_list = get_list(match_name)
    no_duplicates = get_non_duplicate_list(player_list, match_list)
    total_chr = total_remaining_chr(no_duplicates)
    compatability = get_compatability(total_chr)
    print_results(compatability)

main()

