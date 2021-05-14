import os
import threading
import time
from client import Battleship
from log import logging, get_logger

logger = get_logger(__name__)
logger.setLevel(logging.INFO)


class PiBattleships:
    def __init__(self, _grpc_host, _grpc_port):
        self.__playing = threading.Event()
        self.__playing.set()

        # Create Battleships object and store in instance variable
        battleship = Battleship(grpc_host=_grpc_host, grpc_port=_grpc_port)
        self.__battleship = battleship

        # Register event handlers for various gRPC events
        battleship.add_event_listener(handler=self.begin)
        battleship.add_event_listener(handler=self.hit)
        battleship.add_event_listener(handler=self.miss)
        battleship.add_event_listener(handler=self.win)
        battleship.add_event_listener(handler=self.lose)
        battleship.add_event_listener(handler=self.attack)

    def begin(self):
        logger.info('BEGIN: Game started')

    def hit(self):
        logger.info('HIT: Our attack was uccessful')

    def miss(self):
        logger.info('MISS: Our attack was unsuccessful')

    def win(self):
        logger.info('WIN: I won')

    def lose(self):
        logger.info('LOSE: Opponent won')

    def attack(self, vector):
        vector = vector[0]
        logger.info(f'ATTACK: Attacked on {vector}')

    def play(self):
        self.__battleship.join()
        while self.__playing.is_set():
            time.sleep(1.0)


if __name__ == '__main__':
    grpc_host = os.getenv('GRPC_HOST', 'localhost')
    grpc_port = os.getenv('GRPC_PORT', '50051')

    pi_battleships = PiBattleships(grpc_host, grpc_port)
    pi_battleships.play()
