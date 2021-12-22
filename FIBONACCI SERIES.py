n = int(input('Enter any number: '))
a = 0
b = 1

count  = 0

F = [0, 1]

if n <= 0:
    print('Please enter a valid number')

else:   
    while count < n:
     n1 = a + b
     a = b
     b = n1
     count += 1
     F.append(n1)
    
    print(f'The Fibonacci series of {n} is = {F}')
