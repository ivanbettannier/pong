import pong
import gym
from gym.spaces import Box, Discrete
import numpy as np
import pygame

class PongEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 30}
    def __init__(self, render_mode=None):
        self.pong_game = pong.Pong()
        width = self.pong_game.play_area.settings.play_area_width
        height = self.pong_game.play_area.settings.play_area_height

        self.observation_space = Box(low=0, high=255, shape=(width, height, 3), dtype=np.uint8)
                                                                
        self.action_space = Discrete(2)

        assert render_mode is None or render_mode in self.metadata["render_modes"]

    def step(self,action):
        self.pong_game.step(action)
        info = None 

        player1_point = self.pong_game.stats.player1_point
        player2_point = self.pong_game.stats.player2_point

        reward = player1_point - player2_point

        terminated = (player1_point >= 5) or (player2_point >= 5)
        info = None

        obs = self._get_obs()

        return obs, reward, terminated, False, info 


    
    def _get_obs(self):
        pixarray =  pygame.surfarray.pixels3d(self.pong_game.screen)
        obs = pixarray.copy()
        del pixarray
        return obs
    
    def reset(self):
        super().reset()
        self.pong_game = pong.Pong()
        info = None

        if self.render_mode == "human":
            self._render_frame()


        obs = self._get_obs()

        return obs, info 
    
    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()
    
    def _render_frame(self):
        if self.render_mode == "human":
            pygame.display.update()

        else:
            return self._get_obs()
    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()




