import random
from data.data import Person
from faker import Faker
import os
faker_en = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(20, 80),
        salary=random.randint(1000, 100000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        mobile=faker_en.msisdn()
    )

def generated_file():
    path = os.path.abspath(f"../files/test{random.randint(0, 999)}.txt")
    file = open(path, 'w+')
    file.write(f'Hello world{random.randint(0, 999)}')
    file.close()
    return file.name, path
