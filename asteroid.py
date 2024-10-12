from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", center = self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def collides(self, other):
        return super().collides(other)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ran = random.uniform(20, 50)
            a1 = self.velocity.rotate(ran)
            a2 = self.velocity.rotate(-ran)
            newa1 = self.radius - ASTEROID_MIN_RADIUS
            newa2 = self.radius - ASTEROID_MIN_RADIUS
            as1 = Asteroid(self.position.x, self.position.y, newa1)
            as2 = Asteroid(self.position.x, self.position.y, newa2)
            as1.velocity = a1 * 1.2
            as2.velocity = a2
