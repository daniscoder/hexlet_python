import json
from collections import Counter
from datetime import datetime as dt
from collections import defaultdict

# 1. Логи посещения сайта
print('1. Логи посещения сайта')

logs = [
    "192.168.1.1 2023-10-01 10:00:00 200",
    "192.168.1.2 2023-10-01 10:05:00 404",
    "192.168.3.1 2023-10-01 10:10:00 500",
    "10.0.0.1 2023-10-01 10:15:00 200",
    "192.168.1.2 2023-10-01 10:20:00 200"
]

ip_addresses = [log_entry.split()[0] for log_entry in logs]

unique_ip_addresses = list(set(ip_addresses))

status_count = dict(Counter([log_entry.split()[-1] for log_entry in logs]))

visiting_times = [dt.strptime(log_entry.split()[2], "%H:%M:%S").time() for log_entry in logs]

print(f'IP-адреса: {ip_addresses}')
print(f'Уникальные IP-адреса: {unique_ip_addresses}')
print(f'Столько раз встречается каждый статус ответа: {status_count}')
print(f'Самое раннее посещение: {min(visiting_times)}')
print(f"Самое позднее посещение: {max(visiting_times)}")


# 2. Заказы пользователей
print('\n2. Заказы пользователей')

orders = [
    (101, "Python для начинающих"),
    (101, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (101, "Python для начинающих"),
    (103, "Искусство программирования"),
    (102, "Python для начинающих"),
    (103, "Чистый код"),
    (101, "Грокаем алгоритмы"),
    (102, "Грокаем алгоритмы"),
    (103, "Алгоритмы и структуры данных"),
    (102, "Чистый код"),
    (104, "Python для начинающих")
]

user_books = defaultdict(set)
for order in orders:
    user_books[order[0]].add(order[1])

books_count = -1
user_id_max_books = -1
for user_id in user_books:
    l = len(user_books[user_id])
    if l > books_count:
        user_id_max_books = user_id
        books_count = l

print(f'user_books: {dict(user_books)}')
print(f'Пользователь, который купил больше всего уникальных книг: {user_id_max_books}')


# 3. Работа с деревом файлов
print('\n3. Работа с деревом файлов')

tree1 = {
    'name': '/',
    'meta': {},
    'type': 'directory',
    'children': [
        {
            'name': 'eTc',
            'meta': {},
            'type': 'directory',
            'children': [
                {
                    'name': 'NgiNx',
                    'meta': {'size': 4000},
                    'type': 'directory',
                    'children': [],
                },
                {
                    'name': 'CONSUL',
                    'meta': {},
                    'type': 'directory',
                    'children': [
                        {
                            'name': 'config.json',
                            'type': 'file',
                        },
                    ],
                },
            ],
        },
        {'name': 'hosts', 'type': 'file', 'meta': {}},
    ],
}

def uppercase_filenames(tree):
    if 'children' in tree:
        for child in tree['children']:
            uppercase_filenames(child)
    elif tree['type'] == 'file':
        tree['name'] = tree['name'].upper()

uppercase_filenames(tree1)

print(json.dumps(tree1, indent=4))

# 4. Класс Dog
print('\n4. Класс Dog')

class Dog:
    def __init__(self, name=None, breed=None, age=None):
        self.name = name
        self.breed = breed
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

dog1 = Dog('Шарик', 'Дворняга', 5)
print(dog1.get_name())
print(dog1.get_breed())
print(dog1.get_age())
dog1.set_breed('Овчарка')
print(dog1.get_breed())

# 5. Сотрудники компании
print('\n5. Сотрудники компании')

employees = [
    {"name": "Анна Смирнова", "department": "IT", "salary": 120000, "age": 28, "experience": 5},
    {"name": "Иван Петров", "department": "Sales", "salary": 95000, "age": 35, "experience": 10},
    {"name": "Мария Иванова", "department": "HR", "salary": 85000, "age": 42, "experience": 15},
    {"name": "Дмитрий Сидоров", "department": "IT", "salary": 150000, "age": 31, "experience": 7},
    {"name": "Елена Козлова", "department": "Sales", "salary": 110000, "age": 29, "experience": 6},
    {"name": "Сергей Михайлов", "department": "IT", "salary": 90000, "age": 24, "experience": 2},
    {"name": "Ольга Новикова", "department": "HR", "salary": 95000, "age": 38, "experience": 12},
    {"name": "Алексей Федоров", "department": "Sales", "salary": 130000, "age": 33, "experience": 8},
    {"name": "Татьяна Морозова", "department": "IT", "salary": 140000, "age": 36, "experience": 9},
    {"name": "Константин Васильев", "department": "Sales", "salary": 88000, "age": 26, "experience": 3},
    {"name": "Наталья Павлова", "department": "HR", "salary": 105000, "age": 45, "experience": 18},
    {"name": "Максим Соколов", "department": "IT", "salary": 160000, "age": 29, "experience": 6}
]

sorted_by_salary = sorted(employees, key=lambda x: x["salary"], reverse=True)

sorted_by_age = sorted(employees, key=lambda x: x["age"])

print(sorted_by_salary)
print(sorted_by_age)
