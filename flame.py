#write a Flame program!
#take in two names to 'predict' romantic compatability

#prompts user for thier name
def get_player_name():
    while True:
        player_name = raw_input("Your name please? :")
        player_name = player_name.lower().strip(' ')
        if not player_name.isalpha():
            print "Invalid name, please try again."
        else:
            return player_name

#promts user for thier crush's name
def get_match_name():
    while True:
        match_name = raw_input(
            "Your crush's name?, don't worry I'll never tell. :"
        )
        match_name = match_name.lower().strip(' ')
        if not match_name.isalpha():
            print "Invalid name, please try again."
        else:
            return match_name

#converts a string to a list
def convert_to_list(str):
    str_as_list = list(str)
    return str_as_list

#convert_to_list to convert player_name to a list called player_list
def get_player_list(player_name):
    player_list = convert_to_list(player_name)
    return player_list

#convert_to_list to convert match_name to a list called match_list
def get_match_list(match_name):
    match_list = convert_to_list(match_name)
    return match_list

#combines both lists to get a list containing combined_characters
def get_combined_characters(list_1, list_2):
    combined_characters_list = list_1 + list_2
    return combined_characters_list

#removes duplicates by converting to set and then back to a list, returns a list with no duplicates
def remove_duplicates(some_list):
    some_list = set(some_list)
    some_list = list(some_list)
    return some_list

#returns # of total remianing characters
def total_remaining_chr(some_list):
    total_chr = len(some_list)
    return total_chr

def get_compatability_rating(total_chr):
    flame = list('flame') * 5
    compatability_rating =  flame[total_chr]
    return compatability_rating

#print get_compatability(7)

def compatability(compatability_rating):
    flame_dict = {'f' : 'friends', 'l' : 'lovers', 'a' : 'affection', 'm' : 'marriage', 'e' : 'enemies'}
    result = flame_dict[compatability_rating]
    return result

def print_results(compatability):
    print "You both are most compatible as " + compatability

print_results(compatability(get_compatability_rating(total_remaining_chr(remove_duplicates(get_combined_characters(get_player_list(get_player_name()), get_match_list(get_match_name())))))))




