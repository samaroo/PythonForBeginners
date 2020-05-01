# Notes
# ** is used for exponents
# 2 ** 3 returns 8
# Different comparison operators
# "and" instead of "&&"
# "or" instead of "||"
# "not" instead of "!"


operand1 = 250.66
operand2 = 1008.2

print("%0.2f + %0.1f = " % (operand1, operand2), operand1 + operand2)
print("%0.2f - %0.1f = " % (operand1, operand2), operand1 - operand2)
print("%0.2f * %0.1f = " % (operand1, operand2), operand1 * operand2)
print("%0.2f / %0.1f = " % (operand1, operand2), operand1 / operand2)
print("%0.2f " % operand1, "%", " %0.1f =  " % operand2, operand1 % operand2, sep = "")

operand1 = 12.722
operand2 = 33.8

print("%0.3f + %0.1f = " % (operand1, operand2), operand1 + operand2)
print("%0.3f - %0.1f = " % (operand1, operand2), operand1 - operand2)
print("%0.3f * %0.1f = " % (operand1, operand2), operand1 * operand2)
print("%0.3f / %0.1f = " % (operand1, operand2), operand1 / operand2)
print("%0.3f " % operand1, "%", " %0.1f =  " % operand2, operand1 % operand2, sep = "")
