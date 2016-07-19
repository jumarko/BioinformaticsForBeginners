### Unit 3. Conditionals and Control Flow lesson - 15 excercices
### https://www.codecademy.com/courses/python-beginner-BxUFN/0/1?curriculum_id=4f89dab3d788890003000096

## 1. Go with the flow - motivation
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()


## 2. Compare Closely!
## ==
## !=
## <
## <=
## >
## >=
# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False


## 3. Compare... Closelier!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False


## 4. How the Tables Have Turned.

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 2**3 != 8

# Make me true!
bool_three = 2**3 == 8

# Make me false!
bool_four = (3 + 1) * 4 > 16

# Make me true!
bool_five = 1**2 >= 1


## 5. To Be and/or Not to Be

"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""


## 6. And
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 / 10 / 10

bool_four = -(1**2) < 2**0

bool_five = True and True


## 7. Or
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1


## 8. Not
bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False


## 9. This and That (or This, But Not That!)
## not is evaluated first
## and is evaulated next
## or is evaluated last
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)


## 10. Mix 'n' Match

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 1 <= 0 or (True and True)

# Make me false!
bool_three = 2**3 == 8 and not 3 == 3

# Make me true!
bool_four = not (1 >= 2**0 and (False or False))

# Make me true!
bool_five = 1 < 0 or 1 > 0


## 11. Conditional Statement Syntax

response = 'Y'

answer = "Left"
if answer == "Left":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.


## 12. If You're Having...
def using_control_once():
    if 1 < 2**1:
         return "Success #1"

def using_control_again():
    if not False:
        return "Success #2"

print using_control_once()
print using_control_again()


## 13. Else Problems, I Feel Bad for You, Son...
anser = "'Tis but a scratch!"

def black_knight():
    if answer == "'This but a scratch!":
        return True
    else:
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False


## 14. I got 99 Problems But a Switch Ain't One
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


## 15. The Big If
def the_flying_circus():
    if 2**3 >= 8 and 8 < 9:
        return True
    elif not 10**2 < 100:
        return True
    else:
        return False
