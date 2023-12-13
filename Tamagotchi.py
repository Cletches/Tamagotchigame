import random
import numpy


class Tamagotchi(object):
    """
    A class representing a Tamagotchi virtual pet.

    Attributes:
    name (str): The name of the Tamagotchi.
    fullness (int): The fullness level of the Tamagotchi.
    happiness (int): The happiness level of the Tamagotchi.
    cleanliness (int): The cleanliness level of the Tamagotchi.
    alive (bool): Indicates if the Tamagotchi is alive.
    stage (str): The current stage of the Tamagotchi (egg, baby, child, adult).
    progress (int): The progress towards the next stage.
    """

    stage = ["egg", "baby", "child", "adult"]

    def __init__(self, name: str):
        """
        Initializes a Tamagotchi instance with the given name and default attribute values.
        Parameters:name (str): The name of the Tamagotchi.
        """
        self.name = name
        self.fullness = 8
        self.happiness = 8
        self.cleanliness = 8
        self.alive = True
        self.stage = "egg"
        self.progress = 1

    def feed(self):
        """
        Increases the fullness level of the Tamagotchi by 3, but decreases cleanliness if fullness is already at the maximum.
        """
        if self.fullness < 10:
            self.fullness += 3
            if self.fullness > 10:
                self.fullness = 10
        else:
            self.cleanliness -= 2
            if self.cleanliness < 1:
                self.cleanliness = 1

    def play(self):
        """
        Increases the happiness level of the Tamagotchi by 3, but decreases fullness if happiness is already at the maximum.
        """
        if self.happiness < 10:
            self.happiness += 3
            if self.happiness > 10:
                self.happiness = 10
        else:
            self.fullness -= 2
            if self.fullness < 1:
                self.fullness = 1

    def bathe(self):
        """
        Increases the cleanliness level of the Tamagotchi by 3, but decreases happiness if cleanliness is already at the maximum.
        """
        if self.cleanliness < 10:
            self.cleanliness += 3
            if self.cleanliness > 10:
                self.cleanliness = 10
        else:
            self.happiness -= 2
            if self.happiness < 1:
                self.happiness = 1

    def age_up(self):
        """
        Advances the Tamagotchi to the next stage and resets the progress.
        """
        self.stage = Tamagotchi.stage[Tamagotchi.stage.index(self.stage) + 1]
        self.progress = 1

    def status(self):
        """
        Returns the status of the Tamagotchi based on its levels.
        Returns:str: The status of the Tamagotchi ("fine", "dead", or "distress").
        """

        if self.fullness > 5 and self.happiness > 5 and self.cleanliness > 5:
            return "fine"
        elif self.fullness == 1 or self.happiness == 1 or self.cleanliness == 1:
            self.alive = False
            return "dead"
        elif self.fullness <= 5 or self.happiness <= 5 or self.cleanliness <= 5:
            return "distress"

    def time_step(self):
        """
        Simulates the passage of time, updating levels and checking for stage progression.
        Returns:
        str: The status of the Tamagotchi after the time step.
        """
        choosing = numpy.random.choice(self.happiness, self.fullness, self.cleanliness)
        choosing -= 1
        self.progress += 1
        if self.progress == 20:
            self.age_up()
        return self.status()


def main():
    pet = Tamagotchi("Goku")
    pet.bathe()
    pet.play()
    pet.feed()
    print(f'fullness Goku : ', pet.fullness)
    print(f'cleanliness Goku : ', pet.cleanliness)
    print(f'happiness Goku: ', pet.happiness)

    pet2 = Tamagotchi("Gohan")
    pet2.bathe()
    pet2.play()
    pet2.feed()
    pet2.feed()
    pet2.bathe()
    pet2.play()
    print(f'fullness Gohan : ', pet2.fullness)
    print(f'cleanliness Gohan : ', pet2.cleanliness)
    print(f'happiness Gohan : ', pet2.happiness)

    print(pet.stage)
    pet.age_up()
    pet.age_up()
    pet.age_up()
    print(pet.stage)
    pass

    pet3 = Tamagotchi("Vegeta")
    pet3.fullness = 6
    pet3.happiness = 6
    pet3.cleanliness = 6
    print(pet3.status())

    pet3 = Tamagotchi("Vegeta")
    pet3.fullness = 6
    pet3.happiness = 6
    pet3.cleanliness = 3
    print(pet3.status())

    pet3 = Tamagotchi("Vegeta")
    pet3.fullness = 1
    pet3.happiness = 6
    pet3.cleanliness = 3
    print(pet3.status())


if __name__ == "__main__":
    main()
