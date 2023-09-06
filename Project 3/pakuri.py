class Pakuri:
    def __init__(self, species):
        self.species = species
        self.attack = ((len(str(species))) * 7) + 9
        self.defense = ((len(str(species))) * 5) + 17
        self.speed = ((len(str(species))) * 6) + 13

    # getters and setters
    # getters: retrieve the value of an attribute
    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def set_attack(self, new_attack):
        self.attack = new_attack

    # setters: set the value of a specific attribute
    def set_species(self, new_species):
        self.species = new_species

    def evolve(self):
        # update self.attack, self.defense, self.speed
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3
        return [self.attack, self.defense, self.speed]

    # possible way to solve
    def __lt__(self, other):
        if isinstance(self, Pakuri):
            return self.species < other.species
