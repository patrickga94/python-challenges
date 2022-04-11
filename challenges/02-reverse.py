# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


from posixpath import split


string = input("Enter a string: ")

def reverse_string(sample_string):
    string_list = split(sample_string)
    reversed = []
    i = len(sample_string) - 1
    while i > -1:
        reversed.append(sample_string[i])
        i -= 1
    reversed_string = ''.join(reversed)
    print(reversed_string)

reverse_string(string)