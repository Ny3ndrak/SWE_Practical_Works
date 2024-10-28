def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_file('sample.txt')
print(content[:100])  

def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

analyze_text('sample.txt')

#Counting unique words
import string

def count_unique_words(text):
    text = text.lower()
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

#Finding the longest word
def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
    return longest_word

file_path = 'sample.txt'
print(f"The longest word is: {find_longest_word(file_path)}")

#Counting specific words
def count_specific_word(content):
    words = content.split()
    count_specific_word = set(words)
    count_specific_word_count = len(count_specific_word)
    return max(words, key=len)
print("occurance of specific words:", count_specific_word(content))
 
#Calculating percentage of words longer than average length
def percentage_of_long_words(text):
    words = text.split()
    if len(words) == 0:
        return 0.0
    average_length = sum(len(word) for word in words) / len(words)
    longer_words_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_words_count / len(words)) * 100
    return percentage
text = read_file('sample.txt')
print(percentage_of_long_words(text))








