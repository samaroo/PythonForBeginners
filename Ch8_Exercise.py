# Notes
# Using functions from "str" library
#
# "str.capitalize(m)" will reverse the "case" of each character after a sentence in m
#   "welcome! How are you?" will turn into "Welcome! how are you?"
# "m.center(int x, char c)" will center message m in a string of x number of c characters
# "m.count(c)" will count how many times c occurs in m
# "m.find(s)" will find the substring s inside of m and returns its index
# "m.isalpha()" will return true if every character in m is a letter
# "m.isdigit()" will return true if every character is a number
# "s.join(l)" will take each element of a list or tuple t, and put them in a string with the string s inbetween them
#   if s = "," and l = [Brandon, Thrishna], then s.join(l) will return "Brandon, Thrishna"
# "s.split(s2)" will partition string s into pieces seperated by string s2 and put each partition into a list


# Given code

poem = "With rue my heart is laden\n"
poem += "For golden friends I had\n"
poem += "For many a rose-lipped maiden\n"
poem += "And many a light foot lad\n"
poem += "By brooks too broad for leaping\n"
poem += "The light oot boys are laid\n"
poem += "The rose lipped girls are sleeping\n"
poem += "In fields where roses fade\n"
print(poem)
# Print each character in the poem along withs its line and index in the line
# If the character is capitalized, write "Captial" next to it

poemList = poem.split("\n")

counter = 1
for i in poemList:
    counter2 = 0
    for j in i:
        print("Line: ", counter, " Char: ", counter2, " ", j, (" Capital" if j.isupper() else ""), sep = "")
        counter2 += 1
    counter += 1