import re

file_ = open("regex_test.txt","r")
lines = file_.readlines()

for line in lines:
    # print(line)
    match = re.search(r'([A-Z][a-z]+\b).+([A-Z][a-z]+\b)', line)
    if (match != None):
        print(match.group(2))
        # print(match.groups())
        
#i need to create a pattern that will only take range a-z with a space a-z again and then end and print back out
