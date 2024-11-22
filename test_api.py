import data
import configuration
import requests

# Функция: создать заказ
def create_order(order_body):
    response = requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=order_body)
    track = response.json().get("track")
    print(f"Order track number: {track}")
    return response

# Функция: получить заказ по треку
def get_order_by_track(order_track_number):
    response = requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + str(order_track_number))
    print(f"Response code: {response.status_code}")
    return response

# Сохраняем номер заказа
order_response = create_order(data.order_body)
order_track_number = order_response.json().get("track")

# получение данных о заказе по его треку
def test_get_order_by_track():
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200
