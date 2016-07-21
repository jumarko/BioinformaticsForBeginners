### Unit 3 - Pig Latin
### https://www.codecademy.com/courses/python-beginner-2W5v7/0/1?curriculum_id=4f89dab3d788890003000096
###
### Implement Pig Latin translator
### Pig Lating is a language game, where you move the first letter of the word to the end and add "ay.".
### So "Python" becomes "ythonpay"


## 0. Print welcome message
print("Pig Latin")


## 1. Ask the user to input a word in English
print("Welcome to the Pig Latin Translator!")
original = raw_input("Enter a word:")


## 2. Make sure the user entered a valid word.
# if len(original) > 0 and original.isalpha():
#     print(original)
# else:
#     print "empty"


## 3. Convert the word from English to Pig Latin
pyg = "ay"
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print new_word
else:
    print "empty"


## 4. Display the translation result.
