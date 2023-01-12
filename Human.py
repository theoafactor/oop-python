class Mammal():

    def __init__(self):
        print("This is the parent constructor")
    
    def breastfeed(self):
        pass

    def walk(self):
        print("Walking from parent")

    def run(self):
        pass


class Human(Mammal):

    def __init__(self):
        print("This is the child constructor")
        super().__init__()

    def walk(self):
        print("Walking from child")
        super().walk() 
    
    def talk():
        pass

human = Human()

human.walk()