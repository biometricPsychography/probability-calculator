import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **balls) :
        self.contents = []
        for key in balls :
            i = 0
            while i < balls[key] :
                self.contents.append(key)
                i += 1

        print(self.contents)

    def draw(self, num_to_draw) :
        random.randint(0, len(self.contents))

Hat(blue=2, red=5)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass