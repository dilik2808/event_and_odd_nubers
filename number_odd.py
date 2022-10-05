#A four-digit integer is given. Find the number of odd digits in it.
var_int=6783
#Create a variable "var_int" and assign it a four-digit integer value.
x1=var_int%10 #3
y= var_int%100 #83
x2= y//10 #8
z=var_int%1000 #783
x3=z//100 #7
x4=var_int//1000 #6

print((x1%2)+(x2%2)+(x3%2)+(x4%2))

#Print the number of odd digits in the variable "var_int".
