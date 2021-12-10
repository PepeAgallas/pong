from typing import Tuple

import pygame
from pygame.mixer import Sound

from constants.window import SCREEN_HEIGHT, SCREEN_WIDTH
from entities.entity import Entity
from entities.player import Player


class Ball(Entity):
    x_speed: int = 5
    y_speed: int = 5
    size: Tuple[float, float] = (30, 30)
    pong_sfx: Sound

    def __init__(
            self, position: Tuple[float, float],
    ) -> None:
        super().__init__(position, self.size)
        self.__load_resources()

    def __update__(self) -> None:
        self.__bounce()

    def __bounce(self) -> None:
        self.x += self.x_speed
        self.y += self.y_speed

        if self.top <= 0 or self.bottom >= SCREEN_HEIGHT:
            self.y_speed *= -1
            self.pong_sfx.play()
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.x_speed *= -1
            self.pong_sfx.play()

    def collide(self, pad: Player) -> None:
        # Check for collision
        if self.colliderect(pad):
            self.pong_sfx.play()
            self.x_speed *= -1

    def __load_resources(self):
        # Sound Effects
        self.pong_sfx = pygame.mixer.Sound("../resources/sfx/pong.wav")
