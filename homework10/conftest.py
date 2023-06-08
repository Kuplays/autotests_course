import pytest
from datetime import datetime
import time


@pytest.fixture(scope='class')
def start_time():
    """Дата начала и окончания"""
    start = datetime.now()
    print(f'\nСтартовали {start}')
    yield
    end = datetime.now()
    print(f'\nЗавершили {end}')


@pytest.fixture()
def run_time():
    """Время выполнения в секундах"""
    start = time.time()
    yield
    end = time.time()
    print(f' Выполнили за: {end - start} секунд')
