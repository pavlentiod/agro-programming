import time

from pioneer_sdk import Pioneer

from src import launch


def fly_task():
    drone = Pioneer()
    height = 1
    yaw = 0.0

    drone.arm()
    drone.takeoff()
    time.sleep(3)

    cols = 3
    rows = 3
    cell_size = 1
    for col in range(0, cols):
        for row in range(0, rows):
            if col % 2 == 0:
                drone.go_to_local_point(-col * cell_size, row * cell_size, height, yaw)
            else:
                drone.go_to_local_point(-(cols - col - 1) * cell_size, row * cell_size, height, yaw)
            time.sleep(6)
    drone.go_to_local_point(0, 0, height, yaw)
    time.sleep(5)
    drone.land()


if __name__ == '__main__':
    launch(fly_task)
