lst1 = []

lst2 = []

n = int(input('Enter how many number you want in the list: '))

for i in range(1, n+1):
    a  = int(input('Enter any value: '))
    lst1.append(a)
print(f'Given list: {lst1}')
    
for j in lst1:
    if j >= 0:
       lst2.append(j)
       
print(f'The positive numbers in the given list is: {lst2} ')
