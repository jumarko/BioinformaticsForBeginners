### Unit 5: Lists and Dictionaries
### https://www.codecademy.com/courses/python-beginner-en-pwmb1/0/1?curriculum_id=4f89dab3d78889000300009

## 1.
zoo_animals = ["pangolin", "cassowary", "sloth", "bear"]
if len(zoo_animals) > 3:
    print "The first animal at the zoo is the " + zoo_animals[0]
    print "The first animal at the zoo is the " + zoo_animals[1]
    print "The first animal at the zoo is the " + zoo_animals[2]
    print "The first animal at the zoo is the " + zoo_animals[3]

## 2. Items are accessed by zero-based index!
numbers = [5, 6, 7, 8]

## 3.
print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

## 4. items can be assigned
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[3] = "bear"


## 5. Late arrivals & List length
suitcase = []
suitcase.append("sunglasses")
suitcase.append("notebook")
suitcase.append("tie")
suitcase.append("wallet")
list_length = len(suitcase)
print "There are %d items in the suitcase." % (list_length)
print suitcase


## 6. List Slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]
middle = suitcase[2:4]
last = suitcase[4:6]


## 7. Slicing lists and Strings
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:10]


## 8. Maintaining Order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print animals


## 9. For One and All
my_list = [1, 9, 3, 8, 5, 7]
for number in my_list:
    print(number * 2)


## 10. More with 'for'
start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
    square_list.append(number**2)

square_list.sort()
print square_list


## 11. Dictionaries
## A key can be any string or number
residents = {"Puffin" : 104, "Sloth" : 105, "Burmese Python" : 106}
print residents["Puffin"]
print residents["Sloth"]
print residents["Burmese Python"]


## 12. New Entries
menu = {}
menu['Chicken Alfredo'] = 14.50
print menu['Chicken Alfredo']

menu['Garlic Nan'] = 2.10
menu['Aloo Matter'] = 6.20
menu['Tomato Soup'] = 3.30

print "There are " + str(len(menu)) + " items on the menu."
print menu


## 13. Changing Your Mind
zoo_animals = {'Unicorn' : 'Cotton Candy House',
               'Sloth' : 'Rainforest Exhibit',
               'Bengal Tiger' : 'Jungle House',
               'Atlantic Puffin' : 'Arctic Exhibit',
               'Rockhopper Penguin' : 'Arctic Exchibit'}
del zoo_animals['Unicorn']

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Antarctica'

print zoo_animals


## 14. Remove a few things
backpack = ['xilophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')


## 15. It's Dangerous to Go Alone! Take This
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

print inventory
