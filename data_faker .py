import random
import csv
from faker import Faker

fake = Faker()

# Membuat data
data = []
for _ in range(1000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    age = random.randint(20, 65)
    salary = random.randint(30000, 120000)
    department = fake.job()
    data.append([first_name, last_name, email, age, salary, department])

# Menyimpan data dalam format CSV
file_path = 'data_karyawan.csv'  # Path file CSV
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["First Name", "Last Name", "Email", "Age", "Salary", "Department"])
    writer.writerows(data)

print(f"Data berhasil dibuat dan disimpan dalam file: {file_path}")
