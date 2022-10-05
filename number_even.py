#A four-digit integer is given. Find the number of even digits in it.
var_int = 7852
#Create a variable "var_int" and assign it a four-digit integer value.
x1 = var_int%10#8
y= var_int%100#48
x2= y//10#4
z=var_int%1000#548
x3= z//100#5
x4=var_int//1000#2

print((x1+1)%2 + (x2+1)%2+(x3+1)%2+ (x4+1)%2)



#Print the number of even digits in the variable "var_int".