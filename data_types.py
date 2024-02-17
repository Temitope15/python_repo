var_1 = 45  # this is a decimal
var_2 = 0b11  # this is binary
var_3 = 0X22  # this is hexadecimal
var_4 = 0o34  # this is octal
print(var_1, var_2, var_3, var_4)
# That is that for int
# For float
var_5 = 3.4

# For strings
var_6 = "Sunmade"
print(type(var_5))  # will print <class, 'float' >
print(var_6[3])  # will print m

# The concept of escaping characters
var_7 = "\"Sunmade\" is the world\'s best!\n"  # I have successfully escaped the inverted commas by using backslash "\"
print(5 * var_7)  # This will print var_7 on five separate lines

# For boolean
var_8 = True  # Note that True or False are the values here and that they must start with capital letter "T" and "F"
print(type(var_8))  # will print < class, 'bool' >
