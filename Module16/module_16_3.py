# -*- coding: utf-8 -*-

# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Цель: выработать навык работы с CRUD запросами.
#
# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.

# post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username},
# возраст: {age}". И возвращает строку "User <user_id> is registered".

# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id на строку "Имя: {username},
# возраст: {age}". И возвращает строку "The user <user_id> is registered"

# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.

# Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
# 1. GET '/users'
# {
# "1": "Имя: Example, возраст: 18"
# }
# 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
# "User 2 is registered"
# 3. POST '/user/{username}/{age}' # username - NewUser, age - 22
# "User 3 is registered"
# 4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
# "User 1 has been updated"
# 5. DELETE '/user/{user_id}' # user_id - 2
# "User 2 has been deleted"
# 6. GET '/users'
# {
# "1": "Имя: UrbanProfi, возраст: 28",
# "3": "Имя: NewUser, возраст: 22"
# }

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple='24')]) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple='24')],
                      user_id: int=Path(ge=1, le=100, description="Enter User ID", example='16')) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    del users[user_id]
    return f"User {user_id} has been deleted"