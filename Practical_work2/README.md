# SWE_Practical_Works
This script analyzes a text file (sample.txt) and provides insights such as the number of lines, words, the most common word, average word length, the longest word, and the percentage of words longer than the average word length.

Step1:
Clone the repository:

git clone https://github.com/your-username/text-analysis-project.gitcd text-analysis-project

Step2:
I ensured my sample.txt file is in the same directory as the script.

When running the analysis it should give:
##python analyze_text.py


*Counting Unique Words:
1. Import String Module

import string

Purpose: While string is imported, it isn't actually used in this function. It can be useful for more complex text manipulations but isn't necessary here.

2. Define the Function

def count_unique_words(text):

Function Definition: Starts the definition of a function named count_unique_words which takes one argument text.

3. Convert Text to Lowercase

text = text.lower()

Lowercase Conversion: Converts all characters in the input text to lowercase to ensure that "Word" and "word" are treated as the same word.

4. Split Text into Words

words = text.split()

Split Text: Splits the text into individual words based on spaces. This creates a list of words from the text.

5. Create a Set of Unique Words

unique_words = set(words)

Set Creation: Converts the list of words into a set. A set automatically removes any duplicate words, leaving only unique words.

6. Return the Number of Unique Words

return len(unique_words)

Count Unique Words: Calculates the length of the set, which is the number of unique words in the text.

Return Value: Returns this count as the output of the function.


8. Finding the Longest Word

Function Definition: find_longest_word(file_path) takes the path to a file.

Open and Read File: Opens the file in read mode.

Split Words: Reads the content and splits it into words.
Find Longest Word: Uses the max function with key=len to find the longest word in the list.
Return: Returns the longest word.
Example Usage: The longest word in sample.txt is printed.
Variable longest_word: Stores the longest word.
Print: Displays the longest word.

9. Counting Specific Words

Function Definition: count_specific_word(content) takes the text content as input.
Split Words: Splits the content into individual words.
Unique Words Set: Creates a set of the words to ensure uniqueness.
Count Unique Words: Counts the unique words (though it’s using len(set(words)) which might not be as intended).
Return: Returns the longest word in the content.
Example Usage: Prints the occurrence of specific words (though it actually returns the longest word).

10. Calculating Percentage of Words Longer Than Average Length

Function Definition: percentage_of_long_words(text) calculates the percentage of words that are longer than the average word length.
Split Words: Splits the text into individual words.
Average Length: Calculates the average word length.
Count Longer Words: Counts the number of words that are longer than the average length.
Calculate Percentage: Calculates the percentage of these longer words.
Return: Returns the percentage.
Example Usage: Prints the percentage of words longer than the average length in sample.txt.

