secret = 9
guessCount = 0
while guessCount < 3:
    guess = int(input("Enter a guess: "))
    guessCount += 1
    if guess == secret:
        print("You won!")
        break
