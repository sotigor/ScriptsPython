'''
Task 1
Make a program that has some sentence (a string) on input and returns
a dict containing all unique words as keys and the number of occurrences
as values.
'''
import string

sentence = "Make a has that. a has some sentence. on (a string) on input as has. sentence"

for sign in string.punctuation:
	if sign in sentence:
		sentence = sentence.replace(sign, '')
sentence_parsed = sentence.split()

word_dict = {}

for word in sentence_parsed:
	if word not in word_dict:
		word_dict[word] = 0
	word_dict[word] += 1
print(word_dict)
"""
Task 2
Create a function which takes as input two dicts with structure 
mentioned above, then computes and returns the total price of stock.
Создайте функцию, которая получает на вход два словаря (запас на 
складе и цены), а потом возвращает суммарную стоимость товаров.
"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_cost = sum([stock[item]*prices[item] for item in stock])
print(total_cost)
