''' 
Q. Convert a given string to a url string, i.e., replace every space with 
%20

This is pretty simple in python. Split the string with " " as the delimiter
and join the list with .join with the string "%20". 
In Java or CPP, we go through the string and count the number of spaces.
The second time we traverse from the end and everytime we come across a space
we replace index-1, index-2 and index-3 with %,2,0 as characters.
'''


def urlify(str):
    strlist = str.split(" ")
    print(strlist)
    return "%20".join(strlist)

print(urlify("Mr John Smith"))