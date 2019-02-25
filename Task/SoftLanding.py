import numpy as np
import gym

class SoftLanding():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos=None):
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.env = gym.make('LunarLander-v2')
        self.action_repeat = 3
        self.init_pose = self.env.reset()
        
        # state made of current position, velocity and angular velocity
        self.state_size = self.action_repeat * 6
        #Numbers defined for takeoff and also to prevent the agent from having 2 motors in max and two in zero
        self.action_low = -1.0
        self.action_high = 1.0
        self.action_size = 4

        # Goal
        self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.]) 

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        
        
        return (reward)

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        state_all = []
        for _ in range(self.action_repeat):
            #done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            reward += self.get_reward() 
            state_all.append(self.env.state)
        next_state = np.concatenate(state_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        state = self.env.reset()
        #state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state