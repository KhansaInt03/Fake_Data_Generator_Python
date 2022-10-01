from faker import Faker
import csv
import random

print("""Welcome to Fake Data Generator!!!\nYou can generate fake data like name, username, address, and email also the fake datas is saved as CSV file.""")

print()

# This function is for data generator
def data_fake_generator():

    fake = Faker()

    f_name = fake.name()
    f_add = fake.address().replace('\n',', ')
    uname = f_name.lower().replace(' ','') 
    username = uname + str(random.randint(10,50))
    email = uname + '@gmail.com'

    return(f_name, f_add, username, email)

total_generate = int(input("How many data you'd like to generate? \n >>> "))

print()

file_name = input("Your CSV file's name \n >>> ") + '.csv'

# This section is for generate your CSV file
with open (f'{file_name}', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('Name', 'Address', 'Username', 'E-mail'))
    for i in range(total_generate):
        writer.writerow(data_fake_generator())