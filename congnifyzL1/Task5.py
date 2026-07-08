# Function to check palindrome

def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")

if is_palindrome(word):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")