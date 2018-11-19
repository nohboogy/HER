import numpy as np
from baselines.her.rollout import RolloutWorker
import gym.envs.robotics.fetch_env

class Distance_calc:

    def goal_distance(goal_a, goal_b):
        assert goal_a.shape == goal_b.shape
        return np.linalg.norm(goal_a - goal_b, axis=-1)


    def count_success(self):