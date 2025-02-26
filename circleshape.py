import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:   
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, other):
        r1 = self.radius
        r2 = other.radius

        distance = self.position.distance_to(other.position)

        if distance < (r1 + r2):
            return True
        else:
            return False

    def draw(self, screen):
        #sub-classes must override
        pass
    
    def update(self, dt):
        #sub-classes must override
        pass