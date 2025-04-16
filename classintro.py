class Fruit:
    def __init__(self, loc, clr):
        self._location = loc
        self._color = clr

    def _setlocation(self, l):
        self._location = l

    def fruitName(self):
        pass

    def drop(self):
        if self._location == "tree":
            self._setlocation("ground")
            print ("I am a" + self.fruitName() + " and I dropped")
        else:
            print ("I am a" + self.fruitName() + " and I connot be dropped")

class Apple(Fruit):  # class, concept
    def __init__(self, clr = "red"):
        super().__init__("tree", clr)

    def fruitName(self):
        return "Apple"

class Strawberry(Fruit):
    def __init__(self):
        super().__init__("ground", "red")

    def fruitName(self):
        return "Strawberry"


x = Apple("red") # object, tangible, implicitely calls __init__
x.drop()

y = Strawberry()
y.drop()

y = Apple()
z = Apple(clr="yellow")

# z._color = "black" # access to member variable. should not be allowed.
z.drop() # if I designate drop function as public then ok. otherwise should not be allowed.

x.drop() # Actually calls Apple.drop(x)

print (x.type)


