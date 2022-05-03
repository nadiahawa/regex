import re
my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."

# Output: ['10909090','1',2]

pattern = re.compile('[0-9]*[0-9]')

found = pattern.search(my_string)
print(found)

found_again = re.compile(my_string)
print(found_again)