
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


