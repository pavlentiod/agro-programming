import time

from pioneer_sdk import Pioneer

from src import launch

def fly_task():
    """
    Функция полёта квадрокоптера.

    Здесь необходимо реализовать:
    - взлёт;
    - облёт всей площадки размером 3×3 м (шаг сетки 1 м);
    - сканирование ArUco-маркеров (происходит автоматически);
    - возврат в начальную точку;
    - приземление.

    Используйте методы:
        drone.arm()
        drone.takeoff()
        drone.go_to_local_point(x, y, z, yaw)
        drone.land()

    Подробнее: https://docs.geoscan.ru/pioneer/programming/python/pioneer-sdk-methods.html
    """

    drone = Pioneer()

    # TODO: Запрограммируйте здесь логику полёта
    # Пример начала:
    # drone.arm()
    # drone.takeoff()
    # time.sleep(3)
    # drone.go_to_local_point(0, 0, 1, 0.0)
    # ...
    # drone.land()
    pass

if __name__ == '__main__':
    launch(fly_task)
