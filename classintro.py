i = 5
def f():
    j = 10
    print (j)

f()
class Apple:  # class, concept
    type = "fruit"
    def __init__(self, loc = "tree", clr = "red"):
        self._location = loc
        self._color = clr

    def _setlocation(self, l):
        self._location = l

    def drop(self):
        if self._location == "tree":
            self._setlocation("ground")
            print ("I dropped")
        else:
            print ("I connot be dropped")

x = Apple("tree", "red") # object, tangible, implicitely calls __init__
y = Apple()
z = Apple(clr="yellow")

# z._color = "black" # access to member variable. should not be allowed.
z.drop() # if I designate drop function as public then ok. otherwise should not be allowed.

x.drop() # Actually calls Apple.drop(x)

print (x.type)


