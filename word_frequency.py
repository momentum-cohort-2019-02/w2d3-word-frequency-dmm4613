import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def normalize_text(text):
        """Given a text, lowercases it, removes all punct, and removes white space. 
        double space will become single space"""
        #will convert any weird letters to standard case english
        text = text.casefold()
        #this will state that all upper and lower case letters are valid
        valid_chars = string.ascii_letters + string.whitespace + string.digits
        
        #remove all punctuation
        new_text = ""
        for char in text:
            if char in valid_chars:
                new_text += char

        text = new_text
        text = text.replace("\n", " ")
        return text

def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""

    #call the file
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    #creates a list
    words = []
    for word in text.split(" "):
        #checks to see if a word actually is there
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    #sets the dictionary to the called function word_freq()
    words = word_freq(words)
    #changes the dictionary into a list. words.get calls the value of each key of the dictionary. Does so in reverse order
   
   # sorted will take the list called and make sure they are in order. words.get is a method that gets the value of the key of words. Reverse = True just checks to see if you want to sort backwards. It will swap the values in the list until they are ordered. Also creates a new list instead of a dictionary
    for word in sorted(words, key=words.get, reverse=True):
        #assign freq to the value of the key
        freq = words[word]
        symbolize_freq = ''
        index = 0
        #this loop will check to see if the index is less than the occurences of the value of the dictionary key
        while index < freq:
            #each pass the variable symbolize_freq will gain another '*'
            symbolize_freq += '*'
            index += 1
        #each {} is formatted to output a variable. They are assigned inside of each {} with a variable. The 'f' before each string calls this formatting. rjust(20) will adjust that string to the right by 20 characters.   
        print (f"'{word}'".rjust(20) + " | " + f"{symbolize_freq} {freq} times")


def word_freq(a_list):
    """Given a list, find all the times a word appears"""
    word_count = {}
    for word in a_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


#this if statement was given. It allows us to use the command line to run and find the text file as well as the program. 
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


