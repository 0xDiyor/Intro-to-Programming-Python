
#Python Program 1: Strings

sentence = input("Please input a sentence: ")

print(f"First 5 characters: {sentence[:5]}")
print(f"Lowercase version: {sentence.lower()}")
print(f"Spaces replaced with underscores: {sentence.replace(' ', '_')}")
words = sentence.split()
print(f"List of words: {words}")
print(f"Hyphen-joined string: {'-'.join(words)}")

print() #extra spacing

#Python Program 2: List and Dictionaries
items = []
print("Enter 5 items you would pack for a trip:")
for i in range(1, 6):
    item = input(f"{i}: ")
    items.append(item)

items.sort()

print() #extra spacing

print(f"Sorted list: {items}")

items.pop()
print(f"Updated list after removing the last item: {items}")

items.append("Sunscreen")
print(f"Updated list after adding an item: {items}")

print() #extra spacing

packed = {item: 1 for item in items}
print(f"Packed items dictionary: {packed}")

for item, qty in packed.items():
    print(f"Item: {item}, Quantity: {qty}")

print() #extra spacing

#Python Program 3: Classes

class TripItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def describe(self):
        print(f"Item: {self.name}, Quantity: {self.quantity}")

trip_items = []
for i in range(1, 4):
    name = input(f"Enter the name of the {['first', 'second', 'third'][i-1]} item: ")
    quantity = int(input(f"Enter the quantity for {name}: "))
    trip_items.append(TripItem(name, quantity))

print() #extra spacing

print("Packing List:")
for item in trip_items:
    item.describe()