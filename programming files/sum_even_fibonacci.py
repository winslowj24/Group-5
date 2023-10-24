#Intialize a , b, and sum even variable to 0 , 1 , 0 respectively
a, b = 0, 1
sum_even = 0
#while loop to loop until b is even
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    #intialize a,  set b to b, and sum a and b
    a, b = b, a+b
#print sum even
print(sum_even)

# answer should be 4613732
