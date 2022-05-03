import re

file_ = open("regex_test.txt","r")
lines = file_.readlines()

for line in lines:
    # print(line)
    match = re.search(r'([A-Z][a-z]+\b).+([A-Z][a-z]+\b)', line)
    if (match != None):
        print(match.group(1),match.group(2))
        # print(match.group(2))
        #*** Was a little confused on the rubric on what exactly the output should be since the directions stated only last name
        #That solution is listed above but commented out. 
        #Use python to read the file regex_test.txt and print the 
        #last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)
        #But the expected output is as follows:
        #"""
        # Expected Output
        # Abraham Lincoln
        # Andrew P Garfield
        # Connor Milliken
        # Jordan Alexander Williams
        # None
        # None
        # """

    else:
        print(f'{match}')



#i need to create a pattern that will only take range a-z with a space a-z again and then end and print back out
