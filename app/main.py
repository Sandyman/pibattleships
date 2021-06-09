from sense_hat import SenseHat
from time import sleep


def main():
    s = SenseHat()
    s.clear()
    s.set_rotation(270)
    s.show_message('Battleships 2021', 0.035)
    sleep(0.5)
    s.show_message('LET\'S GO!', 0.040)


if __name__ == '__main__':
    main()
