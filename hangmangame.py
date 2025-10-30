import random


words = ["apple", "table", "chair", "mouse", "plant"]


secret_word = random.choice(words)


guessed_letters = []     
attempts = 6             


guessed_letters.append(secret_word[0])    
guessed_letters.append(secret_word[-1])   

print("🎯 Welcome to the Hangman Game!")
print("Try to guess the word one letter at a time.")
print(f"(Hint: The word starts with '{secret_word[0]}' and ends with '{secret_word[-1]}')")


display = ""
for letter in secret_word:
    if letter in guessed_letters:
        display += letter + " "
    else:
        display += "_ "
print("Word:", display.strip())


while attempts > 0:
    guess = input("\nEnter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter one letter only.")
        continue

   
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    
    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display.strip())

    
    if "_" not in display:
        print("\n🎉 Great job! You guessed the word:", secret_word)
        break
else:
    print("\n💀 Game Over! The word was:", secret_word)
