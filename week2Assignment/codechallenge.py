# Sum of list
numbers = input("Enter integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
total = sum(numbers)
print("Sum of the integers:", total)

# Tuple 
favorite_books = ("Book1", "Book2", "Book3", "Book4", "Book5")

for book in favorite_books:
    print(book)
    
# Dictionary
person_info = {}

person_info['name'] = input("Enter name: ")
person_info['age'] = input("Enter age: ")
person_info['favorite_color'] = input("Enter favorite color: ")

print("Person's information:", person_info)

# Set
set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
set2 = set(input("Enter integers for set 2 separated by spaces: ").split())

# Create a new set containing common elements from both sets
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)
# List Comprehension
words = ["apple", "banana", "orange", "grape", "kiwi"]

odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)