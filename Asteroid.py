from CircleShape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        asteroids_angle = random.uniform(20,50)
        first_asteroids_velocity = self.velocity.rotate(asteroids_angle) * 1.2
        second_asteroids_velocity = self.velocity.rotate(-asteroids_angle)  * 1.2

        child_radius = self.radius - ASTEROID_MIN_RADIUS

        first_child_asteroid = Asteroid(self.position[0], self.position[1], child_radius)
        second_child_asteroid = Asteroid(self.position[0], self.position[1], child_radius)

        first_child_asteroid.velocity = first_asteroids_velocity
        second_child_asteroid.velocity = second_asteroids_velocity