class Robots():
    """ Represents a robot, with a name. """
    poplutions = 0

    def __init__(self, name):
        """ Initializes the data. """
        self.name = name
        print(f"(Initializing {self.name})")


        # When The Person Is Created Robot
        # adds to Poplutions
        new_Robot = Robots.poplutions
        new_Robot += 1

        # if The Robot Dosent Work
    def die(self):
        """I'am, Daying"""
        print(f"{self.name} s being destroyed!")

        Robots.poplutions -= 1

        if Robots.poplutions == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robots.population))
