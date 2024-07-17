#conversion float to int
num_float = 3.14
num_int = int(num_float)   
print(num_int)

#conversion string to int
str_num = "5.2"
num_int = int(float(str_num))   
print(num_int)

#conversion string to float 
str_num = "5.2"
num_float = float(str_num)
print(num_float)

#conversion from float to string
num_float = 3.14
str_num = str(num_float)
print(str_num)

#conversion from int to float
num_int = 0o5
num_float = float(num_int)
print(num_float)

#special case
float_value = float("NAN")
print(float_value)