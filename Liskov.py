class Bird:
    def fly(self):
        print("I can fly!")

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("I can't fly!")

def let_bird_fly(bird):
    bird.fly()

let_bird_fly(Sparrow())  
let_bird_fly(Ostrich()) 
