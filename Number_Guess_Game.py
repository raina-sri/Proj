winning_number=3
guessed_number=input("guess a number between 1 to 10 : ")
guessed_number=int(guessed_number)
if winning_number==guessed_number:
    print("You Win !!!!")
else:
    if guessed_number<winning_number:
        print("Too low")
    else:
        print("too high")        