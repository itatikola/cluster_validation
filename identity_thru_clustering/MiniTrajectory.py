'''
A class used to contain metadata about a trajectory - a collection of 10 consecutive frames
Each frame contains a full Assembly of 9 key points

'''

import numpy as np


class MiniTrajectory:

    def __init__(self, hdf_path, assemblies):
        '''
        Initializing the MiniTrajectory object
        :param hdf_path (str): the original file the trajectory is from
        :param assemblies (DataFrame): the contiguous set of assemblies that constitute the Trajectory
        '''
        if assemblies.index.length > 10:
            raise ValueError("A MiniTrajectory is only 10 frames or less.")
        self.original_hdf = hdf_path
        self.assemblies = assemblies
        self.start_frame = assemblies.index[0]
        self.end_frame = assemblies.index[-1]

    def displacement(self):
        '''
        :return: the displacement of the fish
        '''
        if self.assemblies is None:
            raise ValueError("Trajectory does not have a set of Assemblies.")
        first = self.assemblies.iloc[0]
        last = self.assemblies.iloc[-1]
        vec1 = np.array([first.__getitem__(first.index[0]),
                         first.__getitem__(first.index[1])])
        vec2 = np.array([last.__getitem__(last.index[0]),
                         last.assembly.__getitem__(last.index[1])])

        return np.linalg.norm(vec2 - vec1)

    def speed(self):
        '''
        :return: the instantaneous speed of the fish
        '''
        return self.displacement() / self.assemblies.index.length

    def direction(self):
        '''
        :return: a vector object representing the direction that the fish is moving in
                This is also the direction from stripe1 to nose
        '''






