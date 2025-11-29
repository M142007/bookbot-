
def num_words(entire_text):
    total_word_count = 0
    for word in entire_text.split():
        total_word_count += 1
    return total_word_count



def character_total(entire_text):
    lower_cased = entire_text.lower()
    words = lower_cased.split()
    character = {}
    
    for word in words:
        for letter in word:
                if letter in character:
                    character[letter] += 1
                else:
                    character[letter] = 1
    return character


def sort_on(items):
    return items["num"]


def sorted_list(letters):
    sorted_list = []
    for letter in letters:
        indie_dict = dict(char= letter, num = letters[letter])
        sorted_list.append(indie_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
          






