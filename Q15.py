n = int(input('please enter a number : '))
variable_to_store_sum = 0
while (n>0):
    digit = n%10
    variable_to_store_sum = variable_to_store_sum+digit
    n=n//10
print ('the sum of digits is '+ str(variable_to_store_sum))