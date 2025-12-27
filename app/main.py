class Animal:
    def __init__(self, name, appetite, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry


    def print_name(self):
        print(f"Hello, I'm {self.name}")


    def feed(self):
        if self.is_hungry == True:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name, is_hungry):
        super().__init__(name, is_hungry, appetite=3)



    def catch_mouse(self):
        print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry):
        super().__init__(name, is_hungry, appetite=7)



    def bring_slippers(self):
        print("The slippers delivered!")



def feed_animals(animals):
        return sum(animal.feed() for animal in animals)
