from urllib.parse import urljoin

class Urls:
    # Базовый URL — единственная точка изменения для разных стендов
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    # Строим остальные URL на основе базового
    scooter_home_url = urljoin(BASE_URL, '/')
    scooter_order_url = urljoin(BASE_URL, '/order')
    scooter_status_url = urljoin(BASE_URL, '/track')

    # Домены для проверок редиректов (остаются без изменений)
    dzen_domain = 'dzen.ru'
    yandex_search = 'ya.ru'
    yandex_domain = 'yandex.ru'
