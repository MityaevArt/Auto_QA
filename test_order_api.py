# Митяев Максим, 24-я когорта — Финальный проект. Инженер по тестированию плюс

from order_api import create_order, get_order_by_track
import data

def test_create_and_get_order_by_track():
    # Создаем заказ
    order_response = create_order(data.order_body)
    assert order_response.status_code == 201  # Проверка успешного создания заказа

    # Получаем трек-номер
    order_track_number = order_response.json().get("track")
    assert order_track_number is not None  # Проверка, что трек-номер получен

    # Получаем данные заказа по трек-номеру
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200  # Проверка успешного получения заказа по треку
