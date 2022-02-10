import random

def read_file(path):
    f = open(path, "r")
    words = [line.strip() for line in f]
    return words

def random_word(words):
    word = random.choice(words)
    return word

if __name__ == "__main__":
    words_path = "/Users/fjung/Documents/wordle_solver/data/words.txt"
    word_list = read_file(words_path)
    rand_word = random_word(word_list)
    print(rand_word)
