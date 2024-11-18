class Planet:
    def __init__(self, name, radius, num_moons):
        self.name = name
        self.radius = radius
        self.num_moons = num_moons

    def collide(self):
        self.num_moons += 1

earth = Planet("Earth", 6371, 1)
jupiter = Planet("Jupiter", 69911, 79)