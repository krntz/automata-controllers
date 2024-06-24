import logging
import time

from .controller import Controller
from .utils.utils import FlightZone

logger = logging.getLogger(__name__)

"""
Simulated automata controller, acts just like the crazyflieController but
without the need for drone. Useful for testing/development.
"""

class SimulatedController(Controller):
    """
    Controller class for setting up, managing, and shutting down swarms of Crazyflies
    """

    def __init__(self,
                 uris,
                 flight_zone,
                 config):
        super().__init__(uris, flight_zone)

        self.swarm_flying = False
        self._PHYSICAL = False

    def __enter__(self):
        logger.debug("Starting swarm")

        self.swarm_flying = False

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug("Shutting down swarm")

        self.swarm_flying = False

    def swarm_take_off(self):
        logger.debug("Trying to run take off sequence")

        if not self.swarm_flying:
            logger.info("Swarm is taking off")
            self.swarm_flying = True
            time.sleep(2)
            logger.info("Swarm is flying")
        else:
            raise RuntimeError("Swarm is already flying")

    def swarm_land(self, emergency_land=False):
        if self.swarm_flying or emergency_land:
            logger.info("Landing swarm")
            self.swarm_flying = False
        else:
            raise RuntimeError("Swarm has already landed!")

    def swarm_move(self, positions, yaw, time_to_move, relative):
        if not self.swarm_flying:
            raise RuntimeError("Swarm must be flying to be moved")

        if time_to_move == None:
            raise ValueError("time_to_move must be set for physical and simulated systems")

        logger.info("Moving swarm")
        time.sleep(time_to_move)

    def set_swarm_velocities(self, velocities, yaw_rate):
        raise NotImplementedError()
