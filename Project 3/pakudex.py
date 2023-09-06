from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity  # initial value is 20
        self.pakuris = []  # store a list of pakuri objects
        self.size = 0  # keep track of the # of concrete pakuri object in self.pakuris

    # species vs. pakuri object
    def add_pakuri(self, species):
        # 1. check duplicates => return False
        # loop through self.pakuris to look at each pakuri object
        # compare pakuri.species == species
        # if str(species) in self.get_species_array():
        for x in self.pakuris:
            if species in self.get_species_array():
                print("Error: Pakudex already contains this species!")
                return False
            elif self.size == self.capacity:
                return False
            else:
                continue
        self.pakuris.append(Pakuri(species))
        self.size += 1
        return True


    def get_species_array(self):
        res = []
        if len(self.pakuris) == 0:
            return None
        else:
            for x in self.pakuris:
                res.append(str(x.species))
            return (res)
        # loop through self.pakuris to look at each pakuri object
        # append pakuri.species to the res

    def get_stats(self, species):

        # loop through self.pakuris to look at each pakuri object
        # compare pakuri.species == species
        # if true, return [pakuri.attack, pakuri.defense, pakuri.speed]
        for x in self.pakuris:
            if str(x.species) == str(species):
                return [x.attack, x.defense, x.speed]
        else:
            return None

    def get_size(self):
        self.size = len(self.pakuris)
        return self.size

    def get_capacity(self):
        return self.capacity

    def sort_pakuri(self):
        self.pakuris.sort()

    def evolve_species(self, species):
        for x in self.pakuris:
            if x.species == species:
                Pakuri.evolve(x)
                return True
        else:
            return False
