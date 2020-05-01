# Notes
#
# Input
#
# "input(some random prompt for user)" will print the prompt, take input, and return that input
#   you can store the input from this statement in a variable
# all input comes in as strings so make sure to cast to propper data type
# you can cast a string to an int or float
# 
# File I/O
#
# first step is to make a pointer to the file we want to work with
# "x = open("filename", mode)"
#   x is a random variable that will store the stream
#   the mode can be "r" for read, "w" for write, or "a" for append
# "x.read()" will return the entire file
# "x.read(i)" will return next i characters in the stream
# "x.readline()" will return whatever line the stram is on
# "x.readline(i)" will return the next i lines in the stream
# you can loop through stream with for loop
#   "for line in x:"
#
# if you want to write to the same file, you have to open a new stream for writting
#   "y = open("filename", "w")"
# use "y.write(s)" where s is a string, to wrtie to a file
# after writing to a file you must use "y.close()" to close the stream
# everytime you write to a file, you restart the file
# 
# if you want to simply add text to a file, you have to open a new stream for appending
#   "z = open("filename", "a")"
# when you write to a file in "append" mode, you only add on to the existing file
# make sure to close file after you are done
#   "z.close()"

# Read data from file

x = open("companies.csv", "r")
print(x.read())

# Takes a new company from user, stores it in a list, and prints is back out

x = input("Enter: \"Name,Year,Location\": ").split(",")
print("Data is being stored...")

for i in x:
    print(i)
