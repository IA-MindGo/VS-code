#𝗣𝗿𝗶𝗻𝘁 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝟭 𝘁𝗼 𝟮𝟬 𝘂𝘀𝗶𝗻𝗴 𝗮 𝘄𝗵𝗶𝗹𝗲 𝗹𝗼𝗼𝗽۔
while True:
    for i in range(1, 21):
        print(i)
    break
# 𝗣𝗿𝗶𝗻𝘁 𝗲𝘃𝗲𝗿𝘆 𝟯𝗿𝗱 𝗻𝘂𝗺𝗯𝗲𝗿 𝗳𝗿𝗼𝗺 𝟯 𝘁𝗼 𝟯𝟬۔
i = 3
while i <= 30:
    print(i)
    i += 3
#𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝘀𝘂𝗺 𝗼𝗳 𝗲𝘃𝗲𝗻 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝟮 𝘁𝗼 𝟮𝟬۔
sum_even = 0
i = 2
while i <= 20:
    sum_even += i
    i += 2
print("Sum of even numbers from 2 to 20 is:", sum_even)
#𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝗽𝗿𝗼𝗱𝘂𝗰𝘁 𝗼𝗳 𝗼𝗱𝗱 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝟭 𝘁𝗼 𝟵۔
product_odd = 1
i = 1   
while i <= 9:
    if i % 2 != 0:  # Check if the number is odd
        product_odd *= i
    i += 1
print("Product of odd numbers from 1 to 9 is:", product_odd)
#𝗖𝗿𝗲𝗮𝘁𝗲 𝗮 𝗹𝗶𝘀𝘁 𝗼𝗳 𝟱 𝗻𝗮𝗺𝗲𝘀 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝗲𝗮𝗰𝗵 𝗻𝗮𝗺𝗲 𝗼𝗻 𝗮 𝗻𝗲𝘄 𝗹𝗶𝗻𝗲۔
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
i = 0   
while i < len(names):
    print(names[i])
    i += 1
#𝗖𝗼𝘂𝗻𝘁 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗹𝗲𝘁𝘁𝗲𝗿𝘀 '𝗮' 𝗮𝗿𝗲 𝗶𝗻 𝘁𝗵𝗲 𝘄𝗼𝗿𝗱 "𝗯𝗮𝗻𝗮𝗻𝗮"۔
word = "banana"
count_a = 0 
i = 0
while i < len(word):
    if word[i] == 'a':
        count_a += 1
    i += 1
print("Number of 'a' in 'banana':", count_a)    
#𝗣𝗿𝗶𝗻𝘁 𝗼𝗻𝗹𝘆 𝘁𝗵𝗲 𝗻𝗲𝗴𝗮𝘁𝗶𝘃𝗲 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝗮 𝗴𝗶𝘃𝗲𝗻 𝗹𝗶𝘀𝘁۔
numbers = [10, -5, 3, -2, 8, -1, 0, 7, -4]
i = 0
print(f"The given list is: {numbers}")
print("Negative numbers from the list:")
while i < len(numbers):
    if numbers[i] < 0:
        print(numbers[i])
    i += 1
#𝗣𝗿𝗶𝗻𝘁 𝗼𝗻𝗹𝘆 𝘁𝗵𝗲 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗲𝗻𝗱𝗶𝗻𝗴 𝗶𝗻 𝟱 𝗳𝗿𝗼𝗺 𝟭 𝘁𝗼 𝟱𝟬۔
i = 1
print("Numbers ending with 5 from 1 to 50:")
while i <= 50:
    if i % 10 == 5:  # Check if the number ends with 5
        print(i)
    i += 1
#𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝗹𝗲𝗻𝗴𝘁𝗵 𝗼𝗳 𝗲𝗮𝗰𝗵 𝘄𝗼𝗿𝗱 𝗶𝗻 𝘁𝗵𝗲 𝗹𝗶𝘀𝘁 ["cat", "elephant", "bat"]۔
list_of_words = ["cat", "elephant", "bat"]
i = 0
print("Length of each word in the list:")
while i < len(list_of_words):
    print(f"Length of '{list_of_words[i]}' is {len(list_of_words[i])}")
    i += 1
#𝗧𝗮𝗸𝗲 𝟯 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗮𝘀 𝗶𝗻𝗽𝘂𝘁 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝘁𝗵𝗲𝗶𝗿 𝗮𝘃𝗲𝗿𝗮𝗴𝗲۔
numbers = []
i = 0
while i < 3:
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    i += 1
average = sum(numbers) / len(numbers)
print("The average of the entered numbers is:", average)
# 𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝘁𝗮𝗯𝗹𝗲 𝗼𝗳 𝟱 𝗶𝗻 𝗿𝗲𝘃𝗲𝗿𝘀𝗲 (𝗳𝗿𝗼𝗺 𝟱×𝟭𝟬 𝘁𝗼 𝟱×𝟭)۔
i = 10
print("Table of 5 in reverse order:")
while i >= 1:
    print(f"5 x {i} = {5 * i}")
    i -= 1
# 𝗨𝘀𝗲 𝗮 𝗳𝗼𝗿 𝗹𝗼𝗼𝗽 𝘁𝗼 𝗽𝗿𝗶𝗻𝘁 𝗮𝗹𝗹 𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀 𝗶𝗻 "𝗣𝘆𝘁𝗵𝗼𝗻 𝗜𝘀 𝗙𝘂𝗻"۔
print("Characters in 'Python Is Fun':\n")
for char in "Python Is Fun":
    print(char)
#𝗖𝗿𝗲𝗮𝘁𝗲 𝗮 𝗹𝗶𝘀𝘁 𝗼𝗳 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝗲𝘃𝗲𝗿𝘆 𝘀𝗲𝗰𝗼𝗻𝗱 𝗶𝘁𝗲𝗺۔
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Every second item in the list:")
for i in range(1, len(numbers_list), 2):
    print(numbers_list[i])      
#𝗧𝗮𝗸𝗲 𝗮 𝘄𝗼𝗿𝗱 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝘂𝘀𝗲𝗿 𝗮𝗻𝗱 𝗰𝗼𝘂𝗻𝘁 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗰𝗼𝗻𝘀𝗼𝗻𝗮𝗻𝘁𝘀 𝗶𝘁 𝗵𝗮𝘀۔
word = input("Enter a word: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count_consonants = 0
for char in word:
    if char in consonants:
        count_consonants += 1
print(f"The number of consonants in '{word}' is: {count_consonants}")
#𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝗰𝘂𝗯𝗲𝘀 𝗼𝗳 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝟭 𝘁𝗼 𝟱۔
for i in range(1, 6):
    print(f"The cube of {i} is {i ** 3}")
#𝗧𝗮𝗸𝗲 𝗮 𝗹𝗶𝘀𝘁 𝗼𝗳 𝘄𝗼𝗿𝗱𝘀 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝘁𝗵𝗼𝘀𝗲 𝘁𝗵𝗮𝘁 𝘀𝘁𝗮𝗿𝘁 𝘄𝗶𝘁𝗵 '𝗮'۔
words_list = ["apple", "banana", "avocado", "grape", "apricot"]
print("Words that start with 'a':")
for word in words_list:
    if word.startswith('a') or word.startswith('A'):
        print(word)
#𝗨𝘀𝗲 𝗮 𝗹𝗼𝗼𝗽 𝘁𝗼 𝗽𝗿𝗶𝗻𝘁 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝗯𝗲𝘁𝘄𝗲𝗲𝗻 𝟭𝟬𝟬 𝗮𝗻𝗱 𝟭𝟭𝟬 (𝗲𝘅𝗰𝗹𝘂𝗱𝗶𝗻𝗴 𝟭𝟬𝟱)۔
print("Numbers between 100 and 110 (excluding 105):\n")
for i in range(100, 111):
    if i != 105:
        print(i)
# 𝗣𝗿𝗶𝗻𝘁 𝘁𝗵𝗲 𝗳𝗶𝗿𝘀𝘁 𝟱 𝗽𝗼𝘀𝗶𝘁𝗶𝘃𝗲 𝗺𝘂𝗹𝘁𝗶𝗽𝗹𝗲𝘀 𝗼𝗳 𝟰۔
i = 1
count = 0  
print("First 5 positive multiples of 4 are : ")
while count < 5:
    print(i*4)
    count += 1
    i += 1
#𝗣𝗿𝗶𝗻𝘁 𝗲𝗮𝗰𝗵 𝘄𝗼𝗿𝗱 𝗶𝗻 𝘁𝗵𝗲 𝘀𝗲𝗻𝘁𝗲𝗻𝗰𝗲 "𝗖𝗼𝗱𝗶𝗻𝗴 𝗶𝘀 𝗲𝗮𝘀𝘆" 𝗼𝗻 𝗮 𝗻𝗲𝘄 𝗹𝗶𝗻𝗲۔
sentence = "Coding is easy"
words = sentence.split()
i = 0
print("Words in the sentence are :")
while i < len(words):
    print(words[i])
    i += 1  
#**𝗖𝗿𝗲𝗮𝘁𝗲 𝗮 𝗻𝘂𝗺𝗯𝗲𝗿 𝗹𝗶𝘀𝘁 𝗮𝗻𝗱 𝗽𝗿𝗶𝗻𝘁 𝗼𝗻𝗹𝘆 𝗲𝘃𝗲𝗻 𝗻𝘂𝗺𝗯𝗲𝗿𝘀 𝘂𝘀𝗶𝗻𝗴 𝗰𝗼𝗻𝗱𝗶𝘁𝗶𝗼𝗻𝘀 𝗶𝗻 𝗹𝗼𝗼𝗽.
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list:")
for number in numbers_list:
    if number % 2 == 0:  # Check if the number is even
        print(number)
