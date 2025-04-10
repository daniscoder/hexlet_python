# 2. Синтаксис
def make_user(name, age):
    return {'name': name, 'age': age}

def format_user(user):
    return f'{user['name']}, {user['age']}'

phil = make_user('Phil', 25)
print(format_user(phil))
# Phil, 25