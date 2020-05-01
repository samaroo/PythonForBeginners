# Learned:
#   *Lists: 
#       ^listOfNums = [1, 2, 3, 4, 5]
#       ^They print as [1, 2, 3, 4, 5]
#       ^Each element can be modified
#   *Tuples: 
#       ^nums = (1, 2, 3, 4, 5)
#       ^They print as (1, 2, 3, 4, 5)
#       ^None of the elements can be modified
#   *Dictionaries: 
#       ^gpas = {"Name": "Mark", "GPA": 3.55, "Scores": [83, 85, 87]}
#       ^Kind of like maps (associative list)
#       ^gpas["Name"] will return "Mark"
#       ^(gpas["Scores"])[0] will return 83
#       ^Has a function called x.get() which takes in a key and returns its value
#           ^If not found will return "None"
#               ^Function has an optional second parameter to set "Not found" message
#       ^You can modify each key's value
#           ^gpas["Name"] = "Brandon"
#           ^if key is not found, it will addd it to the dicitonary
#       ^Two ways to remove elements from dictionary
#           ^del gpa["Name"]
#           ^gpa.pop("Name")
#               ^will return the value unlike del
#       ^len(gpa) will return the amount of keys in dictionary
#       ^gpa.keys() returns keys of dictionary
#       ^gpa.values() return values of dictionaries
#       ^gpa.items() will return the pairs of keys and values in dictionaries


GPA = 3.15
studentName = "John Smith"
studentNum = "0023452"

places= ["Hawaii", "Alaska", "Toronto", "London", "Greece"]

print(GPA, studentName, studentNum, sep="\n")
print("%s has the following student number: %s" % (studentName, studentNum))
# %0.1f sets precision of float point (0.0), %0.2f would be (0.00)
print("%s has the following student GPA: %0.1f" % (studentName, GPA))

for i in places:
    print(i)




