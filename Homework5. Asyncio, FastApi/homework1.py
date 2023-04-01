import asyncio
import aiohttp
import json


async def fetch_data(url, session):
    async with session.get(url) as response:
        data = await response.json()
        return data


async def get_data():
    async with aiohttp.ClientSession() as session:
        # Запрос данных о пользователях
        url = 'https://jsonplaceholder.typicode.com/users'
        data = await fetch_data(url, session)
        with open('file/users_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о постах
        url = 'https://jsonplaceholder.typicode.com/posts'
        data = await fetch_data(url, session)
        with open('file/posts_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о комментариях
        url = 'https://jsonplaceholder.typicode.com/comments'
        data = await fetch_data(url, session)
        with open('file/comments_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о фотографиях
        url = 'https://jsonplaceholder.typicode.com/photos'
        data = await fetch_data(url, session)
        with open('file/photos_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о задачах
        url = 'https://jsonplaceholder.typicode.com/todos'
        data = await fetch_data(url, session)
        with open('file/todos_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных об альбомах
        url = 'https://jsonplaceholder.typicode.com/albums'
        data = await fetch_data(url, session)
        with open('file/albums_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о постерах
        url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
        data = await fetch_data(url, session)
        with open('file/posters_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о фотоальбомах
        url = 'https://jsonplaceholder.typicode.com/albums/1/photos'
        data = await fetch_data(url, session)
        with open('file/photo_albums_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о задачах для пользователя
        url = 'https://jsonplaceholder.typicode.com/users/1/todos'
        data = await fetch_data(url, session)
        with open('file/user_todos_data.txt', 'w') as f:
            f.write(json.dumps(data))

        # Запрос данных о постах пользователя
        url = 'https://jsonplaceholder.typicode.com/users/1/posts'
        data = await fetch_data(url, session)
        with open('file/user_posts_data.txt', 'w') as f:
            f.write(json.dumps(data))

loop = asyncio.get_event_loop()
loop.run_until_complete(get_data())