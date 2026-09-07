import uuid


def generate_user_data():
    unique_id = uuid.uuid4().hex

    return {'email': f'liza_{unique_id}@yandex.ru', 'password': f'password_{unique_id}', 'name': f'Liza_{unique_id}'}