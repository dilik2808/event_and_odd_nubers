#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
var_int=8547
sum_even=0
x1=var_int%10 #7
y= var_int%100 #47
x2=y//10 #4
z=var_int%1000 #547
x3=z//100 #5
x4= var_int//1000 #8
sum_even=(x1%2)+(x2%2)+(x3%2)+(x4%2)
