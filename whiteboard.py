# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters 
# and empty space characters (" "), return the length of the last word. Meaning, 
# the word that appears far most to the right if we loop through the words.
# ex = "Hello World"
# # Example Output: 5

# def find_space(string):
#     x = string.split(" ")
#     output = len(x[-1])
#     print(output)
# find_space('stupid nadia')


# Given a sentence - "Benedict Cumberbatch cannot say the word penguin correctly."
# Once a letter has occurred in the sentence, replace all of its following occurrences with '_', then return the sentence
# bonus challenge: count uppercase and lowercase letters as the same

from dataclasses import replace
sentence = "Benedict Cumberbatch cannot say the word penguin correctly."
def whiteboard(sen):
    seen_ls=[]
    for i in sen:
        if i not in seen_ls:
            seen_ls.append(i).lower()
        else:
            seen_ls.append('_')
    return ('').join(seen_ls)
print(whiteboard(sentence))