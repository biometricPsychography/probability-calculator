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


    def draw(self, num_to_draw) :
        if num_to_draw > len(self.contents) :
            num_to_draw = len(self.contents)

        drawn_list = []
        i = 0
        while i < num_to_draw :
            
            pop_index = random.randint(0, len(self.contents) - 1)
            drawn_list.append(self.contents.pop(pop_index))
            i += 1
        
        return drawn_list
            
                    

hat = Hat(blue=2, red=5)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    positive_experiments = 0
    i = 0
    
    while i < num_experiments :
        hat_copy = copy.deepcopy(hat)
        drawn_balls_list = hat_copy.draw(num_balls_drawn)
        print(drawn_balls_list)
        drawn_balls_obj = {}
        for ball in drawn_balls_list :
            if ball not in drawn_balls_obj :
                drawn_balls_obj[ball] = 1
            else :
                drawn_balls_obj[ball] += 1
        
        is_expectation_fulfilled = True
        for key in expected_balls :
            if key not in drawn_balls_obj or expected_balls[key] > drawn_balls_obj[key] :
                is_expectation_fulfilled = False
                break
                
        if is_expectation_fulfilled :
            positive_experiments += 1
        
        i += 1

    return positive_experiments / i

# x = experiment(hat=hat,
#             expected_balls={"red":1},
#             num_balls_drawn=5,
#             num_experiments=5)
# print(x)