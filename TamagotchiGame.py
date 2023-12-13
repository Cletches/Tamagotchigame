import turtle
import time
from Tamagotchi import Tamagotchi


class TamagotchiGame(object):
    """
    Game engine to play with the Tamagotchi pet.
    """
    # Explore changing these values and how the game interaction is affected.
    action_delay = 2
    time_step_delay = 3

    def __init__(self, name: str):
        """Creates a Tamagotchi Pet with the given name"""
        self.pen = turtle.Turtle()
        self.pen.up()
        self.pen.hideturtle()
        turtle.tracer(0, 0)
        self.pet = Tamagotchi(name)

    @staticmethod
    def fill_circle(a_turtle: turtle, color: str, radius: float, position: tuple):
        """
        To draw a circle
        :param a_turtle: a turtle object
        :param color: a color to fill the circle
        :param radius: radius of the circle
        :param position: center of circle is radius units left of the turtle position
        :return:
        """
        a_turtle.up()
        a_turtle.color('black')
        a_turtle.goto(position)
        a_turtle.down()
        a_turtle.fillcolor(color)
        a_turtle.begin_fill()
        a_turtle.circle(radius)
        a_turtle.end_fill()
        a_turtle.up()
        a_turtle.goto(0, 0)

    def draw_egg(self):
        """
        Draws the first stage.
        :return: None
        """
        TamagotchiGame.fill_circle(self.pen, "green", 20, (0, 0))
        TamagotchiGame.fill_circle(self.pen, "white", 5, (10, 20))
        TamagotchiGame.fill_circle(self.pen, "white", 5, (-10, 20))
        TamagotchiGame.fill_circle(self.pen, "black", 2, (10, 22))
        TamagotchiGame.fill_circle(self.pen, "black", 2, (-10, 22))
        turtle.update()

    def draw_baby(self):
        """
        Draws the second stage.
        :return: None
        """
        TamagotchiGame.fill_circle(self.pen, "red", 10, (15, 0))
        TamagotchiGame.fill_circle(self.pen, "red", 10, (-15, 0))
        TamagotchiGame.fill_circle(self.pen, "red", 30, (0, 0))
        TamagotchiGame.fill_circle(self.pen, "white", 8, (15, 30))
        TamagotchiGame.fill_circle(self.pen, "white", 8, (-15, 30))
        TamagotchiGame.fill_circle(self.pen, "black", 4, (15, 34))
        TamagotchiGame.fill_circle(self.pen, "black", 4, (-15, 34))
        turtle.update()

    def draw_child(self):
        """
        Draws the third stage.
        :return: None
        """
        TamagotchiGame.fill_circle(self.pen, "purple", 14, (20, 0))
        TamagotchiGame.fill_circle(self.pen, "purple", 14, (-20, 0))
        TamagotchiGame.fill_circle(self.pen, "purple", 10, (40, 40))
        TamagotchiGame.fill_circle(self.pen, "purple", 10, (-40, 40))
        TamagotchiGame.fill_circle(self.pen, "purple", 40, (0, 0))
        TamagotchiGame.fill_circle(self.pen, "white", 10, (15, 40))
        TamagotchiGame.fill_circle(self.pen, "white", 10, (-15, 40))
        TamagotchiGame.fill_circle(self.pen, "black", 5, (15, 44))
        TamagotchiGame.fill_circle(self.pen, "black", 5, (-15, 44))
        turtle.update()

    def draw_adult(self):
        """
        Draws the fourth stage
        :return: None
        """
        TamagotchiGame.fill_circle(self.pen, "blue", 18, (25, 0))
        TamagotchiGame.fill_circle(self.pen, "blue", 18, (-25, 0))
        TamagotchiGame.fill_circle(self.pen, "blue", 12, (50, 50))
        TamagotchiGame.fill_circle(self.pen, "blue", 12, (-50, 50))
        TamagotchiGame.fill_circle(self.pen, "blue", 50, (0, 0))
        TamagotchiGame.fill_circle(self.pen, "purple", 5, (0, 35))
        TamagotchiGame.fill_circle(self.pen, "white", 12, (15, 50))
        TamagotchiGame.fill_circle(self.pen, "white", 12, (-15, 50))
        TamagotchiGame.fill_circle(self.pen, "black", 6, (15, 55))
        TamagotchiGame.fill_circle(self.pen, "black", 6, (-15, 55))
        turtle.update()

    def draw_tombstone(self):
        """
        Draws the stage if pet dies.
        :return: None
        """
        self.pen.fillcolor("gray")
        self.pen.begin_fill()
        self.pen.forward(50)
        for i in range(2):
            self.pen.left(90)
            self.pen.forward(200)
            self.pen.left(90)
            self.pen.forward(100)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(0, 160)
        self.pen.write("RIP", align="center", font=("Arial", 20, "normal"))
        self.pen.goto(0, 140)
        self.pen.write(self.pet.name, align="center", font=("Arial", 15, "normal"))
        self.pen.goto(0, 0)
        turtle.update()

    def display(self, action=""):
        """
        To display the name, status and parameters of the pet, as well as to evolve the pet.
        :param action: if user feeds, plays or bathes the pet
        :return: None
        """
        self.pen.clear()
        self.pen.up()
        self.pen.goto(0, -30)
        self.pen.color('black')
        self.pen.write(f'{self.pet.name}: {self.pet.status()} '
                       f'(F:{self.pet.fullness},H:{self.pet.happiness},C:{self.pet.cleanliness})',
                       align="center", font=("Arial", 20, "normal"))
        turtle.update()
        self.pen.goto(0, 0)
        if self.pet.stage == "egg":
            self.draw_egg()
        elif self.pet.stage == "baby":
            self.draw_baby()
        elif self.pet.stage == "child":
            self.draw_child()
        else:
            self.draw_adult()
        if self.pet.status() == "distress" and action == "":
            self.pen.goto(0, 100)
            self.pen.color('red')
            self.pen.write("WWAHHHH!! :(", align="center", font=("Arial", 30, "normal"))
            self.pen.goto(0, 0)
        turtle.update()

    def feed(self):
        """
        Action to feed the pet.
        :return: None
        """
        self.display(action='feed')
        self.pet.feed()
        self.pen.goto(0, 100)
        self.pen.color('black')
        self.pen.write("NOM NOM NOM", align="center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0, 0)
        time.sleep(self.action_delay)
        self.display()

    def play(self):
        """
        Action to play with the pet.
        :return: None
        """
        self.display(action='play')
        self.pet.play()
        self.pen.goto(0, 100)
        self.pen.color('black')
        self.pen.write("WEEEEE!!!!!", align="center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0, 0)
        time.sleep(self.action_delay)
        self.display()

    def bathe(self):
        """
        Action to bathe the pet.
        :return: None
        """
        self.display(action='bathe')
        self.pet.bathe()
        self.pen.goto(0, 100)
        self.pen.color('black')
        self.pen.write("SCRUB SCRUB SCRUB", align="center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0, 0)
        time.sleep(self.action_delay)
        self.display()

    def run(self) -> None:
        """Runs the Tamagotchi game"""
        self.display()
        time.sleep(2)
        state = self.pet.time_step()
        while state != "dead":
            self.display()
            self.pen.goto(0, -50)
            self.pen.color('purple')
            self.pen.write("Type 1 to feed, 2 to play, 3 to bathe", align="center", font=("Arial", 15, "normal"))
            turtle.update()
            self.pen.goto(0, 0)
            turtle.listen()
            turtle.onkey(self.feed, "1")
            turtle.onkey(self.play, "2")
            turtle.onkey(self.bathe, "3")
            time.sleep(self.time_step_delay)
            state = self.pet.time_step()
        self.pen.clear()
        self.draw_tombstone()
        turtle.exitonclick()


def main():
    game = TamagotchiGame('Goku')
    game.run()


if __name__ == "__main__":
    main()
