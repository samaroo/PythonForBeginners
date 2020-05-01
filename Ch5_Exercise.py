# Notes
# if statements have ":" and tabs to define scope instead of {}
# use "elif" instead of "else if"
# ternary if-else statements ((x > y ? 1 : 0)) in python is ((first possible item to return) if (boolean statement) else (second possible item to return))
# len() finds the length/size of any list, tuple, or string
# range(x) will give you a list of numbers from 0 to 1-x; used for for loops

subjectList = ["English", "Spanish", "Algebra", "Geography", "Theater"]
gpas = [3.12, 3.45, 2.99]takingGeography = False
for i in subjectList:
    if(i == "Geography"):
        takingGeography = True

print(takingGeography)

average = 0.0
for j in gpas:
    average += j

average /= len(gpas)
print(average)

print("Average is 3.33 or greater" if average >= 3.33 else "Avergae is less than 3.33")

for i in range(5):
    print(i)