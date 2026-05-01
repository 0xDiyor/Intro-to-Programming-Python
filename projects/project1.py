#Python Program 1: Basic Input and Output

name = input("What is your name? ")
hobby = input("What is your hobby? ")

print(f"Hello {name}! It's great that you enjoy {hobby}.")

#Python Program 2: Variables and Expressions

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2

print(f"The sum of {number1} and {number2} is {sum_result}.")
print(f"The difference when {number2} is subtracted from {number1} is {difference_result}.")
print(f"The product of {number1} and {number2} is {product_result}.")
print(f"The quotient of {number1} divided by {number2} is {quotient_result}.")

#Python Program 3: Data Types and Conversions

sentence = input("Enter a short sentence: ")
uppercase_sentence = sentence.upper()
character_count = len(sentence)
word_list = sentence.split()
print(f"The sentence in uppercase: {uppercase_sentence}")
print(f"The number of characters in the sentence: {character_count}")
print(f"The sentence as a list of words: {word_list}")
