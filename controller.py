import abc

import numpy as np


class Controller(abc.ABC):
    def __init__(self, uris: list, flight_zone: any) -> None:
        self.uris = uris

        self.flight_zone = flight_zone

        self._positions = {uri: np.zeros(3) for uri in self.uris}

    @property
    def PHYSICAL(self):
        """Denotes whether the system is physical or not"""

        return self._PHYSICAL

    @property
    def positions(self):
        """The positions of the drones in the system"""

        return self._positions

    @abc.abstractmethod
    def swarm_land(self, emergency_land=False):
        """Cleanly shut down the representation"""
        # TODO: Should probably be renamed

    @abc.abstractmethod
    def swarm_move(self):
        """Broadcast positions for each drone to move to"""

    @abc.abstractmethod
    def set_swarm_velocities(self):
        """Set the velocities for x, y, and z of each drone in the swarm"""

    def distance_to_2D_point(self, uid, point):
        """
        Returns 2D euclidean distance to the given point from the drone with the given UID

        This is useful if you don't care about any difference in height

        If the drone's position has 3 coordinates, the z coordinate will be ignored
        """

        drone_position = self.positions[uid]

        if drone_position.shape[0] == 3:
            drone_position = drone_position[0:2]

        return np.linalg.norm(drone_position - point)

    def distance_to_point(self, uid, point):
        """
        Returns the euclidean distance to the given point from the drone with the given UID
        """

        return np.linalg.norm(self.positions[uid] - point)

    def distance_to_swarm(self, uid):
        """
        Returns a list of distances between the drone with the given UID and
        every other drone in the swarm
        """

        return [self.distance_to_point(self.positions[uid], pos) for pos in self.positions]
