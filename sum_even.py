#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".

var_int=6723
sum_even =0
x1= var_int%10 #3
y= var_int%100
x2=y//10 #2
z=var_int%1000 #723
x3=z//100 #7
x4=var_int//1000 #6
print(((x1+1)%2+(x2+1)%2+(x3+1)%2+(x4+1)%2)+sum_even)
