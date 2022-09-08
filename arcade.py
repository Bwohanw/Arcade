import calculatorgame
import hangman
import ticTacToe
import wordle
import numberguesser
import guessing
import time

def main():
    print("Here are the selection of available games: ")
    time.sleep(1)
    print("Press 1 to play the Calculator Game")
    print("Press 2 to play Hangman")
    print("Press 3 to play scalable Tic-Tac-Toe")
    print("Press 4 to play Wordle (not trademarked)")
    print("Press 5 to play a Number Guessing game")
    print("Press 6 to play the Cup guessing game")
    print("If you don't know how to play some of these, that's fine! The rules will be explained within each game.")
    while True:
        arg = input("Which game would you like to play? Or press 0 if you've found youself here by mistake. ").strip()
        match arg:
            case "0":
                return
            case "1":
                calculatorgame.main()
            case "2":
                hangman.main()
            case "3":
                ticTacToe.main()
            case "4":
                wordle.main()
            case "5":
                numberguesser.main()
            case "6":
                guessing.main()
            case default:
                print("I can't seem to find that one here, sorry")
                continue
        break




if __name__ == '__main__':
    print("Welcome to the arcade! We have a wide selection of games for you!")
    time.sleep(1)
    print("It's just that none of them have any user interface but don't pay attention to that, we have Wordle!")
    time.sleep(1)
    print("(not sponsored by the New York Times maybe don't tell them we have it)")
    time.sleep(1)
    print("Anyways, enjoy your stay!")
    time.sleep(1)
    while True:
        main()
        time.sleep(.5)
        q = input("Would you like to play another game? Y/N ").strip().upper()
        if (q != "Y"):
            break