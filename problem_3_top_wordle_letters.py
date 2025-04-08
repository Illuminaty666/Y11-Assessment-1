import requests

# You can ignore how this function works, it's just used to get the list of words in all_words above
def get_valid_wordle_words():
    str_words = []
    words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words") \
                        .content
    words = words_text.split()
    for word in words:
        str_words.append(str(word.decode('ascii')))
    return str_words

def letter_freq(words, letter):
    freq = {}
    for word in words:
        count = word.lower().count(letter.lower())
        freq[word] = count
    return freq

def find_most_used_letter(freq):
    most_used_letter = max(freq, key=freq.get)
    return most_used_letter, freq[most_used_letter]

wlist = get_valid_wordle_words()
letter_to_count = input("Desired letter to count: ")

freq = letter_freq(wlist, letter_to_count)
most_used_letter, count = find_most_used_letter(freq)

print(f"The most used letter '{most_used_letter}' occurs {count} times.")

# all_words will contains a list of all valid words that you can use
all_words = get_valid_wordle_words()






