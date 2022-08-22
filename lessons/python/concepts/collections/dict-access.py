# [Dictionary]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# dict(), type()
my_dictionary = dict(((1, 2), (3, 4)))
print(my_dictionary)
"""
{1: 2, 3: 4}
"""

my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
print("Dictionary:", type(my_dictionary))
"""
Dictionary: <class 'dict'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Access
print("Access by Index:", list(my_dictionary)[1])
print("Access by Key:", my_dictionary["apple"])
print("Access with Get:", my_dictionary.get("green"))

"""
Access by   Index:  orange
Access by   Key:    fruit
Access with Get:    color
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Access with Keys, Values, Zip, Item
my_dictionary = {
    "apple": "apple fruit",
    "orange": "orange fruit",
    "yellow": "yellow color",
    "green": "green color",
}

for key in my_dictionary.keys():
    print("Key:", key, "Value:", my_dictionary[key])
"""
Key: apple      Value: apple  fruit
Key: orange     Value: orange fruit
Key: yellow     Value: yellow color
Key: green      Value: green  color
"""

for k, v in zip(my_dictionary.keys(), my_dictionary.values()):
    print("Key, Value:", k, v)
"""
Key, Value: apple       apple  fruit
Key, Value: orange      orange fruit
Key, Value: yellow      yellow color
Key, Value: green       green  color
"""

for k, v in my_dictionary.items():
    print("Key, Value Item:", k, v)
"""
Key, Value Item: apple      apple  fruit
Key, Value Item: orange     orange fruit
Key, Value Item: yellow     yellow color
Key, Value Item: green      green  color
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Length
print("Length:", len(my_dictionary))
"""
Length: 4
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Assign, Add, Update
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
my_dictionary["apple"] = "food"
my_dictionary["green"] = "green color"
print("Assign:", my_dictionary)
"""
Assign: {'apple': 'food', 'orange': 'fruit', 'yellow': 'color', 'green': 'green color'}
"""

my_dictionary.update({"peach": "fruit", "red": "color"})
print("Update:", my_dictionary)
"""
Update: {'apple': 'food', 'orange': 'fruit', 'yellow': 'color', 'green': 'green color', 'peach': 'fruit', 'red': 'color'}
"""

my_dictionary["banana"] = "fruit"
print("Add:", my_dictionary)
"""
Add:    {'apple': 'food', 'orange': 'fruit', 'yellow': 'color', 'green': 'green color', 'peach': 'fruit', 'red': 'color', 'banana': 'fruit'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check (in)
print("Check:", "apple" in my_dictionary)
"""
Check: True
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pop, Pop Item
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
print("Pop:", my_dictionary.pop("lime", "Not Found"), my_dictionary)
print("Pop:", my_dictionary.pop("apple", "Not Found"), my_dictionary)
print("Pop Item:", my_dictionary.popitem(), my_dictionary)
"""
Pop: Not Found {'apple': 'fruit', 'orange': 'fruit', 'yellow': 'color', 'green': 'color'}
Pop: fruit {'orange': 'fruit', 'yellow': 'color', 'green': 'color'}
Pop Item: ('green', 'color') {'orange': 'fruit', 'yellow': 'color'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# del
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}

del my_dictionary["yellow"]
print("Delete [Yellow]:", my_dictionary)
"""
Delete [Yellow]: {'apple': 'fruit', 'orange': 'fruit', 'green': 'color'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Clear
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
my_dictionary.clear()
print("Clear:", my_dictionary)
"""
Clear: {}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
my_dictionary1 = my_dictionary
my_dictionary2 = dict(my_dictionary)
my_dictionary3 = my_dictionary.copy()
print("Is my_dictonary is the same as my_dictionary1?", my_dictionary1 is my_dictionary)
print("Is my_dictonary is the same as my_dictionary2?", my_dictionary2 is my_dictionary)
print("Is my_dictonary is the same as my_dictionary3?", my_dictionary3 is my_dictionary)
"""
Is my_dictonary is the same as my_dictionary1? True
Is my_dictonary is the same as my_dictionary2? False
Is my_dictonary is the same as my_dictionary3? False
"""

print(my_dictionary == my_dictionary3)
"""
True
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fromkeys()
print("From Keys: ",dict.fromkeys(["key1","key2"],100))
"""
From Keys:  {'key1': 100, 'key2': 100}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# setdefault()
my_dictionary = {
    "apple": "fruit",
    "orange": "fruit",
    "yellow": "color",
    "green": "color",
}
my_dictionary.setdefault("key","value")
print("Set Default:" , my_dictionary)
"""
Set Default: {'apple': 'fruit', 'orange': 'fruit', 'yellow': 'color', 'green': 'color', 'key': 'value'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
