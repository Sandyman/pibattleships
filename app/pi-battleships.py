import os
import threading
import time
from client import Battleship
from log import logging, get_logger
from attack_status import AttackStatus


logger = get_logger(__name__)
logger.setLevel(logging.INFO)


class PiBattleship:
    def __init__(self, _grpc_host, _grpc_port):
        self.__playing = threading.Event()
        self.__playing.set()

        # Create Battleships object and store in instance variable
        battleship = Battleship(grpc_host=_grpc_host, grpc_port=_grpc_port)
        self.__battleship = battleship

        # Register event handlers for various gRPC events
        battleship.add_event_listener(handler=self.begin_event)
        battleship.add_event_listener(handler=self.hit_event)
        battleship.add_event_listener(handler=self.miss_event)
        battleship.add_event_listener(handler=self.win_event)
        battleship.add_event_listener(handler=self.lose_event)
        battleship.add_event_listener(handler=self.attack_event)

        # Register the status update handlers
        self.__status_handlers = {
            AttackStatus.HIT: battleship.hit,
            AttackStatus.MISS: battleship.miss,
            AttackStatus.DEFEAT: battleship.defeat,
        }

    def begin_event(self):
        logger.info('--BEGIN: Game started')

    def hit_event(self):
        logger.info('----HIT: Our attack was uccessful')

    def miss_event(self):
        logger.info('---MISS: Our attack was unsuccessful')

    def win_event(self):
        logger.info('----WIN: I won')
        self.__playing.clear()

    def lose_event(self):
        logger.info('---LOSE: Opponent won')
        self.__playing.clear()

    def attack_event(self, vector):
        vector = vector[0]
        logger.info(f'-ATTACK: Attacked on {vector}')

    def attack(self, vector):
        """Attack the opponents ships with a shot at {vector}.
        """
        pass

    def report_status(self, status):
        """Report the status of the shot fired by the opponent.
        """
        try:
            self.__status_handlers[status]()
        except KeyError:
            logger.error('Invalid status received. Ignoring.')

    def play(self):
        """Start the loop, which does nothing but sleep
        since we are only handling events.
        """
        self.__battleship.join()
        while self.__playing.is_set():
            time.sleep(1.0)

    def stop(self):
        """Stop the game by clearing the "Playing Event".
        """
        self.__playing.clear()


if __name__ == '__main__':
    grpc_host = os.getenv('GRPC_HOST', 'localhost')
    grpc_port = os.getenv('GRPC_PORT', '50051')

    pi_battleship = PiBattleship(grpc_host, grpc_port)
    pi_battleship.play()
