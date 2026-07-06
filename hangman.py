import random

# Word list
words = ["earth", "mars", "jupiter", "saturn",
         "uranus", "neptune", "mercury", "venus"]

# Random word selection
word = random.choice(words)

# Blank spaces
display = ["_"] * len(word)

# Store guessed letters
letters = []

# Total chances
chance = 6

print("=== HANGMAN GAME ===")
print("Guess letters from the SOLAR SYSTEM")

# Game loop
while chance > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Chances left:", chance)
    print("Guessed letters:", " ".join(letters))

    # User input
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) > 1:
    print("Enter only one letter.")

    # Already guessed
    if guess in letters:
        print("You already guessed this letter.")
        continue

    letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    # Wrong guess
    else:
        print("Wrong Guess!")
        chance -= 1

# Win condition
if "_" not in display:
    print("\n🎉 Congratulations! You Won!")
    print("The word was:", word)

# Lose condition
else:
    print("\n💀 Game Over!")
    print("The word was:", word)
