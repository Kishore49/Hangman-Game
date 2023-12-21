import random
import datetime


print("\t\t\t\t\t\t♦ WELCOME TO THE HANGMAN GAME ♦")
print("\t\t\t\t\t♦ Guess the members of BTS & Blackpink  ♦\n")

artists = ["jisoo", "rose", "jennie", "lisa", "taehyung", "suga",
    "rapmonster" , "jhope", "jungkook", "jimin", "jin"]


# this function returns a super-hero name
def random_hero(artistslist):
    return random.choice(artistslist)


HANGMAN = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
          |
         ===''', '''
      +---+
      O   |
     /|\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\  |
     / \  |
         ===''']

turns = True
while turns:                                               # user enter the loop and enter name
    secret_hero = random_hero(artists)

    name = input("Enter your name: \n")
    print(f"Best of luck {name} !\n")
    turns = False
    time1 = datetime.datetime.now()                        # time starts to guess
    trail = 0
    fill_word = ""          # empty str
    words = set()           # empty set

    while trail <= 6:
        print(HANGMAN[0 + trail])   # initializing HANGMAN

        if trail == 6:
            print(f"You ran your trails, better luck next time! \nThe word was {secret_artist}.")
            exit()

        """
        comparing char in secret hero with char in fill word,
        only present char are adding to words(a empty list).
        """
        for letter in secret_hero:
            if letter in fill_word:
                words.add(letter)
                print(letter)
            else:
                print("_")

        # if len of words and secret hero is same, then consider user as a winner with time he\she took.
        if len(words) == len(set(secret_artist)):
            time2 = datetime.datetime.now()
            print(f"Congrats you got the word! '{secret_artist}'. "
                  f"You took {time2-time1} time to guess. \nYOU'RE WINNER! ")
            exit()

        user_guess = input("Please guess a letter: ").lower()

        """
        if user guess (letter or char) is not in secret hero,
        initialize trail.
        """
        if user_guess not in secret_artist:
            trail += 1
            print(f"wrong! {user_guess} is not in word. ")

        fill_word += user_guess   # initializing user guess to a empty str(fill word).
