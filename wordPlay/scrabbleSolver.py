import string
import scrabble

def findUUInWord():
    for word in scrabble.wordlist:
        if "uu" in word:
            print(word)

# # print all word with no duplicates
def findWordWithNoDuplicateLetters():
    for letter in string.ascii_lowercase:
        exists = False
        for word in scrabble.wordlist:
            if letter * 2 in word:
                exists = True
                break
        if not exists:
            print ("No english words with double " + letter)

vowels = "aeiou"
def hasAllVowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True
def wordHasVowels():
    for word in scrabble.wordlist:
            if hasAllVowels(word):
                print(word)


# ##Palindrom Exercise 1
def longestPallindromeEx1():
    longestPalindrome = ""
    for word in scrabble.wordlist:
        isPalindrome = True
        for i in range(len(word)):
            if word[i] != word[-(i + 1)]:
                isPalindrome = False
        if isPalindrome and len(word) > len(longestPalindrome):
            longestPalindrome = word
    print(longestPalindrome)

# ##Palindrom Exercise 2
def longestPallindromeEx2():
    longestPalindrome = ""
    for word in scrabble.wordlist:
        if list(word) == list(reversed(word)) and len(word) > len(longestPalindrome):
            longestPalindrome = word
    print(longestPalindrome)
        
# ##Palindrom Exercise 3
def longestPallindromeEx3():
    longestPalindrome = ""
    for word in scrabble.wordlist:
        if  word == word[::-1] and len(word) > len(longestPalindrome):
            longestPalindrome = word
    print(longestPalindrome)

longestPallindromeEx3()

