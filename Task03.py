# task 03
# Convert the word to uppercase
user_word = input("Enter a word: ")  # Define the variable "user_word" by getting input from the user
user_word = user_word.upper()

# Iterate through each character in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in ['A', 'E', 'I', 'O', 'U']:
        # If it's a vowel, continue to the next iteration without printing it
        continue
    print(letter)