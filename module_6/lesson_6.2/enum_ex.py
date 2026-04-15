from enum import Enum

class Semaphore:
    RED = 1
    YELLOW = 2
    GREEN = 3


def status_light(light):
    match light:
        case Semaphore.RED:
            print('You must stop')
        case Semaphore.YELLOW:
            print('Be patient')
        case Semaphore.GREEN:
            print('You must go!')

status_light(Semaphore.GREEN)
status_light(Semaphore.RED)
status_light(Semaphore.YELLOW)



