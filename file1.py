import random

fruits=['apple','apricot','avocado','banana','blackberry','blackcurrant','blueberry',
'boysenberry','cherry','coconut','fig','grape','grapefruit','kiwifruit','lemon',
'lime','lychee','mandarin','mango','melon','nectarine','orange','papaya','passion fruit',
'peach','pear','pineapple','plum','pomegranate','quince','raspberry','strawberry',
'watermelon']

def getWord(l):
    word=random.choice(l)
    return word.upper()

def play(word):
    word_completion='_ '*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print("Let's start")
    print(tries)
    print(word_completion)
    while not guessed and tries >0:
        guess = input("take a guess: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess," is not in the word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("That's great..",guess," is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_ " not in word_completion:
                    guess=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word",guess)
            elif guess !=word:
                print(guess,"is not the correct word")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_completion=word
        else:
            print("Not a valid guess..")
        print(tries)
        print(word_completion)
        print("\n")
    if guessed:
        print("Yeahh!! you did it")
    else:
        print("sorry, you ran out of tries. The correct word was ",word,"Better luck next time!!")



def main():
    print("WELCOME TO HANGMAN!!")
    print("1: Fruits")
    choice=int(input("Enter Choice: "))
    if(choice==1):
        print("fruit chosen")
        word=getWord(fruits)
        play(word)
    while input("Play Again?? (Y/N) ").upper() =="Y":
        print("WELCOME TO HANGMAN!!")
        print("1: Fruits")
        choice=int(input("Enter Choice: "))
        if(choice==1):
            print("fruit chosen")
            word=getWord(fruits)
            play(word)

if __name__=="__main__":
    main()


