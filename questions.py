welc = 'Hello World!'
user_data = 'Current data collected: \n'

print('Please ansver all questions correctly!')
user_name1 = input("What is your name: ")
user_age = input("What is your age: ")
print(user_data)

print('Name: ', user_name1)
print('Name: ', user_age + '\n')

user_input = input('Please enter Continue: '+'\n')

if user_input == 'Continue' or user_input == 'continue' or user_input == 'c' or user_input == 'C':

 print(welc)

else:
 print("You entered the data incorrectly!") 
