# test_app.py
import pytest
from app import app  # импортируем приложение из app.py

@pytest.fixture
def client():
    """Создаём клиент для тестирования Flask приложения"""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Тестируем домашнюю страницу"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data  # Проверка текста на странице
