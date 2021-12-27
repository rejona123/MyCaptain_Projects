import csv

def file(lst):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact Number', 'E-mail ID'])
        
        writer.writerow(lst)

if __name__ == '__main__':    
    condition = True
    
    while(condition):
        
        student_info = input('Enter the student information in the following format (name. age, contact_number, email_id): ')
        
        student_lst = student_info.split(' ')
        
        print(f'The entered information is \nName = {student_lst[0]} \nAge = {student_lst[1]} \nContact number = {student_lst[2]} \nE-mail ID = {student_lst[3]}')
        
        correction = input('Please check if the entered information is correct. Enter (yes/no): ')
        
        if correction == 'yes':
            
            file(student_lst)
            
            check = input('Enter (yes/no) if you want to enter information for another student: ')
            
            if check == 'yes':
                condition = True
            elif check == 'no':
                condition = False
        elif correction == 'no':
            print('Please re-enter the correct values!')
