class FOURZEROTHREE:
    year=2022
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def add_age(self):
        self.age= self.age+1

    def relocate(self,place):
        self.place=place

    def display(self):
        print("Year : "+str(FOURZEROTHREE.year))
        print("Name : "+self.name)
        print("Age : "+str(self.age))
        print("Place : "+self.place)
@classmethod
def add_year(cls):
    FOURZEROTHREE.year=FOURZEROTHREE.year+1

@staticmethod
def display_wlcome():
    print("Welcome")

FOURZEROTHREE.display_welcome()
    

x=FOURZEROTHREE("sachu",15,"Ernakulam")
y=FOURZEROTHREE("TRASH",0,"Global")

x.display()
y.display()

print("------------------------------------------------------s")
FOURZEROTHREE.year=FOURZEROTHREE.year+1


x.add_age()
y.add_age()
x.display()
y.display()
FOURZEROTHREE.year()