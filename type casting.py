# Type casting means changing the data type of a variable from one type to another, such as converting a string to an integer or an integer to a float.

# TYPES OF TYPE CASTING 
#---> IMPLICIT TYPE CASTING ---> EXPLICIT TYPE CASTING


# ____IMPLICIT TYPE CASTING _____ #

a = "100"
# variable a stores {{string}} type data
b = int(a)
# now string type is converted to {{int}} type by the user
print(b)
print(type(a),type(b))


# _____EXPLICIT TYPE CASTING______ #
a = 100
# here a stores {{int}} type 

b = 207.89
# here b stores {{float}} type

c = a+b
# python converts automatically  {{int}}  to  {{float}}  for easy calculation

print(c)
print(type(a),type(b),type(c))
