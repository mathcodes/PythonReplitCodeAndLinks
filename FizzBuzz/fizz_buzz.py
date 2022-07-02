# FIZZ BUZZ

# This is probably the most common interview task for coders:

# For the numbers 1-100, print them all out, but if the number is divisible 3, print "FIZZ" instead. If the number is divisible by 5, print "BUZZ" instead. If the number is divisible by both 3 AND 5, print "FIZZBUZZ"

# Generally when you start a task in coding, you want to think about the process and what you are trying to do:

# Print corresponding words for `3 and 5s` so neither the 5 nor 3 will snag a number... then `5s`, then `3s`:

array = [3, 6, 9]

for num in range (0, 101, 1):
    # if f is divisible by 5 AND divisible by 3, print fizzbuzz
    if num % 5 == 0 and num % 3 == 0:
        print(f'fizzbuzz because {num} is divisible by 3 and 5')
    elif num % 5 == 0:
        print('buzz')
    elif num % 3 == 0:
        print('fizz')
    else:
        print(num)
    
# (which is actually 1-100... it DOES NOT include the top number in the range)

# REPLIT: https://replit.com/@fullstack11235/FizzBuzz








 

 
