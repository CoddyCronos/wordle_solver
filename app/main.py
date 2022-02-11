import random

def read_file(path):
    f = open(path, "r")
    words = [line.strip() for line in f]
    return words

def random_word(words):
    word = random.choice(words)
    return word

def check_letters(word, guess):
    word = list(word)
    guess = list(guess)
    answer = ""

    for l in range(len(word)):
        if word[l] == guess[l]:
            answer = answer + u'\U0001F7E9'
        else:
            answer = answer + u'\U0001F7E5'
    return answer

if __name__ == "__main__":
    words_path = "/Users/fjung/Documents/wordle_solver/data/words.txt"
    word_list = read_file(words_path)
    rand_word = random_word(word_list)
    print(rand_word)
    while True:
        guess = input("Enter your word: ")
        print(check_letters(rand_word, guess))
        if guess == rand_word:
            break
