import random

words = None
difficulty = None
ranking = list()

DIFFICULTY_SETTING = {
    "easy": {'maxLength':4},
    'medium': {'minLength':5, 'maxLength':6},
    'hard': {'minLength':7}
}

def choose_difficulty():
    global difficulty
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            difficulty = difficulty
            return
        else:
            print("Invalid input. Please enter 'easy', 'medium' or 'hard'.")

def get_word():
    min_len = DIFFICULTY_SETTING[difficulty].get("minLength", float("-inf"))
    max_len = DIFFICULTY_SETTING[difficulty].get("maxLength", float("inf"))
    
    while True:
        word = random.choice(words).lower()
        if min_len <= len(word) <= max_len:
            return word

def game():
    global ranking
    
    word = get_word()
    print(word)
    guessed = "_" * len(word)
    guessed = list(guessed)
    lstguessed = []
    
    tries = 6
    while tries > 0:
        print("\nCurrent word: ", " ".join(guessed))
        lstguessed.sort()
        print("Guessed letters: ", " ".join(lstguessed))
        print(f"Incorrect guesses remaining: {tries}")
        letter = input("Guess a letter: ").lower()

        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single letter.")
        elif letter in lstguessed:
            print("Already guessed!!")
        elif letter not in word:
            tries -= 1
            print(f"Sorry, '{letter}' is not in the word.")
            lstguessed.append(letter)
        else:
            print(f"Good job! '{letter}' is in the word.")
            lstguessed.append(letter)
            for i in range(len(word)):
                if letter == word[i]:
                    guessed[i] = letter

        if "_" not in guessed:
            print(f"Congratulations! You guessed the word!: {word}\n")

            if input("Do you want to save your score? (yes/no): ").lower() == "yes":
                name = input("Please enter your name: ")
                ranking.append({"name": name, "tries": tries, "word": word})
                ranking = sorted(ranking, key=lambda k: k["tries"], reverse=True)
                ranking = ranking[:5]

                print("\nTop 5 ranking:")
                for i, player in enumerate(ranking):
                    print(f"{i+1}. {player['name']} with {player['tries']} tries left. Word: {player['word']}")
            break
    else:
        print(f"You ran out of tries. The word was {word}\n")

def main():
    global words
    # load words from file
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    
    # Run game
    print("Welcome to Hangman!")
    while True:
        choose_difficulty()
        game()
        if input("\nDo you want to play again? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
        