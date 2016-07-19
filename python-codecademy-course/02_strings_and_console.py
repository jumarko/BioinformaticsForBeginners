name = "Ryan"
age = "19"
food = "cheese"

caesar = "Graham"
praline = "John"
viking = "Teresa"
print caesar
print praline
print viking

## Escaping characters
my_string = "This isn't flying, this is falling with style!"
my_escapedstring = 'This isn\'t flying, this is falling with style!'

## Access by index.
c = "cats"[0]
n = "Ryan"[3]
fifth_letter = "MONTY"[4]

## String methods
## len(), lower(), upper(), str()
## Notice that lower() and upper are called using "." notation (they work only on strings)
## while len() and str() are more genearl and calle like str(anything)

parrot = "Norwegian Blue"
print len(parrot)
print parrot.lower()
print parrot.upper()

pi = 3.14
print(pi)


## String concatenation
print "Spam " + "and " + "eggs"


## Explicit string conversion
print "The value of pi is around " + str(3.14)

## String formatting
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'This a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("what is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
    "and your favorite color is %s" % (name, quest, color)
