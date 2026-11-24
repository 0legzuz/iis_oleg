# отправляет случайные примеры пациентов. Каждый десятый запрос специально некорректный, чтобы проверить учёт ошибок.


import json
import os
import random
import time
from itertools import count
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def sample():
    return {
        'age': random.randint(30, 77), 'sex': random.randrange(2),
        'cp': random.randrange(4), 'trestbps': random.randint(95, 175),
        'chol': random.randint(150, 340), 'fbs': random.randrange(2),
        'restecg': random.randrange(3), 'thalach': random.randint(85, 195),
        'exang': random.randrange(2), 'oldpeak': round(random.uniform(0, 5), 1),
        'slope': random.randrange(3), 'ca': random.randrange(4), 'thal': random.randint(1, 3),
    }


def main():
    base = os.getenv('API_URL', 'http://ml_service:8000').rstrip('/')
    for item_id in count(1):
        # Каждый десятый запрос проверяет валидацию тела и даёт HTTP 422.
        body = None if item_id % 10 == 0 else sample()
        request = Request(f'{base}/api/prediction?item_id={item_id}',
                          data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
        try:
            with urlopen(request, timeout=10) as response:
                print(response.status, response.read().decode(), flush=True)
        except HTTPError as error:
            print(error.code, error.read().decode(), flush=True)
        except (URLError, TimeoutError) as error:
            print(f'Сервис недоступен: {error}', flush=True)
        time.sleep(random.uniform(0, 5))


if __name__ == '__main__':
    main()
