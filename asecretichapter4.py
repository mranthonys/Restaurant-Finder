total = 0 #the accumulator is set to 0 for the running total
for num in range(1, 101): #the for loop is set with 101 as the max value
    if num % 3 == 0 and num % 5 == 0: #multiples of 3&5 are set first
        print("FizzBuzz") #to not interrupt the following
    elif num % 3 == 0: #multiples of 3
        total += num
        print("Fizz")
    elif num % 5 == 0: #multiples of 5
        total += num
        print("Buzz")
    else:
        print(num) #the remaining numbers are printed
print('Your total is:', total) #running total of 3 and 5
